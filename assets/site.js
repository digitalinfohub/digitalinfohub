/* Digital Infohub — shared behaviour for every page. */
(function () {
  'use strict';

  var root = document.documentElement;
  var THEME_KEY = 'dih_theme';
  var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function store(key, value) {
    try {
      if (value === undefined) return localStorage.getItem(key);
      localStorage.setItem(key, String(value));
    } catch (e) {
      return null;
    }
  }

  /* ---------------------------------------------------------------- theme */
  function applyTheme(theme) {
    root.setAttribute('data-theme', theme);
    root.setAttribute('data-dih', '');
    document.querySelectorAll('[data-dih-theme]').forEach(function (btn) {
      btn.textContent = theme === 'dark' ? '☀' : '☾';
      btn.setAttribute('aria-label', theme === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
      btn.title = btn.getAttribute('aria-label');
    });
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', theme === 'dark' ? '#07070c' : '#f6f7fb');
  }

  function initTheme() {
    var saved = store(THEME_KEY);
    applyTheme(saved === 'light' ? 'light' : 'dark');
    document.querySelectorAll('[data-dih-theme]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        store(THEME_KEY, next);
        applyTheme(next);
        haptic();
      });
    });
  }

  function haptic() {
    if (navigator.vibrate) { try { navigator.vibrate(8); } catch (e) {} }
  }

  /* --------------------------------------------------------------- drawer */
  function initDrawer() {
    var burger = document.getElementById('dihBurger');
    var drawer = document.getElementById('dihDrawer');
    if (!burger || !drawer) return;

    function setOpen(open) {
      drawer.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    }

    burger.addEventListener('click', function () { setOpen(!drawer.classList.contains('open')); haptic(); });
    drawer.addEventListener('click', function (e) {
      if (e.target === drawer || e.target.closest('[data-dih-close]')) setOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('open')) setOpen(false);
    });
    drawer.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { setOpen(false); });
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 920 && drawer.classList.contains('open')) setOpen(false);
    });
  }

  /* ---------------------------------------------------------- active link */
  function initActiveNav() {
    var path = location.pathname.replace(/\/+$/, '').replace(/\.html$/, '') || '/';
    if (path === '/index') path = '/';
    document.querySelectorAll('[data-dih-nav], #dihDrawer').forEach(function (scope) {
      scope.querySelectorAll('a[href]').forEach(function (a) {
        var href = (a.getAttribute('href') || '').split('#')[0].replace(/\/+$/, '').replace(/\.html$/, '');
        if (!href || href.charAt(0) !== '/') return;
        if (href === '/') {
          if (path === '/') a.classList.add('is-active');
        } else if (path === href || path.indexOf(href + '/') === 0) {
          a.classList.add('is-active');
        }
      });
    });
  }

  /* --------------------------------------------------------- reveal anims */
  function initReveal() {
    if (reduced || !('IntersectionObserver' in window)) return;
    var selectors = [
      'main > section', '.shell > .section', '.article > header', '.post-header',
      '.dih-explore', '.dih-footer-inner > *', '.folder-card', '.topic-card',
      '.service-card', '.product-card', '.tool-card', '.card', '.cab', '.guide-card',
      '.hero', '.home-section', '.pulse', '.section', '.dih-gallery-card'
    ];
    var nodes = [];
    selectors.forEach(function (sel) {
      try {
        document.querySelectorAll(sel).forEach(function (n) {
          if (n.closest('.dih-header, .dih-footer, .dih-drawer, .chat-container')) return;
          if (nodes.indexOf(n) === -1) nodes.push(n);
        });
      } catch (e) {}
    });
    if (!nodes.length) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add('is-in');
          io.unobserve(en.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    nodes.forEach(function (n, i) {
      if (n.classList.contains('dih-anim')) return;
      n.classList.add('dih-anim');
      n.style.setProperty('--dih-delay', Math.min(i % 4, 3) * 0.06 + 's');
      io.observe(n);
    });
  }

  /* ----------------------------------------------------- reading progress */
  function initProgress() {
    var isArticle = document.querySelector('article');
    if (!isArticle || location.pathname === '/' || /^\/($|index)/.test(location.pathname)) return;
    var bar = document.createElement('div');
    bar.className = 'dih-progress';
    bar.setAttribute('aria-hidden', 'true');
    document.body.appendChild(bar);
    var ticking = false;
    function update() {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      var pct = h > 0 ? Math.min(100, (window.scrollY / h) * 100) : 0;
      bar.style.width = pct + '%';
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  }

  /* --------------------------------------------------------- back to top */
  function initTop() {
    var btn = document.createElement('button');
    btn.className = 'dih-top';
    btn.type = 'button';
    btn.setAttribute('aria-label', 'Back to top');
    btn.innerHTML = '↑';
    document.body.appendChild(btn);
    btn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reduced ? 'auto' : 'smooth' });
    });
    var show = function () { btn.classList.toggle('show', window.scrollY > 700); };
    window.addEventListener('scroll', show, { passive: true });
    show();
  }

  /* --------------------------------------------------------------- toast */
  function toast(message) {
    var el = document.getElementById('dihToast');
    if (!el) {
      el = document.createElement('div');
      el.id = 'dihToast';
      el.setAttribute('role', 'status');
      document.body.appendChild(el);
    }
    el.textContent = message;
    el.classList.add('show');
    clearTimeout(el._timer);
    el._timer = setTimeout(function () { el.classList.remove('show'); }, 3600);
  }
  window.dihToast = toast;

  /* ------------------------------------------- install / bookmark prompt */
  function initInstall() {
    var KEY = 'dih_install_prompt';
    var homePath = location.pathname === '/' || /\/index\.html$/.test(location.pathname);
    if (!homePath) return;
    if (window.matchMedia && window.matchMedia('(display-mode: standalone)').matches) return;
    if (window.navigator.standalone) return;

    var last = parseInt(store(KEY) || '0', 10);
    if (last && Date.now() - last < 1000 * 60 * 60 * 24 * 14) return;

    var isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent);
    var isMobile = /Android|iPhone|iPad|iPod|Mobile/i.test(navigator.userAgent);

    var card = document.createElement('div');
    card.className = 'dih-install';
    card.setAttribute('role', 'dialog');
    card.setAttribute('aria-label', 'Save Digital Infohub');
    card.innerHTML =
      '<img src="/assets/logo.png" alt="Digital Infohub" width="44" height="44">' +
      '<div class="dih-install-body">' +
        '<strong>' + (isMobile ? 'Add Digital Infohub to your home screen' : 'Keep Digital Infohub one click away') + '</strong>' +
        '<p>' + (isIOS
          ? 'Tap the Share button, then <b>Add to Home Screen</b> for instant access to daily tech intel.'
          : isMobile
            ? 'Open your browser menu and choose <b>Add to Home screen</b> to get the daily briefing in one tap.'
            : 'Press <kbd>Ctrl</kbd> + <kbd>D</kbd> (<kbd>⌘</kbd> + <kbd>D</kbd> on Mac) to bookmark the hub.') +
        '</p>' +
        '<div class="dih-install-actions">' +
          '<button type="button" class="dih-install-btn" data-install-ok>Got it</button>' +
          '<button type="button" class="dih-install-btn ghost" data-install-later>Later</button>' +
        '</div>' +
      '</div>' +
      '<button type="button" class="dih-install-close" aria-label="Close">✕</button>';
    document.body.appendChild(card);

    var shown = false;
    function show() {
      if (shown || document.body.classList.contains('digi-on')) return;
      shown = true;
      card.classList.add('show');
      setTimeout(function () { hide(KEY); }, 22000);
    }
    function hide(key) {
      card.classList.remove('show');
      store(key || KEY, Date.now());
      setTimeout(function () { card.remove(); }, 400);
    }
    card.querySelector('[data-install-ok]').addEventListener('click', function () { hide(); });
    card.querySelector('[data-install-later]').addEventListener('click', function () {
      store(KEY, 0);
      card.classList.remove('show');
      setTimeout(function () { card.remove(); }, 400);
    });
    card.querySelector('.dih-install-close').addEventListener('click', function () { hide(); });

    var timer = setTimeout(show, 14000);
    window.addEventListener('scroll', function () {
      if (!shown && window.scrollY > 900) { clearTimeout(timer); show(); }
    }, { passive: true });
  }

  /* ------------------------------------------------------- what's new popup */
  function initPulse() {
    var KEY = 'dih_pulse_seen';
    if (/^\/(privacy-policy|subscribe)/.test(location.pathname)) return;
    var onboarding = document.getElementById('onboarding');
    if (onboarding && !onboarding.classList.contains('hidden')) return;
    var last = parseInt(store(KEY) || '0', 10);
    if (last && Date.now() - last < 1000 * 60 * 60 * 24 * 3) return;

    var items = [
      {
        img: 'https://images.unsplash.com/photo-1677442135703-1787eea5ce01?w=140&h=140&fit=crop&auto=format&q=70',
        kicker: 'AI · 4 min read',
        title: 'Inside the AI brain',
        text: 'What large models actually learn, and where a human still has to check the work.',
        href: '/artificialintelligence',
        cta: 'Read the AI guide'
      },
      {
        img: 'https://images.unsplash.com/photo-1590859808308-3d2d9c515b1a?w=140&h=140&fit=crop&auto=format&q=70',
        kicker: 'Markets · live dashboard',
        title: 'Crypto and stock graphs, without the noise',
        text: 'CoinCompass now plots the trend beside the price, so context comes first.',
        href: '/coincompass',
        cta: 'Open CoinCompass'
      },
      {
        img: 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=140&h=140&fit=crop&auto=format&q=70',
        kicker: 'Security · 5 min read',
        title: 'Security is an identity problem',
        text: 'Most breaches start with a stolen session, not a broken firewall.',
        href: '/cybersecurity',
        cta: 'Read the security guide'
      },
      {
        img: 'https://images.unsplash.com/photo-1644088379091-d574269d422f?w=140&h=140&fit=crop&auto=format&q=70',
        kicker: 'Tech trends · analysis',
        title: 'The stories shaping tech right now',
        text: 'AI capex, on-device inference and the security spending shift, in one briefing.',
        href: '/blog',
        cta: 'Open today\'s briefing'
      }
    ];
    var item = items[Math.floor(Math.random() * items.length)];
    var el = document.createElement('aside');
    el.className = 'dih-pulse';
    el.setAttribute('aria-label', 'What is new at Digital Infohub');
    el.innerHTML =
      '<img src="' + item.img + '" alt="" width="62" height="62" loading="lazy">' +
      '<div class="dih-pulse-body">' +
        '<span class="dih-pulse-kicker">' + item.kicker + '</span>' +
        '<strong class="dih-pulse-title">' + item.title + '</strong>' +
        '<span class="dih-pulse-text">' + item.text + '</span>' +
        '<a class="dih-pulse-link" href="' + item.href + '">' + item.cta + ' →</a>' +
      '</div>' +
      '<button type="button" class="dih-pulse-close" aria-label="Close what is new">✕</button>';
    document.body.appendChild(el);

    var dismissed = false;
    function show() {
      if (dismissed || document.body.classList.contains('digi-on') || el.classList.contains('show')) return;
      el.classList.add('show');
    }
    function close() {
      if (dismissed) return;
      dismissed = true;
      el.classList.remove('show');
      store(KEY, Date.now());
      setTimeout(function () { el.remove(); }, 450);
    }
    el.querySelector('.dih-pulse-close').addEventListener('click', close);
    el.querySelector('.dih-pulse-link').addEventListener('click', function () { store(KEY, Date.now()); });

    var timer = setTimeout(show, 32000);
    window.addEventListener('scroll', function () {
      if (window.scrollY > 1400) { clearTimeout(timer); show(); }
    }, { passive: true });
  }

  /* ------------------------------------------------------- Ask Digi launcher */
  function initAskDigi() {
    var path = location.pathname.replace(/\/+$/, '').replace(/\.html$/, '') || '/';
    if (path === '/index') path = '/';
    /* /digi is the full experience; it does not need a second way in. */
    if (path === '/digi' || window.__dihAskLoaded) return;
    window.__dihAskLoaded = true;

    var launch = document.createElement('div');
    launch.className = 'dih-ask-launch';
    launch.innerHTML =
      '<button type="button" class="dih-ask-pill" id="dihAskOpen" aria-haspopup="dialog" aria-controls="dihAskOverlay">' +
        '<span class="dih-ask-spark" aria-hidden="true">✨</span>' +
        '<span class="dih-ask-label">Ask Digi <b>anything</b></span>' +
        '<span class="dih-ask-key" aria-hidden="true">Ask</span>' +
      '</button>';
    document.body.appendChild(launch);

    var overlay = document.createElement('div');
    overlay.className = 'dih-ask-overlay';
    overlay.id = 'dihAskOverlay';
    overlay.setAttribute('aria-hidden', 'true');
    overlay.innerHTML =
      '<div class="dih-ask-modal" role="dialog" aria-modal="true" aria-labelledby="dihAskTitle">' +
        '<button type="button" class="dih-ask-close" id="dihAskClose" aria-label="Close Ask Digi">✕</button>' +
        '<div class="dih-ask-art" aria-hidden="true">' +
          '<img src="/assets/digi.png" alt="" width="92" height="112" decoding="async">' +
        '</div>' +
        '<span class="dih-ask-kicker"><span class="dih-ask-pip"></span> DIGI · AI GUIDE</span>' +
        '<h2 id="dihAskTitle">Ask Digi <span>anything.</span></h2>' +
        '<p class="dih-ask-sub">Tech news, markets, development, design, everyday questions — <b>and so much more.</b> Digi answers clearly, then shows you the best of Digital Infohub.</p>' +
        '<form class="dih-ask-form" action="/digi" method="get" id="dihAskForm" role="search">' +
          '<input class="dih-ask-input" id="dihAskInput" name="q" type="search" placeholder="e.g. Explain AI agents, or how are the markets doing?" aria-label="Ask Digi a question" autocomplete="off" maxlength="500">' +
          '<button class="dih-ask-submit" type="submit">Ask <span aria-hidden="true">→</span></button>' +
        '</form>' +
        '<div class="dih-ask-chips">' +
          '<button type="button" data-ask-q="What&#39;s happening in tech today?">📰 Tech news</button>' +
          '<button type="button" data-ask-q="How are the markets doing right now?">📈 Markets</button>' +
          '<button type="button" data-ask-q="Explain quantum computing simply">⚛️ Explain quantum</button>' +
          '<button type="button" data-ask-q="Help me choose a laptop for work and study">💻 Pick a laptop</button>' +
        '</div>' +
        '<p class="dih-ask-note">Free · no signup · live AI with a built-in backup</p>' +
      '</div>';
    document.body.appendChild(overlay);

    var btn = document.getElementById('dihAskOpen');
    var closeBtn = document.getElementById('dihAskClose');
    var form = document.getElementById('dihAskForm');
    var input = document.getElementById('dihAskInput');
    var open = false;

    function go(q) {
      q = String(q || '').replace(/\s+/g, ' ').trim();
      location.href = q ? '/digi?q=' + encodeURIComponent(q.slice(0, 500)) : '/digi';
    }

    function openOverlay() {
      open = true;
      overlay.classList.add('is-open');
      overlay.setAttribute('aria-hidden', 'false');
      document.body.classList.add('dih-ask-open');
      setTimeout(function () { if (input) input.focus({ preventScroll: true }); }, 80);
    }
    function closeOverlay() {
      open = false;
      overlay.classList.remove('is-open');
      overlay.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('dih-ask-open');
      if (btn) btn.focus({ preventScroll: true });
    }
    function checkVisibility() {
      if (!btn) return;
      var doc = document.documentElement;
      var isHome = location.pathname === '/' || /\/index\.html$/.test(location.pathname);
      /* The homepage already has the big hero composer at the top, so its
         floating pill only returns near the bottom of the page. */
      var nearTop = !isHome && window.scrollY < 230;
      var nearBottom = window.scrollY + window.innerHeight > doc.scrollHeight - 900;
      launch.classList.toggle('is-on', !open && (nearTop || nearBottom));
    }

    if (btn) btn.addEventListener('click', openOverlay);
    if (closeBtn) closeBtn.addEventListener('click', closeOverlay);
    overlay.addEventListener('click', function (e) { if (e.target === overlay) closeOverlay(); });
    if (form) form.addEventListener('submit', function (e) {
      e.preventDefault();
      go(input.value);
    });

    document.querySelectorAll('[data-ask-q]').forEach(function (chip) {
      chip.addEventListener('click', function () { go(chip.getAttribute('data-ask-q')); });
    });

    /* The homepage (and any future page) can hand a query straight to Digi. */
    document.querySelectorAll('form[data-ask-digi]').forEach(function (pageForm) {
      pageForm.addEventListener('submit', function (e) {
        e.preventDefault();
        var field = pageForm.querySelector('input[name="q"]');
        go(field ? field.value : '');
      });
    });

    document.addEventListener('keydown', function (e) {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        if (open) closeOverlay(); else openOverlay();
      }
      if (e.key === 'Escape' && open) closeOverlay();
    });

    var ticking = false;
    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () { checkVisibility(); ticking = false; });
    }, { passive: true });
    window.addEventListener('resize', checkVisibility);
    checkVisibility();
  }

  /* --------------------------------------------------- daily visit streak */
  function initStreak() {
    var key = 'dih_streak';
    var today = new Date().toDateString();
    var raw = null;
    try { raw = JSON.parse(store(key) || 'null'); } catch (e) {}
    if (!raw || raw.day !== today) {
      var yesterday = new Date(Date.now() - 86400000).toDateString();
      var count = raw && raw.day === yesterday ? (raw.count || 1) + 1 : 1;
      store(key, JSON.stringify({ day: today, count: count }));
      if (count >= 3) {
        setTimeout(function () { toast('🔥 ' + count + '-day streak — welcome back to the hub.'); }, 4800);
      }
    }
  }


  /* Fall back to a local brand image if a thumbnail ever 404s. */
  document.addEventListener('error', function (e) {
    var el = e.target;
    if (el && el.tagName === 'IMG' && !el.dataset.dihFallback && /\/(assets\/blog|images\.unsplash|static\.wixstatic)/.test(el.src || '')) {
      el.dataset.dihFallback = '1';
      el.src = '/assets/blog/fallback.jpg';
    }
  }, true);

  /* ------------------------------------------------------------- bootstrap */
  initTheme();
  initDrawer();
  initActiveNav();
  initReveal();
  initProgress();
  initTop();
  initInstall();
  initStreak();
  initAskDigi();
  initPulse();

  /* Keep the page in sync with a theme change made by legacy page scripts. */
  document.querySelectorAll('[data-dih-theme]').forEach(function () {});
})();

/* Digi is deliberately separate from the legacy chrome script. */
(function () {
  if (window.__dihDigiLoaded) return;
  var script = document.createElement('script');
  script.src = '/assets/digi.js';
  script.defer = true;
  document.head.appendChild(script);
})();
