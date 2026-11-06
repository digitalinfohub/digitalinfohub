/* Digital Infohub — live tech headlines.
 * Production uses the Worker at /api/news (TechCrunch RSS, cached at the edge).
 * Local preview and feed outages fall back to rss2json, then to a small set of
 * evergreen Digital Infohub reads so the section is never blank.
 */
(function () {
  'use strict';

  var feeds = Array.prototype.slice.call(document.querySelectorAll('[data-news-feed]'));
  if (!feeds.length) return;

  var statusNodes = Array.prototype.slice.call(document.querySelectorAll('[data-news-status]'));
  var updatedNodes = Array.prototype.slice.call(document.querySelectorAll('[data-news-updated]'));
  var freshNodes = Array.prototype.slice.call(document.querySelectorAll('[data-fresh-time]'));
  var refreshButtons = Array.prototype.slice.call(document.querySelectorAll('[data-news-refresh]'));
  var tabs = Array.prototype.slice.call(document.querySelectorAll('[data-news-filter]'));
  var currentFilter = 'all';
  var allItems = [];
  var cacheKey = 'dih_news_cache_v2';
  var maxAge = 5 * 60 * 1000;

  var FALLBACK = [
    {
      title: 'AI agents meet the next market catalysts',
      link: '/post/ai-agent-economy-october-catalysts',
      summary: 'What changes when agents move from demos into real workflows — and what investors are watching next.',
      date: new Date().toISOString(),
      category: 'ai',
      source: 'Digital Infohub'
    },
    {
      title: 'The AI hardware race is moving beyond the cloud',
      link: '/post/ai-hardware-race-sept-2026',
      summary: 'On-device inference changes the cost curve, the privacy story and the product design.',
      date: new Date().toISOString(),
      category: 'hardware',
      source: 'Digital Infohub'
    },
    {
      title: 'Security is becoming an identity problem',
      link: '/cybersecurity',
      summary: 'Most breaches start with a stolen session or a weak credential, not a broken firewall.',
      date: new Date().toISOString(),
      category: 'security',
      source: 'Digital Infohub'
    },
    {
      title: 'Crypto and stock graphs, without the noise',
      link: '/coincompass',
      summary: 'Live prices and context in one calm dashboard, built for decisions rather than dopamine.',
      date: new Date().toISOString(),
      category: 'markets',
      source: 'Digital Infohub'
    },
    {
      title: 'Quantum computing: the breakthroughs that matter',
      link: '/quantumcomputing',
      summary: 'A plain-language guide to qubits, error correction and the encryption migration to plan for.',
      date: new Date().toISOString(),
      category: 'hardware',
      source: 'Digital Infohub'
    },
    {
      title: 'How well do you actually know tech?',
      link: '/quiz',
      summary: 'Six quick quizzes with a grade for every topic, plus a guide for what to learn next.',
      date: new Date().toISOString(),
      category: 'ai',
      source: 'Digital Infohub'
    }
  ];

  function esc(value) {
    return String(value == null ? '' : value).replace(/[&<>"']/g, function (ch) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[ch];
    });
  }

  function stripHtml(value) {
    return String(value || '')
      .replace(/<script[\s\S]*?<\/script>/gi, ' ')
      .replace(/<style[\s\S]*?<\/style>/gi, ' ')
      .replace(/<[^>]+>/g, ' ')
      .replace(/&nbsp;/gi, ' ')
      .replace(/&amp;/gi, '&')
      .replace(/&quot;/gi, '"')
      .replace(/&#39;/gi, "'")
      .replace(/&lt;/gi, '<')
      .replace(/&gt;/gi, '>')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function classify(item) {
    var haystack = (String(item.title || '') + ' ' + String(item.summary || '') + ' ' + String(item.category || '')).toLowerCase();
    if (/\b(ai|artificial intelligence|model|openai|anthropic|llm|agent|robot)\b/.test(haystack)) return 'ai';
    if (/\b(security|cyber|hack|breach|malware|ransomware|vulnerab|privacy)\b/.test(haystack)) return 'security';
    if (/\b(chip|semiconductor|hardware|device|phone|laptop|apple|nvidia|amd|intel|gpu)\b/.test(haystack)) return 'hardware';
    if (/\b(startup|funding|raises|venture|seed|series [a-c]|acquisition|ipo)\b/.test(haystack)) return 'startups';
    if (/\b(market|stock|crypto|bitcoin|nasdaq|investor|shares)\b/.test(haystack)) return 'markets';
    return 'startups';
  }

  function when(value) {
    var date = value ? new Date(value) : null;
    if (!date || isNaN(date.getTime())) return 'Just now';
    var diff = Math.max(0, Date.now() - date.getTime());
    var mins = Math.floor(diff / 60000);
    if (mins < 2) return 'Just now';
    if (mins < 60) return mins + ' min ago';
    var hours = Math.floor(mins / 60);
    if (hours < 24) return hours + (hours === 1 ? ' hour ago' : ' hours ago');
    var days = Math.floor(hours / 24);
    if (days < 7) return days + (days === 1 ? ' day ago' : ' days ago');
    try {
      return date.toLocaleDateString(undefined, { month: 'short', day: 'numeric' });
    } catch (e) {
      return date.toISOString().slice(0, 10);
    }
  }

  function stamp() {
    var now = new Date();
    var time = '';
    try {
      time = now.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' });
    } catch (e) {}
    return 'Updated just now' + (time ? ' · ' + time : '');
  }

  function setStatus(text) {
    statusNodes.forEach(function (node) { node.textContent = text; });
  }

  function setUpdated(text) {
    updatedNodes.forEach(function (node) { node.textContent = text; });
    freshNodes.forEach(function (node) {
      node.textContent = 'just now' + (text.indexOf('·') !== -1 ? ' · ' + text.split('·').pop().trim() : '');
    });
  }

  function card(item) {
    var category = item.category || classify(item);
    var link = String(item.link || '');
    var external = /^https?:\/\//i.test(link);
    var href = external || /^\//.test(link) ? link : '/news';
    var source = item.source || (external ? 'TechCrunch' : 'Digital Infohub');
    return '<a class="dih-news-card" href="' + esc(href) + '"' + (external ? ' target="_blank" rel="noopener noreferrer"' : '') + ' data-news-cat="' + esc(category) + '">' +
      '<div class="dih-news-card-top"><span class="dih-news-card-tag">' + esc(category) + '</span><span class="dih-news-card-source">' + esc(source) + '</span></div>' +
      '<h3>' + esc(item.title) + '</h3>' +
      '<p>' + esc(String(item.summary || '').slice(0, 190)) + (String(item.summary || '').length > 190 ? '…' : '') + '</p>' +
      '<div class="dih-news-card-foot"><span>' + esc(when(item.date)) + '</span><span class="dih-news-card-arrow">Read →</span></div>' +
      '</a>';
  }

  function render() {
    var items = currentFilter === 'all' ? allItems : allItems.filter(function (item) {
      return (item.category || classify(item)) === currentFilter;
    });
    feeds.forEach(function (feed) {
      var limit = parseInt(feed.getAttribute('data-news-limit') || '8', 10) || 8;
      var shown = items.slice(0, limit);
      if (!shown.length) {
        feed.innerHTML = '<p class="dih-news-empty">No stories in this filter right now. Try <button type="button" class="dih-news-inline-btn" data-news-clear>All headlines</button>.</p>';
      } else {
        feed.innerHTML = shown.map(card).join('');
      }
      feed.setAttribute('aria-busy', 'false');
      feed.classList.toggle('is-compact', feed.getAttribute('data-news-limit') === '4');
    });
    var clear = document.querySelector('[data-news-clear]');
    if (clear) clear.addEventListener('click', function () { setFilter('all'); });
  }

  function setFilter(filter) {
    currentFilter = filter || 'all';
    tabs.forEach(function (tab) {
      var active = tab.getAttribute('data-news-filter') === currentFilter;
      tab.classList.toggle('is-active', active);
      tab.setAttribute('aria-selected', active ? 'true' : 'false');
    });
    render();
  }

  function normalizeRss2Json(data) {
    var items = (data && data.items) || [];
    return items.map(function (item) {
      return {
        title: stripHtml(item.title),
        link: String(item.link || ''),
        summary: stripHtml(item.description || item.content || '').slice(0, 240),
        date: item.pubDate || item.pubDate,
        category: classify({ title: item.title, summary: item.description, category: item.categories }),
        source: 'TechCrunch'
      };
    }).filter(function (item) { return item.title && item.link; });
  }

  function readCache() {
    try {
      var raw = sessionStorage.getItem(cacheKey);
      if (!raw) return null;
      var parsed = JSON.parse(raw);
      if (!parsed || !parsed.t || !Array.isArray(parsed.items)) return null;
      if (Date.now() - parsed.t > maxAge) return null;
      return parsed.items;
    } catch (e) { return null; }
  }

  function writeCache(items) {
    try {
      sessionStorage.setItem(cacheKey, JSON.stringify({ t: Date.now(), items: items }));
    } catch (e) {}
  }

  function finish(items, source, message) {
    allItems = items && items.length ? items : FALLBACK;
    if (items && items.length) writeCache(allItems);
    setUpdated(stamp());
    setStatus(message || 'Showing ' + allItems.length + ' live headlines · source: ' + source);
    render();
  }

  async function load(force) {
    if (!force) {
      var cached = readCache();
      if (cached && cached.length) {
        allItems = cached;
        setUpdated(stamp());
        setStatus('Showing ' + cached.length + ' live headlines · cached for a few minutes');
        render();
        return;
      }
    }

    feeds.forEach(function (feed) { feed.setAttribute('aria-busy', 'true'); });
    setStatus('Loading live headlines…');

    try {
      var response = await fetch('/api/news', { headers: { Accept: 'application/json' } });
      if (response.ok) {
        var payload = await response.json();
        var items = (payload && payload.items) || [];
        if (items.length) {
          finish(items.map(function (item) {
            item.category = item.category || classify(item);
            item.source = payload.source || 'TechCrunch';
            return item;
          }), payload.source || 'TechCrunch');
          return;
        }
      }
    } catch (e) { /* local preview has no Worker */ }

    try {
      var rss = await fetch('https://api.rss2json.com/v1/api.json?rss_url=' + encodeURIComponent('https://techcrunch.com/feed/'));
      if (rss.ok) {
        var data = await rss.json();
        var normalized = normalizeRss2Json(data);
        if (normalized.length) {
          finish(normalized, 'TechCrunch');
          return;
        }
      }
    } catch (e) {}

    finish(FALLBACK, 'Digital Infohub', 'Live feed unavailable right now — showing recent Digital Infohub picks.');
  }

  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      setFilter(tab.getAttribute('data-news-filter'));
    });
  });
  refreshButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      button.classList.add('is-spinning');
      load(true).finally(function () {
        setTimeout(function () { button.classList.remove('is-spinning'); }, 450);
      });
    });
  });

  load(false);
  setInterval(function () {
    if (allItems.length) render();
  }, 60000);
})();
