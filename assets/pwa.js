/* Digital Infohub PWA helpers: install prompt, home-screen guidance, offline cache. */
(function () {
  'use strict';

  var deferredPrompt = null;
  var installBtn = document.getElementById('pwaInstall');
  var hint = document.getElementById('pwaHint');
  var state = document.getElementById('pwaState');

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

  window.addEventListener('beforeinstallprompt', function (event) {
    event.preventDefault();
    deferredPrompt = event;
    refresh();
  });

  window.addEventListener('appinstalled', function () {
    deferredPrompt = null;
    refresh();
    setState('Installed — thanks!', true);
  });

  if (installBtn) {
    installBtn.addEventListener('click', function () {
      if (isStandalone()) return;
      if (deferredPrompt) {
        deferredPrompt.prompt();
        deferredPrompt.userChoice.then(function (choice) {
          if (choice.outcome === 'accepted') setState('Installing…', true);
          deferredPrompt = null;
          refresh();
        });
        return;
      }
      var section = document.getElementById('pwaHow');
      if (section) section.scrollIntoView({ behavior: 'smooth', block: 'center' });
      setHint(isIOS()
        ? 'Tap the Share button at the bottom of Safari, then scroll to “Add to Home Screen”.'
        : 'Open the browser menu (⋮ or •••) and choose “Install app” or “Add to Home screen”.');
    });
  }

  window.addEventListener('load', function () {
    if ('serviceWorker' in navigator && (location.protocol === 'https:' || location.hostname === 'localhost' || location.hostname === '127.0.0.1')) {
      navigator.serviceWorker.register('/sw.js').catch(function () { /* offline optional */ });
    }
    refresh();
  });

  // On small screens the QR is less useful than the install button; keep it visible but explain it.
  var qr = document.querySelector('.pwa-qr');
  if (qr && window.matchMedia('(max-width: 640px)').matches) {
    qr.classList.add('pwa-qr--mobile');
  }
})();
