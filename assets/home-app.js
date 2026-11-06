/* Digital Infohub homepage: ticker, market pulse, daily insight, AI dock. */
(function () {
  'use strict';

  var FINNHUB_KEY = 'd9t07ohr01qqd5j2v6rgd9t07ohr01qqd5j2v6s0';
  var STOCKS = [
    { sym: 'AAPL', name: 'Apple' },
    { sym: 'NVDA', name: 'NVIDIA' },
    { sym: 'MSFT', name: 'Microsoft' },
    { sym: 'GOOGL', name: 'Alphabet' }
  ];
  var CRYPTO = [
    { sym: 'BTC', id: 'bitcoin', name: 'Bitcoin' },
    { sym: 'ETH', id: 'ethereum', name: 'Ethereum' }
  ];

  /* Internal tech-news headlines keep the ticker useful and on-site. */
  var NEWS = [
    { t: 'AI hardware race moves beyond the cloud', u: '/post/ai-hardware-race-sept-2026' },
    { t: 'AI capex fatigue sparks tech sell-off', u: '/post/tech-market-sell-off-october-2026' },
    { t: 'Security budgets shift to AI-assisted response', u: '/post/cybersecurity-ai-investment-2026' },
    { t: 'Quantum milestones bring practical use closer', u: '/post/quantum-computing-breakthroughs-2026' },
    { t: 'AI wearables lose the screen', u: '/post/ai-wearables-2026' },
    { t: 'iPhone 2026: what actually changed', u: '/post/newest-iphone-2026' },
    { t: 'The professional checklist for staying safe online', u: '/post/how-to-stay-safe-online-2026' },
    { t: 'Model wars: DeepSeek, Grok and Qwen', u: '/post/ai-model-wars-august-2026' }
  ];

  var $ = function (s) { return document.querySelector(s); };
  var $$ = function (s) { return Array.prototype.slice.call(document.querySelectorAll(s)); };
  var store = {
    get: function (k, d) { try { var v = localStorage.getItem(k); return v === null ? d : v; } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem(k, String(v)); } catch (e) {} }
  };
  var esc = function (s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  };
  var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function fetchTimeout(url, opts, ms) {
    var c = new AbortController();
    var t = setTimeout(function () { c.abort(); }, ms || 9000);
    return fetch(url, Object.assign({}, opts || {}, { signal: c.signal })).finally(function () { clearTimeout(t); });
  }

  /* ------------------------------------------------------------- market data */
  function getStocks(list) {
    return Promise.allSettled((list || STOCKS).map(function (s) {
      return fetchTimeout('https://finnhub.io/api/v1/quote?symbol=' + s.sym + '&token=' + FINNHUB_KEY)
        .then(function (r) { return r.json(); })
        .then(function (d) {
          if (!d || d.c == null) throw new Error('no data');
          return { sym: s.sym, name: s.name, price: Number(d.c), pct: Number(d.dp || 0) };
        });
    })).then(function (res) {
      return res.filter(function (r) { return r.status === 'fulfilled'; }).map(function (r) { return r.value; });
    });
  }

  function getCrypto(list) {
    var items = list || CRYPTO;
    var ids = items.map(function (c) { return c.id; }).join(',');
    return fetchTimeout('https://api.coingecko.com/api/v3/simple/price?ids=' + ids + '&vs_currencies=usd&include_24hr_change=true')
      .then(function (r) { return r.json(); })
      .then(function (d) {
        return items.map(function (c) {
          var v = d && d[c.id];
          if (!v || v.usd == null) return null;
          return { sym: c.sym, name: c.name, price: Number(v.usd), pct: Number(v.usd_24h_change || 0), crypto: true };
        }).filter(Boolean);
      })
      .catch(function () { return []; });
  }

  function fmtPrice(item) {
    if (item.crypto) {
      if (item.price >= 1000) return '$' + item.price.toLocaleString('en-US', { maximumFractionDigits: 0 });
      return '$' + item.price.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }
    return '$' + item.price.toFixed(2);
  }

  /* ------------------------------------------------------------------ ticker */
  function buildTicker(items) {
    var track = $('#tickerBar');
    if (!track) return;
    var nodes = [];
    items.forEach(function (it) {
      var up = it.pct >= 0;
      nodes.push('<a class="dih-ticker-item" href="/coincompass"><b>' + esc(it.sym) + '</b> ' + esc(fmtPrice(it)) +
        ' <span class="' + (up ? 'up' : 'down') + '">' + (up ? '▲' : '▼') + ' ' + Math.abs(it.pct).toFixed(2) + '%</span></a>');
    });
    NEWS.forEach(function (n) {
      nodes.push('<a class="dih-ticker-item news" href="' + esc(n.u) + '"><span class="news-tag">Tech news</span> ' + esc(n.t) + ' →</a>');
    });
    track.innerHTML = nodes.join('') + nodes.join('');
    sizeTicker(track);
  }

  function sizeTicker(track) {
    if (reduced) { track.style.animation = 'none'; return; }
    /* Constant reading speed (~58 px/s) instead of a fixed duration, so a long
       feed never races past and a short one never crawls. */
    requestAnimationFrame(function () {
      var width = track.scrollWidth / 2;
      if (!width) return;
      var duration = Math.max(85, Math.min(320, width / 45));
      track.style.setProperty('--dih-ticker-duration', duration.toFixed(1) + 's');
      var ticker = track.closest('.dih-ticker');
      if (ticker) ticker.style.setProperty('--dih-ticker-duration', duration.toFixed(1) + 's');
    });
  }

  function renderPulse(items) {
    var grid = $('#pulseGrid');
    if (!grid) return;
    var cards = items.map(function (it) {
      var up = it.pct >= 0;
      return '<a class="pulse-card" href="/coincompass">' +
        '<div class="pulse-left"><div class="pulse-sym">' + esc(it.sym) + '</div><div class="pulse-name">' + esc(it.name) + '</div></div>' +
        '<div class="pulse-right"><div class="pulse-price">' + esc(fmtPrice(it)) + '</div>' +
        '<div class="pulse-chg ' + (up ? 'up' : 'down') + '">' + (up ? '▲' : '▼') + ' ' + Math.abs(it.pct).toFixed(2) + '%</div></div></a>';
    });
    cards.push('<a class="pulse-card pulse-card--wide" href="/techtopics"><div class="pulse-left"><div class="pulse-sym">DEEP DIVES</div><div class="pulse-name">24 plain-language guides</div></div><div class="pulse-right"><div class="pulse-price">AI →</div><div class="pulse-chg up">Explore</div></div></a>');
    grid.innerHTML = cards.join('');
  }

  function loadMarkets() {
    Promise.all([getStocks(), getCrypto()]).then(function (res) {
      var items = res[0].concat(res[1]);
      if (!items.length) {
        var track = $('#tickerBar');
        if (track) {
          var nodes = NEWS.map(function (n) {
            return '<a class="dih-ticker-item news" href="' + esc(n.u) + '"><span class="news-tag">Tech news</span> ' + esc(n.t) + ' →</a>';
          });
          track.innerHTML = nodes.join('') + nodes.join('');
          sizeTicker(track);
        }
        var grid = $('#pulseGrid');
        if (grid) {
          grid.innerHTML =
            '<a class="pulse-card" href="/coincompass"><div class="pulse-left"><div class="pulse-sym">MARKETS</div><div class="pulse-name">Live quotes in CoinCompass</div></div><div class="pulse-right"><div class="pulse-price">→</div></div></a>' +
            '<a class="pulse-card" href="/post/tech-market-sell-off-october-2026"><div class="pulse-left"><div class="pulse-sym">ANALYSIS</div><div class="pulse-name">What the sell-off means</div></div><div class="pulse-right"><div class="pulse-price">→</div></div></a>' +
            '<a class="pulse-card pulse-card--wide" href="/techtopics"><div class="pulse-left"><div class="pulse-sym">DEEP DIVES</div><div class="pulse-name">24 plain-language guides</div></div><div class="pulse-right"><div class="pulse-price">AI →</div></div></a>';
        }
        return;
      }
      renderPulse(items);
      buildTicker(items);
    });
  }

  /* --------------------------------------------------------------- ask dock */
  var MODES = {
    search: { placeholder: 'Ask anything — or press / to focus', chips: ['How does WebGPU work?', 'Explain AI agents simply', 'Best laptop for developers'] },
    markets: { placeholder: 'Ask about stocks, crypto or a ticker…', chips: ['Market briefing', 'Bitcoin price', 'How is NVDA doing?'] },
    news: { placeholder: 'Search tech news…', chips: ['Latest tech news', 'AI', 'Cybersecurity', 'Apple'] },
    genai: { placeholder: 'Ask AI to write, explain or brainstorm…', chips: ['Explain WebGPU simply', 'Draft a tech newsletter intro', 'Compare cloud vs edge AI'] }
  };
  var mode = store.get('dih_chat_mode', 'search');
  if (!MODES[mode]) mode = 'search';
  var busy = false;
  var history = [];

  function setMode(next, silent) {
    if (!MODES[next]) next = 'search';
    mode = next;
    store.set('dih_chat_mode', next);
    $$('.ask-mode').forEach(function (b) { b.classList.toggle('active', b.dataset.mode === next); });
    var input = $('#chatInput');
    if (input) input.placeholder = MODES[next].placeholder;
    renderChips();
    if (!silent && document.body.classList.contains('chatting')) {
      var thread = $('#chatThread');
      if (thread && !thread.children.length) greet();
    }
  }

  function renderChips() {
    var box = $('#askChips');
    if (!box) return;
    box.innerHTML = (MODES[mode].chips || []).map(function (c) {
      return '<button type="button" class="ask-chip" data-q="' + esc(c) + '">' + esc(c) + '</button>';
    }).join('');
    box.querySelectorAll('.ask-chip').forEach(function (b) {
      b.addEventListener('click', function () { send(b.dataset.q); });
    });
  }

  function greet() {
    addMsg('bot',
      '<p>👋 <strong>Digital Infohub AI</strong> here. I can search the web, pull a market snapshot, scan tech news or draft something for you.</p>' +
      '<p style="color:var(--dih-text-muted);font-size:12px">You are in <strong>' + esc(mode === 'search' ? 'Ask' : mode === 'genai' ? 'AI assistant' : mode) + '</strong> mode. Switch modes with the icons in the dock.</p>' +
      '<div class="chat-follow-ups">' +
        '<button class="follow-up-btn" data-send="Latest tech news">📰 Today\'s tech news</button>' +
        '<button class="follow-up-btn" data-send="Market briefing">📈 Market briefing</button>' +
        '<button class="follow-up-btn" data-send="Explain AI agents simply">✨ Explain AI agents</button>' +
      '</div>');
  }

  function addMsg(role, html) {
    var thread = $('#chatThread');
    if (!thread) return;
    var d = document.createElement('div');
    d.className = 'msg ' + role;
    var avatar = role === 'bot'
      ? '<img src="/assets/logo.png" alt="" width="34" height="34">'
      : 'U';
    d.innerHTML = '<div class="msg-avatar ' + role + '">' + avatar + '</div>' +
      '<div class="msg-body"><div class="msg-header"><span class="msg-role">' + (role === 'bot' ? 'Digital Infohub AI' : 'You') + '</span>' +
      '<span class="msg-time">' + new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' }) + '</span></div>' +
      '<div class="msg-content">' + html + '</div></div>';
    thread.appendChild(d);
    d.querySelectorAll('.follow-up-btn').forEach(function (b) {
      b.addEventListener('click', function () { send(b.dataset.send); });
    });
    scrollChat(true);
  }

  function thinking() {
    var thread = $('#chatThread');
    var d = document.createElement('div');
    d.className = 'msg bot';
    d.innerHTML = '<div class="msg-avatar bot"><img src="/assets/logo.png" alt="" width="34" height="34"></div><div class="msg-body"><div class="msg-content"><div class="typing-indicator"><span></span><span></span><span></span></div></div></div>';
    thread.appendChild(d);
    scrollChat(true);
    return d;
  }

  function scrollChat(force) {
    var thread = $('#chatThread');
    if (thread && document.body.classList.contains('chatting')) {
      window.scrollTo({ top: document.body.scrollHeight, behavior: force ? 'auto' : 'smooth' });
    }
  }

  function sanitize(html) {
    return String(html)
      .replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, '')
      .replace(/\son\w+\s*=\s*"[^"]*"/gi, '')
      .replace(/\son\w+\s*=\s*'[^']*'/gi, '')
      .replace(/javascript:/gi, '#');
  }

  function markdown(text) {
    var html;
    try {
      html = window.dihMarkdown ? window.dihMarkdown(String(text)) : (window.marked ? marked.parse(String(text), { breaks: true, gfm: true }) : esc(text).replace(/\n/g, '<br>'));
    } catch (e) { html = esc(text).replace(/\n/g, '<br>'); }
    return sanitize(html);
  }

  async function webSearch(q) {
    try {
      var r = await fetchTimeout('https://api.duckduckgo.com/?q=' + encodeURIComponent(q) + '&format=json&no_html=1', {}, 7000);
      var d = await r.json();
      if (d && d.AbstractText) {
        var h = '<h3>🔍 ' + esc(d.Heading || q) + '</h3><div class="news-tldr">' + esc(d.AbstractText) + '</div>';
        if (d.AbstractURL) h += '<p style="margin-top:9px"><a href="' + esc(d.AbstractURL) + '" target="_blank" rel="noopener">Read more →</a></p>';
        return h;
      }
    } catch (e) {}
    return '<p>I could not fetch a live answer for that. Try a more specific question, or explore the hub:</p>' +
      '<div class="chat-follow-ups"><button class="follow-up-btn" data-send="Latest tech news">📰 Tech news</button>' +
      '<button class="follow-up-btn" data-send="Market briefing">📈 Market briefing</button></div>';
  }

  async function markets(q) {
    var items = (await getStocks()).concat(await getCrypto());
    if (!items.length) return '<p>Live market data is unavailable right now. <a href="/coincompass">Open CoinCompass</a> for the dashboard.</p>';
    var want = String(q || '').toUpperCase();
    var matches = items.filter(function (i) { return want.indexOf(i.sym) !== -1; });
    var shown = matches.length ? matches : items.slice(0, 6);
    var h = '<h3>📊 ' + (matches.length ? 'Snapshot: ' + matches.map(function (m) { return m.sym; }).join(', ') : 'Market snapshot') + '</h3>' +
      '<p style="color:var(--dih-text-muted);font-size:12px">Delayed quotes · tap CoinCompass for the full picture</p><div class="market-grid">';
    shown.forEach(function (it) {
      var up = it.pct >= 0;
      h += '<a class="market-item" href="/coincompass"><span class="market-symbol">' + esc(it.sym) + '</span>' +
        '<span class="market-price">' + esc(fmtPrice(it)) + '</span>' +
        '<span class="market-change ' + (up ? 'up' : 'down') + '">' + (up ? '▲' : '▼') + ' ' + Math.abs(it.pct).toFixed(2) + '%</span></a>';
    });
    h += '</div><div class="chat-follow-ups"><a class="follow-up-btn" href="/coincompass">Open CoinCompass →</a>' +
      '<a class="follow-up-btn" href="/post/tech-market-sell-off-october-2026">Read the market analysis →</a></div>';
    return h;
  }

  async function news(q) {
    try {
      var r = await fetchTimeout('https://api.rss2json.com/v1/api.json?rss_url=' + encodeURIComponent('https://techcrunch.com/feed/'));
      var d = await r.json();
      var items = (d.items || []).slice(0, 5);
      if (!items.length) throw new Error('empty');
      var key = String(q || '').toLowerCase();
      return '<h3>📰 Tech headlines</h3>' + items.map(function (i) {
        var title = String(i.title || '').replace(/<[^>]*>/g, '');
        var desc = String(i.description || '').replace(/<[^>]*>/g, '').slice(0, 160);
        var hit = key && key.length > 2 && (title + desc).toLowerCase().indexOf(key) !== -1;
        return '<a class="news-card" href="' + esc(i.link) + '" target="_blank" rel="noopener"' + (hit ? ' style="border-left:3px solid var(--dih-accent)"' : '') + '>' +
          '<div class="news-category">TechCrunch · ' + esc((i.pubDate || '').slice(0, 10)) + '</div>' +
          '<div class="news-title">' + esc(title) + '</div>' +
          '<div class="news-tldr">' + esc(desc) + '…</div></a>';
      }).join('') +
        '<div class="chat-follow-ups"><a class="follow-up-btn" href="/blog">Digital Infohub analysis →</a></div>';
    } catch (e) {
      return '<p>Live headlines are unavailable right now. Digital Infohub coverage is always here:</p>' +
        '<div class="chat-follow-ups"><a class="follow-up-btn" href="/blog">Read the blog →</a>' +
        '<a class="follow-up-btn" href="/techtopics">Browse tech guides →</a></div>';
    }
  }

  async function genai(q) {
    history.push({ role: 'user', content: q });
    if (history.length > 8) history = history.slice(-8);
    var sys = 'You are Digital Infohub AI, a sharp analyst for technology professionals, founders and investors. Be concise, practical and structured. Use markdown. When discussing markets, add a one-line strategic takeaway. Prefer concrete examples over hype.';
    try {
      var r = await fetchTimeout('https://text.pollinations.ai/openai', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ model: 'openai', messages: [{ role: 'system', content: sys }].concat(history), temperature: 0.6 })
      }, 28000);
      if (!r.ok) throw new Error('HTTP ' + r.status);
      var reply = '';
      var ct = r.headers.get('content-type') || '';
      if (ct.indexOf('json') !== -1) {
        var d = await r.json();
        reply = d && d.choices && d.choices[0] && d.choices[0].message ? d.choices[0].message.content : '';
      } else {
        reply = await r.text();
      }
      if (!reply || !reply.trim()) throw new Error('empty');
      history.push({ role: 'assistant', content: reply });
      return markdown(reply) + '<p style="margin-top:14px;font-size:10.5px;color:var(--dih-text-muted)">✨ Live model output — verify important facts.</p>';
    } catch (e) {
      history.pop();
      return '<p>⚠️ The AI model is busy right now. Try again, or use <strong>Ask</strong> mode for a web answer.</p>' +
        '<div class="chat-follow-ups"><button class="follow-up-btn" data-send="' + esc(q) + '">🔄 Retry</button>' +
        '<a class="follow-up-btn" href="/techtopics">Browse guides →</a></div>';
    }
  }

  async function send(text) {
    text = String(text || '').trim();
    if (!text || busy) return;
    busy = true;
    document.body.classList.add('chatting');
    var thread = $('#chatThread');
    if (thread && !thread.children.length) greet();
    addMsg('user', esc(text));
    var input = $('#chatInput');
    if (input) input.value = '';
    var sendBtn = $('#chatSend');
    var stopBtn = $('#chatStop');
    if (sendBtn) sendBtn.style.display = 'none';
    if (stopBtn) stopBtn.style.display = 'flex';
    if (input) input.disabled = true;
    var th = thinking();
    var out;
    try {
      if (mode === 'markets') out = await markets(text);
      else if (mode === 'news') out = await news(text);
      else if (mode === 'genai') out = await genai(text);
      else out = await webSearch(text);
    } catch (e) {
      out = '<p>⚠️ Something went wrong. Please try again.</p><div class="chat-follow-ups"><button class="follow-up-btn" data-send="' + esc(text) + '">🔄 Retry</button></div>';
    }
    th.remove();
    addMsg('bot', out);
    busy = false;
    if (sendBtn) sendBtn.style.display = 'flex';
    if (stopBtn) stopBtn.style.display = 'none';
    if (input) { input.disabled = false; input.focus({ preventScroll: true }); }
  }

  window.dihSend = send;

  /* ----------------------------------------------------------- daily insight */
  function dailyInsight() {
    var host = $('#homeDailyInsight');
    if (!host) return;
    var tips = [
      { icon: '💡', label: 'Productivity', title: 'Use the 2-minute rule', text: 'If a task takes less than two minutes, do it now instead of adding it to a list. Your future self will thank you.' },
      { icon: '🔐', label: 'Security', title: 'Turn on passkeys', text: 'Passkeys are phishing-resistant and faster than passwords. Enable them for email, banking and your main SaaS accounts first.' },
      { icon: '🤖', label: 'AI prompting', title: 'Give the model a role', text: '“Act as a senior engineer reviewing this code for performance bottlenecks” beats “make this better” every time.' },
      { icon: '📈', label: 'Markets', title: 'Separate signal from noise', text: 'One headline is noise. A shift in guidance, capex or hiring is signal. Ask what changed in the next four quarters.' },
      { icon: '⚡', label: 'Shortcut', title: 'Win + V / Cmd + Shift + V', text: 'Windows clipboard history and macOS paste-and-match will save you hundreds of context switches a week.' }
    ];
    var day = new Date().toDateString();
    var idx = 0;
    if (store.get('dih_insight_day', '') === day) {
      idx = parseInt(store.get('dih_insight_idx', '0'), 10) || 0;
    } else {
      idx = Math.floor(Math.random() * tips.length);
      store.set('dih_insight_day', day);
      store.set('dih_insight_idx', idx);
    }
    var tip = tips[idx];
    host.innerHTML = '<div class="insight"><div class="insight-icon">' + tip.icon + '</div>' +
      '<div class="insight-body"><div class="insight-label">Daily insight · ' + esc(tip.label) + '</div>' +
      '<h3>' + esc(tip.title) + '</h3><p>' + esc(tip.text) + '</p></div>' +
      '<button class="insight-copy" id="insightCopy" title="Copy this insight" aria-label="Copy this insight">📋</button></div>';
    var btn = $('#insightCopy');
    if (btn) {
      btn.addEventListener('click', function () {
        var text = tip.title + ' — ' + tip.text;
        if (navigator.clipboard) navigator.clipboard.writeText(text).then(function () {
          if (window.dihToast) window.dihToast('Insight copied. Share it with your team.');
          btn.textContent = '✅';
          setTimeout(function () { btn.textContent = '📋'; }, 1800);
        });
      });
    }
  }

  /* --------------------------------------------------------- resume reading */
  function initResume() {
    var card = $('#resumeCard');
    if (!card) return;
    var last = null;
    try { last = JSON.parse(store.get('dih_last_read', 'null')); } catch (e) {}
    if (!last || !last.u) return;
    var title = $('#resumeTitle');
    var link = $('#resumeLink');
    var img = card.querySelector('img');
    if (title) title.textContent = last.t || 'Continue reading';
    if (link) link.href = last.u;
    if (img && last.i) img.src = last.i;
    card.classList.add('show');
    $$('.article-card[data-resume-title]').forEach(function (a) {
      a.addEventListener('click', function () {
        var im = a.querySelector('img');
        store.set('dih_last_read', JSON.stringify({
          u: a.getAttribute('href'),
          t: a.getAttribute('data-resume-title'),
          i: im ? im.getAttribute('src') : ''
        }));
      });
    });
  }

  /* --------------------------------------------------------------- bootstrap */
  document.addEventListener('DOMContentLoaded', function () {
    var form = $('#chatForm');
    var input = $('#chatInput');
    var chips = $('#askChips');

    $$('.ask-mode').forEach(function (b) {
      b.addEventListener('click', function () { setMode(b.dataset.mode); });
    });
    setMode(mode, true);

    if (form) form.addEventListener('submit', function (e) { e.preventDefault(); send(input.value); });
    if (input) {
      input.addEventListener('focus', function () { if (chips) chips.classList.add('active'); });
      input.addEventListener('blur', function () { setTimeout(function () { if (chips) chips.classList.remove('active'); }, 180); });
    }
    var back = $('#chatBack');
    if (back) back.addEventListener('click', function () {
      document.body.classList.remove('chatting');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    var stop = $('#chatStop');
    if (stop) stop.addEventListener('click', function () {
      busy = false;
      stop.style.display = 'none';
      var s = $('#chatSend'); if (s) s.style.display = 'flex';
      if (input) input.disabled = false;
    });

    document.addEventListener('keydown', function (e) {
      if ((e.key === '/' || ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k')) && !/input|textarea|select/i.test(e.target.tagName)) {
        e.preventDefault();
        document.body.classList.add('chatting');
        if (input) input.focus();
        if (chips) chips.classList.add('active');
      }
      if (e.key === 'Escape' && document.body.classList.contains('chatting')) {
        document.body.classList.remove('chatting');
      }
    });

    dailyInsight();
    initResume();
    loadMarkets();

    /* The homepage covers its own ad slot once, after layout settles. */
    try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
  });
})();
