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
      '.hero', '.home-section', '.pulse', '.section'
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
      if (shown) return;
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

  /* Keep the page in sync with a theme change made by legacy page scripts. */
  document.querySelectorAll('[data-dih-theme]').forEach(function () {});
})();
