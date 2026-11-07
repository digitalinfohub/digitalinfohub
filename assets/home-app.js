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
    cards.push('<a class="pulse-card pulse-card--wide" href="/techtopics"><div class="pulse-left"><div class="pulse-sym">DEEP DIVES</div><div class="pulse-name">30 plain-language guides</div></div><div class="pulse-right"><div class="pulse-price">AI →</div><div class="pulse-chg up">Explore</div></div></a>');
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
            '<a class="pulse-card pulse-card--wide" href="/techtopics"><div class="pulse-left"><div class="pulse-sym">DEEP DIVES</div><div class="pulse-name">30 plain-language guides</div></div><div class="pulse-right"><div class="pulse-price">AI →</div></div></a>';
        }
        return;
      }
      renderPulse(items);
      buildTicker(items);
    });
  }


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
    dailyInsight();
    initResume();
    loadMarkets();

    /* The homepage covers its own ad slot once, after layout settles. */
    try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
  });
})();
