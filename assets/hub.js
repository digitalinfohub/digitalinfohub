/* Digital Infohub — hub layer.
   Adds the shared extras on top of site.js: interest logging, sound design,
   a working share sheet, navigation dropdowns, the Hub Guide (rule-based
   assistant) and the interest board. Loaded automatically by site.js. */
(function () {
  'use strict';
  if (window.__dihHubLoaded) return;
  window.__dihHubLoaded = true;

  var root = document.documentElement;
  var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var DB_KEY = 'dih::userinterest';
  var SOUND_KEY = 'dih_sound';

  function store(key, value) {
    try {
      if (value === undefined) return localStorage.getItem(key);
      localStorage.setItem(key, String(value));
    } catch (e) { return null; }
  }
  function readJSON(key, fallback) {
    try { return JSON.parse(store(key) || '') || fallback; } catch (e) { return fallback; }
  }
  function norm(path) {
    var p = String(path || location.pathname).split('?')[0].split('#')[0];
    p = p.replace(/\/index\.html$/, '/').replace(/\.html$/, '');
    if (p.length > 1) p = p.replace(/\/+$/, '');
    return p || '/';
  }
  function esc(s) {
    return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  /* ------------------------------------------------------------- catalog */
  var catalog = null;
  function loadCatalog(cb) {
    if (catalog) { cb(catalog); return; }
    if (window.DIH_CATALOG) { catalog = window.DIH_CATALOG; cb(catalog); return; }
    var s = document.createElement('script');
    s.src = '/assets/catalog.js?v=20261202';
    s.async = true;
    s.onload = function () { catalog = window.DIH_CATALOG || []; cb(catalog); };
    s.onerror = function () { catalog = []; cb(catalog); };
    document.head.appendChild(s);
  }

  /* ------------------------------------------------------------ interest */
  var interest = {
    all: function () { return readJSON(DB_KEY, {}); },
    record: function (path, kind) {
      var db = interest.all();
      var key = norm(path);
      var row = db[key] || { views: 0, clicks: 0, first: Date.now(), last: 0 };
      if (kind === 'click') row.clicks += 1; else row.views += 1;
      row.last = Date.now();
      db[key] = row;
      try { localStorage.setItem(DB_KEY, JSON.stringify(db)); } catch (e) {}
      return db;
    },
    list: function () {
      var db = interest.all();
      var out = [];
      for (var k in db) {
        if (!Object.prototype.hasOwnProperty.call(db, k)) continue;
        var row = db[k] || {};
        out.push({
          path: k,
          views: row.views || 0,
          clicks: row.clicks || 0,
          score: (row.views || 0) + (row.clicks || 0) * 1.5,
          last: row.last || 0
        });
      }
      out.sort(function (a, b) { return b.score - a.score || b.last - a.last; });
      return out;
    },
    top: function (n) {
      var db = interest.all();
      var list = interest.list().filter(function (r) { return r.score > 0; });
      return list.slice(0, n || 6).map(function (r) {
        var meta = sourceMeta(r.path);
        return { path: r.path, title: meta.title, cat: meta.cat, score: Math.round(r.score), views: r.views, clicks: r.clicks };
      });
    },
    seen: function (path) {
      var db = interest.all();
      return !!db[norm(path)];
    },
    reset: function () {
      try { localStorage.removeItem(DB_KEY); } catch (e) {}
    },
    exportFile: function () {
      var payload = {
        generated: new Date().toISOString(),
        note: 'Per-browser interest log. Views and taps recorded on this device only.',
        pages: interest.list()
      };
      var blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'userinterest.json';
      document.body.appendChild(a);
      a.click();
      setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1500);
    }
  };

  function sourceMeta(path) {
    var p = norm(path);
    var found = null;
    (catalog || []).some(function (row) {
      if (norm(row.path) === p) { found = row; return true; }
      return false;
    });
    if (found) return found;
    var title = (document.title || p).replace(/\s*[|—–]\s*Digital Infohub.*$/i, '');
    return { path: p, title: title, cat: 'page' };
  }
  window.DIH = window.DIH || {};
  window.DIH.interest = interest;

  /* --------------------------------------------------------------- sound */
  var ctx = null;
  var lastSound = 0;
  var unlocked = false;
  var soundOn = store(SOUND_KEY) === null ? !reduced : store(SOUND_KEY) === '1';

  /* Browsers forbid audio before a gesture. Stay silent (and avoid the
     console warning flood) until the visitor touches or types something. */
  function unlockAudio() {
    unlocked = true;
    if (ctx && ctx.state === 'suspended') { try { ctx.resume(); } catch (e) {} }
  }
  ['pointerdown', 'keydown'].forEach(function (evt) {
    document.addEventListener(evt, unlockAudio, { once: true, passive: true });
  });

  function audio() {
    if (!soundOn || !unlocked) return null;
    try {
      var AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) return null;
      if (!ctx) ctx = new AC();
      if (ctx.state === 'suspended') ctx.resume();
      return ctx;
    } catch (e) { return null; }
  }
  function tone(freq, dur, type, gain, delay) {
    var ac = audio();
    if (!ac) return;
    var t0 = ac.currentTime + (delay || 0);
    var osc = ac.createOscillator();
    var amp = ac.createGain();
    osc.type = type || 'sine';
    osc.frequency.setValueAtTime(freq, t0);
    amp.gain.setValueAtTime(0.0001, t0);
    amp.gain.exponentialRampToValueAtTime(gain == null ? 0.05 : gain, t0 + 0.012);
    amp.gain.exponentialRampToValueAtTime(0.0001, t0 + (dur || 0.09));
    osc.connect(amp);
    amp.connect(ac.destination);
    osc.start(t0);
    osc.stop(t0 + (dur || 0.09) + 0.02);
  }

  var sfx = {
    enabled: function () { return soundOn; },
    set: function (on) {
      soundOn = !!on;
      store(SOUND_KEY, soundOn ? '1' : '0');
      syncSoundButton();
      if (soundOn) sfx.play('on');
    },
    toggle: function () { sfx.set(!soundOn); },
    play: function (name) {
      if (!soundOn) return;
      var now = Date.now();
      if (name === 'click' && now - lastSound < 45) return;
      lastSound = now;
      switch (name) {
        case 'click': tone(520, 0.05, 'sine', 0.035); break;
        case 'nav': tone(392, 0.07, 'sine', 0.03); tone(587, 0.08, 'sine', 0.024, 0.05); break;
        case 'open': tone(440, 0.09, 'triangle', 0.04); tone(660, 0.12, 'triangle', 0.03, 0.06); break;
        case 'success': tone(523, 0.09, 'sine', 0.045); tone(659, 0.09, 'sine', 0.04, 0.08); tone(784, 0.14, 'sine', 0.035, 0.16); break;
        case 'error': tone(220, 0.16, 'triangle', 0.05); break;
        case 'on': tone(660, 0.07, 'sine', 0.03); tone(880, 0.1, 'sine', 0.026, 0.07); break;
        case 'off': tone(320, 0.1, 'sine', 0.03); break;
        case 'type': tone(1200, 0.012, 'square', 0.008); break;
      }
    }
  };
  window.DIH.sfx = sfx;

  function syncSoundButton() {
    document.querySelectorAll('[data-dih-sound]').forEach(function (b) {
      /* .on / .off SVGs inside the button follow aria-pressed. */
      var label = soundOn ? 'Sound on — tap to mute' : 'Sound off — tap to enable';
      b.setAttribute('aria-label', label);
      b.setAttribute('aria-pressed', soundOn ? 'true' : 'false');
      b.title = label + ' (Shift+S)';
    });
  }

  /* --------------------------------------------------------- share sheet */
  var sheet = null;
  function shareLinks(url, title) {
    var u = encodeURIComponent(url);
    var t = encodeURIComponent(title);
    return [
      { label: 'Copy link', icon: '🔗', action: 'copy' },
      { label: 'X', icon: '𝕏', href: 'https://twitter.com/intent/tweet?text=' + t + '&url=' + u },
      { label: 'WhatsApp', icon: '💬', href: 'https://wa.me/?text=' + t + '%20' + u },
      { label: 'LinkedIn', icon: 'in', href: 'https://www.linkedin.com/sharing/share-offsite/?url=' + u },
      { label: 'Facebook', icon: 'f', href: 'https://www.facebook.com/sharer/sharer.php?u=' + u },
      { label: 'Email', icon: '✉️', href: 'mailto:?subject=' + t + '&body=' + t + '%0A%0A' + u }
    ];
  }

  function openShare(title, url, text) {
    title = title || document.title;
    url = url || location.href;
    closeShare();
    sheet = document.createElement('div');
    sheet.className = 'dih-sheet-wrap';
    sheet.setAttribute('role', 'dialog');
    sheet.setAttribute('aria-modal', 'true');
    sheet.setAttribute('aria-label', 'Share this page');
    sheet.innerHTML =
      '<div class="dih-sheet">' +
        '<div class="dih-sheet-head">' +
          '<div><span class="dih-sheet-kicker">Share</span><strong>' + esc(title) + '</strong></div>' +
          '<button type="button" class="dih-sheet-x" aria-label="Close share">✕</button>' +
        '</div>' +
        '<div class="dih-sheet-grid">' +
          shareLinks(url, title).map(function (l) {
            if (l.action === 'copy') return '<button type="button" class="dih-sheet-link" data-copy-url="' + esc(url) + '"><span aria-hidden="true">' + l.icon + '</span>' + l.label + '</button>';
            return '<a class="dih-sheet-link" href="' + l.href + '" target="_blank" rel="noopener noreferrer"><span aria-hidden="true">' + l.icon + '</span>' + l.label + '</a>';
          }).join('') +
          (navigator.share ? '<button type="button" class="dih-sheet-link" data-native-share><span aria-hidden="true">📲</span>More options</button>' : '') +
        '</div>' +
        '<div class="dih-sheet-url"><input type="text" readonly value="' + esc(url) + '" aria-label="Page link"><button type="button" data-copy-url="' + esc(url) + '">Copy</button></div>' +
        '<p class="dih-sheet-note">' + (text ? esc(text) : 'Send it to someone who would find it useful.') + '</p>' +
      '</div>';
    document.body.appendChild(sheet);
    document.body.classList.add('dih-sheet-open');
    requestAnimationFrame(function () { sheet.classList.add('is-open'); });
    var closeBtn = sheet.querySelector('.dih-sheet-x');
    if (closeBtn) closeBtn.focus();
    sheet.addEventListener('click', function (e) {
      if (e.target === sheet) closeShare();
      var copy = e.target.closest('[data-copy-url]');
      if (copy) { copyText(copy.getAttribute('data-copy-url')); sfx.play('success'); }
      var native = e.target.closest('[data-native-share]');
      if (native && navigator.share) {
        navigator.share({ title: title, text: text || title, url: url }).catch(function () {});
      }
    });
    document.addEventListener('keydown', onSheetKey);
  }
  function onSheetKey(e) {
    if (e.key === 'Escape') closeShare();
  }
  function closeShare() {
    if (!sheet) return;
    var el = sheet;
    sheet = null;
    el.classList.remove('is-open');
    document.body.classList.remove('dih-sheet-open');
    document.removeEventListener('keydown', onSheetKey);
    setTimeout(function () { el.remove(); }, 260);
  }
  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        if (window.dihToast) window.dihToast('Link copied — send it anywhere.');
      }, function () { legacyCopy(text); });
    } else {
      legacyCopy(text);
    }
  }
  function legacyCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); if (window.dihToast) window.dihToast('Link copied.'); } catch (e) {
      if (window.dihToast) window.dihToast(text);
    }
    ta.remove();
  }
  window.DIH.share = openShare;
  window.DIH.copy = copyText;

  /* -------------------------------------------------------------- chrome */
  var MENUS = [
    {
      match: '/software',
      label: 'Software',
      items: [
        ['/software', '🛠️', 'All software & tools', 'Every free tool in one place'],
        ['/software#tools', '⚡', 'Instant tools', 'Calculators, converters, formatters'],
        ['/software/tedori', '🇯🇵', '手取り計算', '給与の手取りを概算'],
        ['/software/furusato', '🎁', 'ふるさと納税', '限度額をシミュレーション'],
        ['/software/rirekisho', '📄', '履歴書メーカー', 'JIS様式・印刷対応'],
        ['/software/seikyusho', '🧾', '請求書メーカー', 'インボイス対応'],
        ['/software/kakutei', '🗂️', '確定申告チェック', '必要書類を診断'],
        ['/software/invoice', '💵', 'Invoice generator', 'Freelance invoices with tax'],
        ['/software/timezone', '🌍', 'Meeting planner', 'Find a workable hour'],
        ['/terminal', '⌨️', 'Terminal mode', 'Browse the hub like Linux']
      ]
    },
    {
      match: '/app',
      label: 'More',
      allLabel: 'Install the app',
      items: [
        ['/digi', '✦', 'Digi AI guide', 'Ask anything, in your own words'],
        ['/terminal', '⌨️', 'Terminal mode', 'Drive the hub like Linux'],
        ['/app', '📲', 'Install the app', 'Home-screen app with offline pages'],
        ['/extension', '🧩', 'Chrome extension', 'The hub in your toolbar'],
        ['/techproducts', '💻', 'Tech Products', 'Buying guides worth reading'],
        ['/subscribe', '✉️', 'Newsletter', 'One email a week, no noise'],
        ['/about', 'ℹ️', 'About the hub', 'Who builds it and why']
      ]
    },
    {
      match: '/games',
      label: 'Games',
      items: [
        ['/games', '🎮', 'Pixel Palace', 'All nine games'],
        ['/games/snake', '🐍', 'Snake', 'Classic, keyboard or swipe'],
        ['/games/2048', '🔢', '2048', 'Merge to the 2048 tile'],
        ['/games/pong', '🏓', 'Pong', 'Beat the machine'],
        ['/games/memory', '🧠', 'Memory', 'Match the pairs'],
        ['/games/mole', '🐹', 'Whack-a-mole', 'Thirty seconds of reflex'],
        ['/games/reaction', '⚡', 'Reaction test', 'Measure your reflexes'],
        ['/games/simon', '🎵', 'Simon', 'Repeat the sequence'],
        ['/games/tictactoe', '❌', 'Tic-tac-toe', 'You against the hub'],
        ['/games/typing', '⌨️', 'Typing rush', 'How fast do you type?']
      ]
    }
  ];

  function initChrome() {
    /* hub.css is injected once; pages that link it already skip this. */
    if (!document.querySelector('link[href^="/assets/hub.css"]')) {
      var link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = '/assets/hub.css?v=20261203';
      document.head.appendChild(link);
    }

    var actions = document.querySelector('.dih-actions');
    var shareBtn = document.querySelector('[data-dih-share]');
    if (actions && !actions.querySelector('.dih-term')) {
      var term = document.createElement('a');
      term.className = 'dih-icon dih-term';
      term.href = '/terminal';
      term.title = 'Terminal mode — browse like a shell';
      term.setAttribute('aria-label', 'Open terminal mode');
      term.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="3"/><path d="m7 9 3 3-3 3"/><path d="M13 15h4"/></svg>';
      if (shareBtn) actions.insertBefore(term, shareBtn); else actions.insertBefore(term, actions.firstChild);
    }
    if (actions && !actions.querySelector('[data-dih-sound]')) {
      var snd = document.createElement('button');
      snd.type = 'button';
      snd.className = 'dih-icon dih-sound';
      snd.setAttribute('data-dih-sound', '');
      snd.innerHTML = '<svg class="on" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4Z"/><path d="M16.5 8.5a5 5 0 0 1 0 7"/><path d="M19 6a8.5 8.5 0 0 1 0 12"/></svg><svg class="off" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4Z"/><path d="m16 9 5 6"/><path d="m21 9-5 6"/></svg>';
      var themeBtn = actions.querySelector('[data-dih-theme]');
      if (themeBtn) actions.insertBefore(snd, themeBtn.nextSibling); else actions.appendChild(snd);
      snd.addEventListener('click', function () { sfx.toggle(); });
    }
    syncSoundButton();
    document.querySelectorAll('[data-dih-sound]').forEach(function (b) {
      if (b.dataset.bound) return;
      b.dataset.bound = '1';
      b.addEventListener('click', function () { sfx.toggle(); });
    });

    /* Dropdown menus on the primary nav — the plain links still work. */
    var nav = document.querySelector('.dih-nav');
    if (nav) {
      MENUS.forEach(function (menu) {
        var trigger = null;
        nav.querySelectorAll('a').forEach(function (a) {
          if (!trigger && a.getAttribute('href') === menu.match) trigger = a;
        });
        if (!trigger || trigger.parentNode.classList.contains('dih-menu-wrap')) return;
        var wrap = document.createElement('div');
        wrap.className = 'dih-menu-wrap';
        trigger.parentNode.insertBefore(wrap, trigger);
        wrap.appendChild(trigger);
        trigger.classList.add('dih-menu-trigger');
        trigger.setAttribute('aria-haspopup', 'true');
        trigger.setAttribute('aria-expanded', 'false');
        var panel = document.createElement('div');
        panel.className = 'dih-menu-panel';
        panel.innerHTML = menu.items.map(function (it) {
          return '<a class="dih-menu-item" href="' + it[0] + '"><span class="dih-menu-ico" aria-hidden="true">' + it[1] +
            '</span><span><b>' + esc(it[2]) + '</b><small>' + esc(it[3]) + '</small></span></a>';
        }).join('') + '<a class="dih-menu-all" href="' + menu.match + '">' + (menu.allLabel || ('Open ' + menu.label)) + ' →</a>';
        wrap.appendChild(panel);
        var timer;
        function open() {
          clearTimeout(timer);
          wrap.classList.add('is-open');
          trigger.setAttribute('aria-expanded', 'true');
        }
        function close() {
          timer = setTimeout(function () {
            wrap.classList.remove('is-open');
            trigger.setAttribute('aria-expanded', 'false');
          }, 140);
        }
        wrap.addEventListener('mouseenter', open);
        wrap.addEventListener('mouseleave', close);
        /* Click/tap: first press opens the menu, a second press follows the link. */
        trigger.addEventListener('click', function (e) {
          if (!wrap.classList.contains('is-open')) {
            e.preventDefault();
            open();
          }
        });
        document.addEventListener('click', function (e) {
          if (!wrap.contains(e.target) && wrap.classList.contains('is-open')) {
            wrap.classList.remove('is-open');
            trigger.setAttribute('aria-expanded', 'false');
          }
        });
        trigger.addEventListener('focus', open);
        trigger.addEventListener('keydown', function (e) {
          if (e.key === 'Escape') { wrap.classList.remove('is-open'); trigger.setAttribute('aria-expanded', 'false'); }
          if (e.key === 'ArrowDown') { e.preventDefault(); open(); var first = panel.querySelector('a'); if (first) first.focus(); }
        });
        wrap.addEventListener('focusout', function (e) {
          if (!wrap.contains(e.relatedTarget)) {
            wrap.classList.remove('is-open');
            trigger.setAttribute('aria-expanded', 'false');
          }
        });
      });
    }

    /* Drawer extras. */
    var drawerSub = document.querySelector('.dih-drawer-sub');
    if (drawerSub && !drawerSub.querySelector('a[href="/terminal"]')) {
      var extra = document.createElement('a');
      extra.className = 'dih-drawer-link';
      extra.href = '/terminal';
      extra.textContent = '⌨️ Terminal mode';
      drawerSub.appendChild(extra);
      var interestLink = document.createElement('a');
      interestLink.className = 'dih-drawer-link';
      interestLink.href = '/terminal#interest';
      interestLink.textContent = '📊 Most opened pages';
      drawerSub.appendChild(interestLink);

      /* Sound is a header icon on desktop; on phones it lives here. */
      var soundLink = document.createElement('button');
      soundLink.type = 'button';
      soundLink.className = 'dih-drawer-link dih-drawer-sound';
      soundLink.textContent = soundOn ? '🔊 サウンド / Sound on' : '🔇 サウンド / Sound off';
      soundLink.addEventListener('click', function () {
        sfx.toggle();
        soundLink.textContent = soundOn ? '🔊 サウンド / Sound on' : '🔇 サウンド / Sound off';
      });
      drawerSub.appendChild(soundLink);
    }
    var drawerGrid = document.querySelector('.dih-drawer-grid');
    if (drawerGrid && !drawerGrid.querySelector('a[href="/app"]')) {
      var appLink = document.createElement('a');
      appLink.className = 'dih-drawer-link';
      appLink.href = '/app';
      appLink.textContent = '📲 Install the app';
      drawerGrid.appendChild(appLink);
      var extLink = document.createElement('a');
      extLink.className = 'dih-drawer-link';
      extLink.href = '/extension';
      extLink.textContent = '🧩 Chrome extension';
      drawerGrid.appendChild(extLink);
    }

    /* Footer link so the shell is reachable from every page. */
    var footNav = document.querySelector('.dih-footer-bottom nav');
    if (footNav && !footNav.querySelector('a[href="/terminal"]')) {
      var fa = document.createElement('a');
      fa.href = '/terminal';
      fa.textContent = 'Terminal';
      footNav.appendChild(fa);
    }
    if (footNav && !footNav.querySelector('a[href="/app"]')) {
      var fa2 = document.createElement('a');
      fa2.href = '/app';
      fa2.textContent = 'App';
      footNav.appendChild(fa2);
      var fa3 = document.createElement('a');
      fa3.href = '/extension';
      fa3.textContent = 'Extension';
      footNav.appendChild(fa3);
    }
    var footCol = document.querySelector('.dih-footer-col');
    if (footCol && !footCol.querySelector('a[href="/games/snake"]')) {
      var g = document.createElement('a');
      g.href = '/games/snake';
      g.textContent = 'Play Snake';
      footCol.appendChild(g);
    }
  }

  /* Interest: record this view once, then clicks on internal links. */
  function initInterest() {
    interest.record(location.pathname, 'view');
    document.addEventListener('click', function (e) {
      var a = e.target.closest('a[href]');
      if (!a) return;
      var href = a.getAttribute('href') || '';
      if (!href || href.charAt(0) === '#' || /^(mailto:|tel:|javascript:)/.test(href)) return;
      var url;
      try { url = new URL(a.href, location.href); } catch (err) { return; }
      if (url.origin !== location.origin) {
        interest.record(url.href, 'click');
        return;
      }
      interest.record(url.pathname, 'click');
    }, true);
  }

  /* ----------------------------------------------------------- Hub Guide */
  var RULES = [
    {
      test: /(手取り|給与|給料|社会保険|所得税|住民税|salary|take.home|paycheck)/i,
      title: '給与の手取りを計算する',
      body: '総額（額面）から社会保険料と税金を引いた金額を出します。月給・賞与・年齢・扶養人数を入れるだけです。',
      links: [['/software/tedori', '手取り計算ツール']]
    },
    {
      test: /(ふるさと納税|寄付|furusato|donation tax)/i,
      title: 'ふるさと納税の限度額',
      body: '年収と家族構成から、自己負担2,000円で収まる寄付の目安を計算します。ワンストップ特例の条件も確認できます。',
      links: [['/software/furusato', '限度額シミュレーター']]
    },
    {
      test: /(履歴書|職務経歴|転職|resume|cv|curriculum)/i,
      title: '履歴書・職務経歴書',
      body: 'JIS様式の履歴書をブラウザで作成。学歴・職歴の年表を自動で整え、志望動機のたたき台も作れます。',
      links: [['/software/rirekisho', '履歴書メーカー'], ['/software/resume', 'English résumé builder']]
    },
    {
      test: /(請求書|インボイス|見積|freelance|invoice|quote)/i,
      title: '請求書をつくる',
      body: '適格請求書（インボイス）の登録番号、消費税、源泉徴収まで入った請求書をPDF・印刷で出せます。',
      links: [['/software/seikyusho', '請求書メーカー（日本語）'], ['/software/invoice', 'Invoice generator']]
    },
    {
      test: /(確定申告|税金|経費|副業|tax return|deduction)/i,
      title: '確定申告の準備',
      body: '収入の種類を選ぶと、必要な書類・経費の考え方・期限を順番に案内します。',
      links: [['/software/kakutei', '確定申告チェックリスト']]
    },
    {
      test: /(game|ゲーム|play|遊び|break|休憩)/i,
      title: 'Five-minute break',
      body: 'Nine small games, each on its own page so you can jump straight in. Keyboard, mouse or touch.',
      links: [['/games', 'Pixel Palace'], ['/games/snake', 'Snake'], ['/games/2048', '2048']]
    },
    {
      test: /(terminal|shell|linux|コマンド|command line)/i,
      title: 'Terminal mode',
      body: 'Browse the whole hub as a Linux-like shell: ls, cd, cat, top, ask. Type help to start.',
      links: [['/terminal', 'Open the terminal']]
    },
    {
      test: /(market|株|相場|crypto|bitcoin|仮想通貨|price today)/i,
      title: 'Markets right now',
      body: 'CoinCompass shows the price, the move and the context. Delayed quotes, no advice.',
      links: [['/coincompass', 'Open CoinCompass'], ['/software/marketlens', 'MarketLens briefing']]
    },
    {
      test: /(news|ニュース|headline|today|今日)/i,
      title: 'Today’s tech news',
      body: 'Live headlines from the industry, refreshed through the day, with a guide behind each story.',
      links: [['/news', 'News desk'], ['/blog', 'Analysis blog']]
    },
    {
      test: /(learn|guide|explain|what is|とは|仕組み|初心者)/i,
      title: 'Start with a guide',
      body: 'Thirty-five guides explain the technology behind the headlines without the jargon.',
      links: [['/techtopics', 'Tech Topics'], ['/artificialintelligence', 'AI, explained']]
    },
    {
      test: /(tool|ツール|convert|calculator|計算|pdf|qr|password|json)/i,
      title: 'Free tools, no signup',
      body: 'Calculators, converters, generators and editors that run in your browser and keep your data local.',
      links: [['/software', 'Software suite'], ['/software/seo-preview', 'SEO preview'], ['/software/loan', 'Loan calculator']]
    },
    {
      test: /(travel|旅行|trip|flight|航空券|hotel)/i,
      title: 'Plan a trip',
      body: 'たび組 builds a yen budget, checks the exchange rate against 2019, and lists what to pack.',
      links: [['/software/tabikumi', 'たび組 travel planner'], ['/software/travel-planner', 'Travel planner']]
    },
    {
      test: /(share|共有|send|link)/i,
      title: 'Share this page',
      body: 'The share button in the header opens a sheet with copy, X, WhatsApp, LinkedIn, Facebook and email — on desktop too.',
      links: [['/about', 'About Digital Infohub']]
    }
  ];

  function searchCatalog(q, limit) {
    var words = String(q || '').toLowerCase().split(/\s+/).filter(Boolean);
    if (!words.length) return [];
    var rows = (catalog || []).map(function (row) {
      var hay = (row.title + ' ' + (row.desc || '') + ' ' + (row.kw || '') + ' ' + row.path).toLowerCase();
      var score = 0;
      words.forEach(function (w) {
        if (hay.indexOf(w) !== -1) score += w.length > 3 ? 3 : 2;
        if (String(row.title).toLowerCase().indexOf(w) !== -1) score += 4;
      });
      return { row: row, score: score };
    }).filter(function (r) { return r.score > 0; });
    rows.sort(function (a, b) { return b.score - a.score; });
    return rows.slice(0, limit || 4).map(function (r) { return r.row; });
  }

  function answer(q) {
    var query = String(q || '').trim();
    if (!query) {
      return { title: 'Ask the Hub Guide', body: 'Try “handover pay in Japan”, “where is the invoice maker”, “what is quantum computing” or “games”.', links: [] };
    }
    for (var i = 0; i < RULES.length; i++) {
      if (RULES[i].test.test(query)) {
        return { title: RULES[i].title, body: RULES[i].body, links: RULES[i].links };
      }
    }
    var hits = searchCatalog(query, 4);
    if (hits.length) {
      return {
        title: 'Closest pages in the hub',
        body: 'No single canned answer for that, so here is what matches best across all ' + (catalog ? catalog.length : 100) + ' pages.',
        links: hits.map(function (h) { return [h.path, h.title]; })
      };
    }
    return {
      title: 'Try the wider guide',
      body: 'The Hub Guide answers site questions from a fixed rulebook. For open questions, Digi can go further.',
      links: [['/digi?q=' + encodeURIComponent(query.slice(0, 300)), 'Ask Digi'], ['/techtopics', 'Browse Tech Topics'], ['/software', 'Browse software']]
    };
  }
  window.DIH.answer = answer;
  window.DIH.search = searchCatalog;

  /* Mounts a Hub Guide panel into any container. */
  function mountGuide(el) {
    if (!el) return;
    if (el.getAttribute('data-hub-ready') === '1') return;
    loadCatalog(function () {
      el.setAttribute('data-hub-ready', '1');
      el.classList.add('hub-ai');
      el.innerHTML =
        '<form class="hub-ai-form" role="search">' +
          '<span class="hub-ai-spark" aria-hidden="true">◆</span>' +
          '<input class="hub-ai-input" type="search" placeholder="Ask the Hub Guide — “手取り”, “invoice”, “games”…" aria-label="Ask the Hub Guide" autocomplete="off" maxlength="200">' +
          '<button class="hub-ai-btn" type="submit">Ask</button>' +
        '</form>' +
        '<p class="hub-ai-purpose">A shortcut finder: type what you need and it points at the right page. Instant and rule-based. For a conversation, ask Digi; for commands, use terminal mode.</p>' +
        '<div class="hub-ai-modes">' +
          '<button type="button" class="hub-ai-mode" data-hub-digi>✦ Ask Digi (AI)</button>' +
          '<button type="button" class="hub-ai-mode" data-hub-term>⌨ Terminal mode</button>' +
        '</div>' +
        '<div class="hub-ai-out" aria-live="polite"></div>' +
        '<div class="hub-ai-chips">' +
          ['手取り', 'ふるさと納税', 'Invoice', 'Games', 'Terminal', 'What is quantum computing?'].map(function (q) {
            return '<button type="button" data-hub-q="' + esc(q) + '">' + esc(q) + '</button>';
          }).join('') +
        '</div>';
      var form = el.querySelector('form');
      var input = el.querySelector('input');
      var out = el.querySelector('.hub-ai-out');

      function openDigi(q) {
        q = String(q || input.value || '').trim();
        if (window.Digi && typeof window.Digi.open === 'function') {
          window.Digi.open();
          if (q) {
            setTimeout(function () {
              var field = document.getElementById('digiModalInput');
              var digiForm = document.getElementById('digiModalForm');
              if (field && digiForm) {
                field.value = q.slice(0, 80);
                digiForm.dispatchEvent(new Event('submit', { cancelable: true, bubbles: true }));
              }
            }, 260);
          }
          return;
        }
        location.href = '/digi' + (q ? '?q=' + encodeURIComponent(q.slice(0, 300)) : '');
      }

      function openTerm(q) {
        q = String(q || input.value || '').trim();
        location.href = '/terminal' + (q ? '?q=' + encodeURIComponent(q.slice(0, 300)) : '');
      }

      /* One small, non-blocking card after the first question of a session:
         makes the difference between the guide, Digi and the shell explicit. */
      function showRoute(q) {
        if (el.querySelector('.hub-ai-pop')) return;
        try {
          if (sessionStorage.getItem('dih_route_seen') === '1') return;
          sessionStorage.setItem('dih_route_seen', '1');
        } catch (e) {}
        var pop = document.createElement('div');
        pop.className = 'hub-ai-pop';
        pop.setAttribute('role', 'dialog');
        pop.setAttribute('aria-label', 'Choose how to get an answer');
        pop.innerHTML =
          '<button type="button" class="hub-ai-pop-x" aria-label="Close">✕</button>' +
          '<p class="hub-ai-pop-kicker">WANT MORE THAN A LINK?</p>' +
          '<p class="hub-ai-pop-title">Digi can talk it through.</p>' +
          '<p class="hub-ai-pop-sub">The Hub Guide only matches pages. Digi is the AI guide for open questions, and terminal mode runs the same question as a shell command.</p>' +
          '<div class="hub-ai-pop-actions">' +
            '<button type="button" class="is-primary" data-pop-digi>✦ Ask Digi (AI)</button>' +
            '<button type="button" data-pop-term>⌨ Use terminal mode</button>' +
          '</div>';
        el.appendChild(pop);
        requestAnimationFrame(function () { pop.classList.add('is-in'); });
        sfx.play('open');
        function close() { pop.remove(); document.removeEventListener('keydown', onKey); }
        function onKey(e) { if (e.key === 'Escape') close(); }
        document.addEventListener('keydown', onKey);
        pop.querySelector('.hub-ai-pop-x').addEventListener('click', close);
        pop.querySelector('[data-pop-digi]').addEventListener('click', function () { close(); openDigi(q); });
        pop.querySelector('[data-pop-term]').addEventListener('click', function () { close(); openTerm(q); });
      }

      function run(q, preview) {
        var a = answer(q);
        out.innerHTML = '<div class="hub-ai-answer"><strong>' + esc(a.title) + '</strong><p>' + esc(a.body) + '</p>' +
          (a.links.length ? '<div class="hub-ai-links">' + a.links.map(function (l, i) {
            return '<a href="' + esc(l[0]) + '"' + (i === 0 ? ' class="is-primary"' : '') + '>' + esc(l[1]) + ' →</a>';
          }).join('') + '</div>' : '') + '</div>';
        if (preview) return;
        sfx.play('open');
        showRoute(q);
      }

      /* Live results: the answer card follows the query as it is typed. */
      var typeTimer = null;
      input.addEventListener('input', function () {
        clearTimeout(typeTimer);
        var q = input.value.trim();
        if (!q) { out.innerHTML = ''; return; }
        typeTimer = setTimeout(function () { run(q, true); }, 130);
      });
      input.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') { input.value = ''; out.innerHTML = ''; }
      });

      form.addEventListener('submit', function (e) { e.preventDefault(); run(input.value); });
      el.querySelectorAll('[data-hub-q]').forEach(function (b) {
        b.addEventListener('click', function () { input.value = b.getAttribute('data-hub-q'); run(input.value); });
      });
      el.querySelectorAll('[data-hub-digi]').forEach(function (b) {
        b.addEventListener('click', function () { openDigi(); });
      });
      el.querySelectorAll('[data-hub-term]').forEach(function (b) {
        b.addEventListener('click', function () { openTerm(); });
      });
    });
  }
  window.DIH.mountGuide = mountGuide;


  /* ------------------------------------------------------- AI answer typing */
  var typeReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function typeInto(el, html) {
    if (!el) return;
    el.innerHTML = html;
    if (typeReduced) return;
    var nodes = [];
    var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null);
    while (walker.nextNode()) {
      var node = walker.currentNode;
      nodes.push({ node: node, text: node.nodeValue || '' });
      node.nodeValue = '';
    }
    var total = nodes.reduce(function (n, x) { return n + x.text.length; }, 0);
    if (!total) return;
    var started = performance.now();
    var duration = Math.min(1400, 220 + total * 6);
    function frame(now) {
      var p = Math.min(1, (now - started) / duration);
      var budget = Math.floor(total * p);
      for (var i = 0; i < nodes.length && budget > 0; i++) {
        var take = Math.min(nodes[i].text.length, budget);
        nodes[i].node.nodeValue = nodes[i].text.slice(0, take);
        budget -= take;
      }
      if (p < 1) requestAnimationFrame(frame);
      else nodes.forEach(function (x) { x.node.nodeValue = x.text; });
    }
    requestAnimationFrame(frame);
  }
  function thinking(el, label) {
    if (!el) return;
    el.innerHTML = '<span class="ai-thinking"><i></i><i></i><i></i><span>' + esc(label || 'Thinking') + '</span></span>';
  }
  window.DIH.typeInto = typeInto;
  window.DIH.thinking = thinking;

  /* Keyboard: Shift+S toggles sound, Shift+T opens the terminal. */
  document.addEventListener('keydown', function (e) {
    var tag = (e.target && e.target.tagName || '').toLowerCase();
    if (tag === 'input' || tag === 'textarea' || (e.target && e.target.isContentEditable)) return;
    if (e.shiftKey && !e.ctrlKey && !e.metaKey && e.key.toLowerCase() === 's') {
      e.preventDefault();
      sfx.toggle();
    }
    if (e.shiftKey && !e.ctrlKey && !e.metaKey && e.key.toLowerCase() === 't') {
      e.preventDefault();
      location.href = '/terminal';
    }
  });

  /* Global click/hover sounds, deliberately quiet. */
  document.addEventListener('pointerdown', function (e) {
    var el = e.target.closest('button, a.dih-btn, a[href], .dih-icon');
    if (!el || el.hasAttribute('disabled')) return;
    if (el.closest('.terminal-body, .hub-ai, .dih-sheet-wrap')) return;
    sfx.play('click');
  }, { passive: true });

  /* ------------------------------------------------------------ interest UI */
  function mountInterestBoard(el, opts) {
    if (!el) return;
    opts = opts || {};
    loadCatalog(function () {
      var top = interest.top(opts.limit || 6);
      if (!top.length) {
        el.innerHTML = '<div class="interest-empty"><strong>' + esc(opts.emptyTitle || 'Nothing opened yet') + '</strong><p>' +
          esc(opts.emptyText || 'The pages you open are counted on this device, so the hub can surface what you actually use.') +
          '</p><a href="/terminal#interest">See the full interest board →</a></div>';
        return;
      }
      el.innerHTML = '<div class="interest-row">' + top.map(function (row, i) {
        return '<a class="interest-card" href="' + esc(row.path) + '">' +
          '<span class="interest-rank">' + String(i + 1).padStart(2, '0') + '</span>' +
          '<span class="interest-copy"><strong>' + esc(row.title || row.path) + '</strong>' +
          '<span>' + esc(catLabel(row.cat)) + ' · opened ' + row.views + '× · tapped ' + row.clicks + '×</span></span>' +
          '<span class="interest-arrow">→</span></a>';
      }).join('') + '</div>';
      if (opts.showNote !== false) {
        el.insertAdjacentHTML('beforeend', '<p class="interest-note">Counted privately on this device. <a href="/terminal#interest">Open the interest board</a> for every page.</p>');
      }
    });
  }
  window.DIH.mountInterest = mountInterestBoard;

  function catLabel(cat) {
    var map = {
      home: 'Home', software: 'Software', app: 'Tool', games: 'Game', game: 'Game',
      guide: 'Guide', blog: 'Blog', news: 'News', markets: 'Markets', quiz: 'Quiz',
      products: 'Products', terminal: 'Terminal', about: 'About', japanese: '日本語'
    };
    return map[cat] || 'Page';
  }

  /* ------------------------------------------------------------- bootstrap */
  /* ------------------------------------------- ocean light + interactions */
  function initLife() {
    if (typeReduced) return;

    /* A soft light that follows the pointer across hero sections. */
    if (window.matchMedia && window.matchMedia('(pointer: fine)').matches) {
      document.querySelectorAll('.hero, .promo-hero').forEach(function (sec) {
        if (sec.querySelector('.dih-pointer-glow')) return;
        var glow = document.createElement('div');
        glow.className = 'dih-pointer-glow';
        glow.setAttribute('aria-hidden', 'true');
        sec.insertBefore(glow, sec.firstChild);
        sec.addEventListener('pointermove', function (e) {
          var r = sec.getBoundingClientRect();
          glow.style.setProperty('--mx', ((e.clientX - r.left) / r.width * 100).toFixed(1) + '%');
          glow.style.setProperty('--my', ((e.clientY - r.top) / r.height * 100).toFixed(1) + '%');
          glow.classList.add('is-on');
        });
        sec.addEventListener('pointerleave', function () { glow.classList.remove('is-on'); });
      });
    }

  }

  function boot() {
    initChrome();
    initInterest();
    initLife();
    loadCatalog(function () {
      document.querySelectorAll('[data-hub-guide]').forEach(function (el) {
        if (!el.querySelector('.hub-ai-form')) mountGuide(el);
      });
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
