/* Digital Infohub — Freebuff Sites Worker.
 * Serves the static site and a small cached TechCrunch RSS endpoint at /api/news.
 * No Node APIs: this runs in the Workers runtime.
 */

const FEED_URL = 'https://techcrunch.com/feed/';
const CACHE_KEY = 'https://digitalinfohub.internal/api/news';
const MAX_ITEMS = 12;

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      'content-type': 'application/json; charset=utf-8',
      'cache-control': status === 200 ? 'public, max-age=300, s-maxage=600' : 'no-store',
      'access-control-allow-origin': '*',
      'x-content-type-options': 'nosniff'
    }
  });
}

function decode(value) {
  return String(value || '')
    .replace(/<!\[CDATA\[|\]\]>/g, '')
    .replace(/&#(\d+);/g, (_, n) => String.fromCharCode(Number(n)))
    .replace(/&#x([0-9a-f]+);/gi, (_, n) => String.fromCharCode(parseInt(n, 16)))
    .replace(/&nbsp;/gi, ' ')
    .replace(/&amp;/gi, '&')
    .replace(/&quot;/gi, '"')
    .replace(/&#39;|&apos;/gi, "'")
    .replace(/&lt;/gi, '<')
    .replace(/&gt;/gi, '>');
}

function strip(value) {
  return decode(String(value || '')
    .replace(/<script[\s\S]*?<\/script>/gi, ' ')
    .replace(/<style[\s\S]*?<\/style>/gi, ' ')
    .replace(/<[^>]+>/g, ' '))
    .replace(/\s+/g, ' ')
    .trim();
}

function tag(block, name) {
  const match = block.match(new RegExp('<' + name + '(?:\\s[^>]*)?>([\\s\\S]*?)<\\/' + name + '>', 'i'));
  return match ? decode(match[1]).trim() : '';
}

function classify(title, summary, sourceCategory) {
  const haystack = (title + ' ' + summary + ' ' + sourceCategory).toLowerCase();
  if (/\b(ai|artificial intelligence|model|openai|anthropic|llm|agent|robot)\b/.test(haystack)) return 'ai';
  if (/\b(security|cyber|hack|breach|malware|ransomware|vulnerab|privacy)\b/.test(haystack)) return 'security';
  if (/\b(chip|semiconductor|hardware|device|phone|laptop|apple|nvidia|amd|intel|gpu)\b/.test(haystack)) return 'hardware';
  if (/\b(market|stock|crypto|bitcoin|nasdaq|investor|shares)\b/.test(haystack)) return 'markets';
  return 'startups';
}

function parseFeed(xml) {
  const items = [];
  const blocks = String(xml || '').match(/<item\b[^>]*>[\s\S]*?<\/item>/gi) || [];
  for (const block of blocks) {
    const title = strip(tag(block, 'title'));
    if (!title) continue;
    const rawLink = tag(block, 'link').trim();
    const summary = strip(tag(block, 'description') || tag(block, 'content:encoded')).slice(0, 360);
    const rawDate = tag(block, 'pubDate');
    const sourceCategory = tag(block, 'category');
    let link = '';
    try {
      const parsed = new URL(rawLink);
      if (parsed.hostname === 'techcrunch.com' || parsed.hostname.endsWith('.techcrunch.com')) link = parsed.toString();
    } catch (e) { continue; }
    if (!link) continue;
    const date = rawDate ? new Date(rawDate) : new Date();
    items.push({
      title,
      link,
      summary,
      date: isNaN(date.getTime()) ? new Date().toISOString() : date.toISOString(),
      category: classify(title, summary, sourceCategory),
      source: 'TechCrunch'
    });
    if (items.length >= MAX_ITEMS) break;
  }
  return items;
}

async function news(ctx) {
  let cache = null;
  try {
    if (typeof caches !== 'undefined' && caches.default) cache = caches.default;
  } catch (e) { /* cache unavailable in local test */ }

  if (cache) {
    try {
      const hit = await cache.match(CACHE_KEY);
      if (hit) return hit;
    } catch (e) { /* ignore cache read failure */ }
  }

  try {
    const response = await fetch(FEED_URL, {
      headers: {
        'user-agent': 'DigitalInfohub/1.0 (+https://digitalinfohub.net)',
        accept: 'application/rss+xml, application/xml, text/xml;q=0.9, */*;q=0.8'
      },
      cf: { cacheTtl: 300, cacheEverything: true }
    });
    if (!response.ok) throw new Error('HTTP ' + response.status);
    const xml = await response.text();
    const items = parseFeed(xml);
    if (!items.length) throw new Error('empty feed');
    const result = json({ ok: true, source: 'TechCrunch', updated: new Date().toISOString(), items }, 200);
    if (cache && ctx && ctx.waitUntil) {
      ctx.waitUntil(cache.put(CACHE_KEY, result.clone()).catch(() => {}));
    }
    return result;
  } catch (error) {
    return json({
      ok: false,
      source: 'TechCrunch',
      updated: new Date().toISOString(),
      items: [],
      error: 'feed-unavailable'
    }, 502);
  }
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    if (url.pathname === '/api/news') {
      if (request.method !== 'GET' && request.method !== 'HEAD') {
        return json({ ok: false, error: 'method-not-allowed' }, 405);
      }
      return news(ctx);
    }

    let response = await env.ASSETS.fetch(request);

    // Pretty URLs: /blog -> /blog.html, /software/infohubgpt -> .html.
    if (response.status === 404 && request.method === 'GET' && url.pathname !== '/' &&
        !url.pathname.endsWith('/') && !/\.[^/]+$/.test(url.pathname)) {
      const alternative = new URL(request.url);
      alternative.pathname = url.pathname + '.html';
      const retry = await env.ASSETS.fetch(new Request(alternative.toString(), request));
      if (retry.status !== 404) response = retry;
    }

    return response;
  }
};
