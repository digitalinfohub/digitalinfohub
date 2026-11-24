/* Digital Infohub PWA helpers: install prompt, install dialog, offline cache. */
(function () {
  'use strict';
  if (window.__dihPwaLoaded) return;
  window.__dihPwaLoaded = true;

  var deferredPrompt = null;
  var installBtn = document.getElementById('pwaInstall');
  var hint = document.getElementById('pwaHint');
  var state = document.getElementById('pwaState');
  var modal = null;
  var lastFocus = null;

  function isStandalone() {
    return (window.matchMedia && window.matchMedia('(display-mode: standalone)').matches) ||
      window.navigator.standalone === true;
  }

  function isIOS() {
    return /iphone|ipad|ipod/i.test(navigator.userAgent) ||
      (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  }

  function setHint(text) { if (hint) hint.textContent = text; }
  function setState(text, ok) {
    if (!state) return;
    state.textContent = text;
    state.classList.toggle('ok', !!ok);
  }

  function refresh() {
    if (!installBtn) return;
    if (isStandalone()) {
      installBtn.textContent = '✓ Already installed';
      installBtn.disabled = true;
      setState('Installed — opens like a native app', true);
      setHint('Find Digital Infohub on your home screen or app library.');
      return;
    }
    if (deferredPrompt) {
      installBtn.textContent = 'Install the app';
      installBtn.disabled = false;
      setState('Ready to install', true);
      setHint('Tap install — or use your browser menu → “Install app”.');
      return;
    }
    installBtn.textContent = isIOS() ? 'Add to Home Screen' : 'How to install';
    installBtn.disabled = false;
    setState('Works like a native app', false);
    setHint(isIOS()
      ? 'On iPhone or iPad: tap Share, then “Add to Home Screen”.'
      : 'Open your browser menu and choose “Install app” or “Add to Home screen”.');
  }

  /* ---------------------------------------------------------- install modal */
  function buildModal() {
    if (modal) return modal;
    modal = document.createElement('div');
    modal.className = 'pwa-modal';
    modal.id = 'pwaModal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-labelledby', 'pwaModalTitle');
    modal.innerHTML =
      '<div class="pwa-card">' +
        '<div class="pwa-card-head">' +
          '<div>' +
            '<p class="pwa-card-kicker">Install · free</p>' +
            '<h2 id="pwaModalTitle">Digital Infohub, one tap away</h2>' +
            '<p>Add the hub to your home screen or dock. It opens full screen, keeps working offline and updates itself — no app store, no account.</p>' +
          '</div>' +
          '<button type="button" class="pwa-card-x" aria-label="Close install instructions">✕</button>' +
        '</div>' +
        '<div class="pwa-card-body">' +
          '<div class="pwa-card-qr">' +
            '<img src="/assets/pwa-qr.png" alt="QR code for digitalinfohub.net" width="240" height="240" loading="lazy">' +
            '<small>Scan to open on your phone</small>' +
          '</div>' +
          '<ol>' +
            '<li><b>iPhone or iPad:</b> open in Safari, tap Share, then “Add to Home Screen”.</li>' +
            '<li><b>Android:</b> open in Chrome, tap ⋮, then “Install app” or “Add to Home screen”.</li>' +
            '<li><b>Desktop Chrome or Edge:</b> click the install icon in the address bar, or menu → “Install Digital Infohub”.</li>' +
          '</ol>' +
        '</div>' +
        '<div class="pwa-card-actions">' +
          '<button type="button" class="dih-btn dih-btn-primary" data-pwa-native hidden>Install now</button>' +
          '<a class="dih-btn dih-btn-ghost" href="/app">Open the install page →</a>' +
          '<a class="dih-btn dih-btn-ghost" href="https://chromewebstore.google.com/detail/digital-infohub/epfalnobaadpaainlepefgikngafhbhl" target="_blank" rel="noopener">Chrome extension</a>' +
        '</div>' +
        '<p class="pwa-card-note">Already installed? Open it from your home screen or app list. The site keeps working in any browser too.</p>' +
      '</div>';
    document.body.appendChild(modal);

    modal.querySelector('.pwa-card-x').addEventListener('click', closeModal);
    modal.querySelector('[data-pwa-native]').addEventListener('click', function () {
      closeModal();
      promptInstall();
    });
    modal.addEventListener('click', function (e) {
      if (e.target === modal) closeModal();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modal.classList.contains('is-open')) closeModal();
    });
    return modal;
  }

  function openModal() {
    buildModal();
    lastFocus = document.activeElement;
    var native = modal.querySelector('[data-pwa-native]');
    if (native) native.hidden = !deferredPrompt;
    document.body.classList.add('pwa-modal-open');
    requestAnimationFrame(function () { modal.classList.add('is-open'); });
    var close = modal.querySelector('.pwa-card-x');
    if (close) setTimeout(function () { close.focus(); }, 60);
  }

  function closeModal() {
    if (!modal) return;
    modal.classList.remove('is-open');
    document.body.classList.remove('pwa-modal-open');
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  function promptInstall() {
    if (isStandalone()) return false;
    if (deferredPrompt) {
      deferredPrompt.prompt();
      deferredPrompt.userChoice.then(function (choice) {
        if (choice.outcome === 'accepted') setState('Installing…', true);
        deferredPrompt = null;
        refresh();
      });
      return true;
    }
    return false;
  }

  window.addEventListener('beforeinstallprompt', function (event) {
    event.preventDefault();
    deferredPrompt = event;
    refresh();
  });

  window.addEventListener('appinstalled', function () {
    deferredPrompt = null;
    refresh();
    setState('Installed — thanks!', true);
    closeModal();
  });

  if (installBtn) {
    installBtn.addEventListener('click', function () {
      if (isStandalone()) return;
      /* Always show the QR + instructions first; the dialog offers the
         native one-click prompt when the browser has one ready. */
      openModal();
    });
  }

  /* Explicit install buttons show the QR + instructions first; the dialog
     offers the native prompt when the browser has one ready. */
  document.querySelectorAll('[data-pwa-open]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      openModal();
    });
  });

  window.DIHInstall = {
    open: openModal,
    close: closeModal,
    prompt: promptInstall,
    installed: isStandalone
  };

  window.addEventListener('load', function () {
    if ('serviceWorker' in navigator && (location.protocol === 'https:' || location.hostname === 'localhost' || location.hostname === '127.0.0.1')) {
      navigator.serviceWorker.register('/sw.js').catch(function () { /* offline optional */ });
    }
    refresh();
  });

  var qr = document.querySelector('.pwa-qr');
  if (qr && window.matchMedia('(max-width: 640px)').matches) {
    qr.classList.add('pwa-qr--mobile');
  }
})();
