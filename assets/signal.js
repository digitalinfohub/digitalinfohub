/* Digital Infohub — "Did you know" signal card.
 *
 * A once-per-visit editorial card that carries a normal in-page ad unit. It is
 * deliberately NOT a popup/overlay: Google's AdSense placement policy forbids
 * ad code in pop-ups ("AdSense code may not be placed in inappropriate places
 * such as pop-ups") and asks that ads never be obscured, so this card sits in
 * the normal document flow, above a standard responsive unit, and the unit
 * stays visible whether or not the editorial text is shown.
 *
 *   window.DIH_SIGNAL_TTL_MINUTES = 60;        // optional override
 *   /assets/signal.json = { ttlMinutes, items: [...] }
 *
 * The content file can be edited without touching code.
 */
(function () {
  'use strict';

  var DEFAULTS = {
    ttlMinutes: 60,
    items: [
      {
        eyebrow: 'Did you know',
        title: 'Five music tools run in this tab',
        body: 'Draw a spectrogram and export a WAV, write a piano roll and export real MIDI, or program a beat on the drum machine — no plugins, no account.',
        href: '/software#studio',
        cta: 'Open the Creative Studio'
      },
      {
        eyebrow: 'Did you know',
        title: 'There is a terminal mode',
        body: 'Press the terminal icon in the header — or visit /terminal — and browse the whole site like a shell. Type "help" to see every command.',
        href: '/terminal',
        cta: 'Try terminal mode'
      },
      {
        eyebrow: 'Did you know',
        title: 'Every tool works offline',
        body: 'The calculators, converters, editors and games run entirely in your browser. Nothing is uploaded, and most pages keep working with the network off.',
        href: '/software',
        cta: 'Browse 50+ tools'
      },
      {
        eyebrow: 'Did you know',
        title: 'Twelve games, zero installs',
        body: 'Snake, 2048, Pong, Block Defender, Neon Horizon and more — each one saves your best score in this browser only.',
        href: '/games',
        cta: 'Enter the arcade'
      },
      {
        eyebrow: 'Did you know',
        title: 'Markets in one screen',
        body: 'Coin Compass tracks crypto and market moves with plain-language context, so a red day is easier to read.',
        href: '/coincompass',
        cta: 'Open Coin Compass'
      },
      {
        eyebrow: 'Did you know',
        title: 'Measure your typing speed',
        body: 'The typing test scores words per minute and accuracy on real paragraphs, then shows which keys slow you down.',
        href: '/software/typing-test',
        cta: 'Take the test'
      }
    ]
  };

  var path = location.pathname.replace(/\.html$/, '');
  if (/^\/(games|terminal|digi|digi\.html)/.test(path)) return;

  function readState() {
    try {
      return JSON.parse(localStorage.getItem('dih:signal') || '{}');
    } catch (e) {
      return {};
    }
  }

  function writeState(v) {
    try { localStorage.setItem('dih:signal', JSON.stringify(v)); } catch (e) {}
  }

  function pick(items, ttl) {
    var seed = Math.floor(Date.now() / (ttl * 60000));
    return items[seed % items.length];
  }

  function card(item) {
    var el = document.createElement('section');
    el.className = 'dih-signal';
    el.setAttribute('aria-labelledby', 'dihSignalTitle');
    el.innerHTML =
      '<div class="dih-signal-copy">' +
        '<span class="dih-signal-eyebrow">' + item.eyebrow + '</span>' +
        '<h2 id="dihSignalTitle">' + item.title + '</h2>' +
        '<p>' + item.body + '</p>' +
        '<a class="dih-signal-cta" href="' + item.href + '">' + item.cta + ' <span aria-hidden="true">&rarr;</span></a>' +
      '</div>' +
      '<button class="dih-signal-close" type="button" aria-label="Hide this note">&times;</button>';
    el.querySelector('.dih-signal-close').addEventListener('click', function () {
      var copy = el.querySelector('.dih-signal-copy');
      if (copy) copy.remove();
      var btn = el.querySelector('.dih-signal-close');
      if (btn) btn.remove();
      el.classList.add('is-quiet');
    });
    return el;
  }

  function run(cfg) {
    var ttl = Number(window.DIH_SIGNAL_TTL_MINUTES || cfg.ttlMinutes || 60);
    var state = readState();
    var due = !state.at || (Date.now() - state.at) > ttl * 60000;
    if (!due) return;

    /* The unit that sits lowest on the page becomes the signal's ad, so the
       card never adds a unit and the page keeps exactly the same ad load. */
    var slots = Array.prototype.slice.call(document.querySelectorAll('[data-dih-ad]'));
    var ad = slots.length ? slots[slots.length - 1] : null;
    var section = card(pick(cfg.items && cfg.items.length ? cfg.items : DEFAULTS.items, ttl));

    if (ad && ad.parentNode) {
      ad.parentNode.insertBefore(section, ad);
      var adLabel = ad.querySelector('span');
      if (adLabel) adLabel.textContent = 'Advertisement';
      section.appendChild(ad);
      section.classList.add('has-ad');
    } else {
      var anchor = document.querySelector('.dih-explore, .dih-gallery, footer');
      if (!anchor || !anchor.parentNode) return;
      anchor.parentNode.insertBefore(section, anchor);
    }

    writeState({ at: Date.now() });

    try {
      var payload = { event: 'signal_shown', item: section.querySelector('h2') ? section.querySelector('h2').textContent : '' };
      if (window.dispatchEvent) window.dispatchEvent(new CustomEvent('dih:signal', { detail: payload }));
    } catch (e) {}
  }

  function boot() {
    if (window.fetch) {
      fetch('/assets/signal.json', { cache: 'no-cache' })
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (cfg) { run(cfg || DEFAULTS); })
        .catch(function () { run(DEFAULTS); });
    } else {
      run(DEFAULTS);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
