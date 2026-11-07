/* Digital Infohub — Digi, the rule-based site companion. */
(function () {
  'use strict';

  if (window.__dihDigiLoaded) return;
  window.__dihDigiLoaded = true;

  var ARTIFY = 'https://artifys.wixsite.com/artifyspace';
  var SNOOZE_KEY = 'dih_digi_snooze_until';
  var SOUND_KEY = 'dih_digi_sound';
  var CENTER_KEY = 'dih_digi_center_seen';
  var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var path = (location.pathname || '/').replace(/\/+$/, '').replace(/\.html$/, '') || '/';
  if (path === '/index') path = '/';
  /* /digi is the full Digi experience — no corner companion needed there. */
  if (path === '/digi') return;

  function read(key) {
    try { return window.localStorage.getItem(key); } catch (e) { return null; }
  }
  function write(key, value) {
    try { window.localStorage.setItem(key, String(value)); } catch (e) {}
  }
  function remove(key) {
    try { window.localStorage.removeItem(key); } catch (e) {}
  }
  function notify(message) {
    if (window.dihToast) window.dihToast(message);
  }
  function clip(text, max) {
    text = String(text || '').replace(/\s+/g, ' ').trim();
    return text.length > max ? text.slice(0, max - 1).replace(/\s+\S*$/, '') + '…' : text;
  }

  function A(label, href) { return { label: label, href: href }; }
  function P(label, prompt) { return { label: label, prompt: prompt }; }

  function pageHeading() {
    var el = document.querySelector('main h1, article h1, .hero h1, h1');
    var text = el ? el.textContent : document.title.split('|')[0];
    return clip(text, 72);
  }

  function pageContext() {
    var heading = pageHeading();
    var base = [
      A('Browse 30 guides', '/techtopics'),
      A('Try a quiz', '/quiz'),
      A('Live tech news', '/news')
    ];

    if (path === '/') {
      return {
        intro: "Hi, I'm Digi — your guide to Digital Infohub. I can explain a tech topic, find a guide, check the headlines or take you to the markets. There's something here whether you're curious or a pro.",
        fact: 'Did you know? Digital Infohub has 30 guides, 12 free tools, six graded quizzes and a live TechCrunch desk — all without a paywall.',
        actions: [A('Open full Digi chat', '/digi'), A('Find a guide', '/techtopics'), A('Live tech news', '/news')]
      };
    }
    if (path === '/news') {
      return {
        intro: "You're on the live desk. I can take you to the guide behind a headline, or test you on the basics.",
        fact: 'Did you know? The news desk is cached for a few minutes, so it stays quick while staying fresh.',
        actions: [A('Browse guides', '/techtopics'), A('Try a quiz', '/quiz'), A('Open the blog', '/blog')]
      };
    }
    if (path === '/quiz') {
      return {
        intro: "You're on the quiz page. Six topics, five questions each — pick one and I'll keep your best grade.",
        fact: 'Did you know? Each quiz has five questions and keeps your best grade for that topic on this device.',
        actions: [A('Browse guides', '/techtopics'), A('Live tech news', '/news'), A('Open the arcade', '/games')]
      };
    }
    if (path === '/techtopics') {
      return {
        intro: 'This is the guide index: 30 plain-language explainers, from AI and cybersecurity to space technology and smart cities.',
        fact: 'Did you know? Every guide gives you the mental model, the limits and a practical next step.',
        actions: [A('Take the quiz', '/quiz'), A('Live tech news', '/news'), A('Open the blog', '/blog')]
      };
    }
    if (path === '/software') {
      return {
        intro: 'This is the toolbox: 12 free browser tools, including AI chat, JSON, passwords, markdown and market data.',
        fact: 'Did you know? All 12 tools run in your browser — no signup, no paywall.',
        actions: [A('Open InfohubGPT', '/software/infohubgpt'), A('All 12 tools', '/software'), A('Try a quiz', '/quiz')]
      };
    }
    if (path.indexOf('/software/') === 0) {
      return {
        intro: "You're in a free AI tool. I can point you to the AI guide, the quiz or the rest of the toolbox.",
        fact: 'Did you know? The AI chat is one of 12 free browser tools on the site.',
        actions: [A('AI guide', '/artificialintelligence'), A('All tools', '/software'), A('Try the AI quiz', '/quiz')]
      };
    }
    if (path === '/games') {
      return {
        intro: "You're in the arcade. Eight browser games, no download, no signup.",
        fact: 'Did you know? The arcade has eight browser games and works on a phone.',
        actions: [A('Open the arcade', '/games'), A('Take a quiz', '/quiz'), A('Live tech news', '/news')]
      };
    }
    if (path === '/coincompass' || path.indexOf('marketlens') !== -1) {
      return {
        intro: "You're in CoinCompass. I can point you to the live news desk, the blog or the guides behind the numbers.",
        fact: 'Did you know? CoinCompass puts the trend beside the price so context comes first.',
        actions: [A('Open CoinCompass', '/coincompass'), A('Live tech news', '/news'), A('Read the blog', '/blog')]
      };
    }
    if (path === '/blog' || path.indexOf('/post/') === 0) {
      return {
        intro: "You're in the briefing. Want the fast version? The guide index is the five-minute path.",
        fact: 'Did you know? The briefing is the long-form version; the guide index is the five-minute version.',
        actions: [A('Browse guides', '/techtopics'), A('Live tech news', '/news'), A('Try a quiz', '/quiz')]
      };
    }
    if (path === '/techproducts') {
      return {
        intro: "You're in the tech products section. I can take you to the buying guides or the topics behind the specs.",
        fact: 'Did you know? The buying guides sit beside the technical explainers, so you can compare the spec with the trade-off.',
        actions: [A('Browse guides', '/techtopics'), A('Open the toolbox', '/software'), A('Live tech news', '/news')]
      };
    }
    if (heading && path !== '/') {
      return {
        intro: "You're on the " + heading + " page. I can take you to the quiz, the full guide index or today's tech news.",
        fact: 'Did you know? Every guide is built to give you a mental model, the limits and a practical next step.',
        actions: [A('Take a quiz', '/quiz'), A('Browse all 30 guides', '/techtopics'), A('Live tech news', '/news')]
      };
    }
    return {
      intro: "I'm Digi, your guide to Digital Infohub. I know the 30 guides, the quiz, the live news desk, the toolbox and the arcade.",
      fact: "Did you know? The fastest path is usually one of the 30 guides, the live news desk or a five-question quiz.",
      actions: base
    };
  }

  var RULES = [
    {
      keys: ['ai', 'artificial intelligence', 'machine learning', 'ml', 'llm', 'model', 'neural', 'deep learning'],
      text: 'AI is one of the 30 guides. Start with the plain-language explainer, then test yourself with the AI quiz.',
      actions: [A('Read the AI guide', '/artificialintelligence'), A('Machine learning guide', '/machinelearning'), A('Try the AI quiz', '/quiz')]
    },
    {
      keys: ['security', 'cyber', 'cybersecurity', 'phishing', 'password', 'breach', 'zero trust'],
      text: 'The security guide covers identity, phishing and a pragmatic stack. The quiz also has a security round.',
      actions: [A('Read the security guide', '/cybersecurity'), A('Zero trust guide', '/zerotrustsecurity'), A('Security quiz', '/quiz')]
    },
    {
      keys: ['cloud', 'aws', 'azure', 'server', 'infrastructure'],
      text: 'The cloud guide explains regions, latency and data sovereignty without the vendor pitch.',
      actions: [A('Read the cloud guide', '/cloudcomputing'), A('Edge computing', '/edgecomputing'), A('Browse guides', '/techtopics')]
    },
    {
      keys: ['quantum', 'qubit', 'post-quantum'],
      text: 'Quantum is explained in plain language: what it speeds up, why error correction is hard and what to plan for.',
      actions: [A('Read the quantum guide', '/quantumcomputing'), A('Browse guides', '/techtopics'), A('Try a quiz', '/quiz')]
    },
    {
      keys: ['chip', 'chips', 'semiconductor', 'semiconductors', 'silicon', 'fab'],
      text: 'The semiconductor guide follows the silicon bottleneck from design to fabrication — and why it matters for products.',
      actions: [A('Semiconductor guide', '/semiconductors'), A('Tech buying guides', '/techproducts'), A('Browse guides', '/techtopics')]
    },
    {
      keys: ['robot', 'robots', 'robotics', 'automation'],
      text: 'Robotics is about sensing, actuation and the boring reliability work in between. Start with the guide.',
      actions: [A('Read the robotics guide', '/robotics'), A('AI guide', '/artificialintelligence'), A('Browse guides', '/techtopics')]
    },
    {
      keys: ['drone', 'drones', 'uav'],
      text: 'The drone guide covers the hardware, the regulation and the useful work beyond the hype.',
      actions: [A('Read the drone guide', '/drones'), A('Robotics guide', '/robotics'), A('Browse guides', '/techtopics')]
    },
    {
      keys: ['blockchain', 'smart contract', 'ledger', 'web3'],
      text: 'The blockchain guide separates shared ledgers and smart contracts from the token hype.',
      actions: [A('Read the blockchain guide', '/blockchain'), A('Browse guides', '/techtopics'), A('Live tech news', '/news')]
    },
    {
      keys: ['market', 'markets', 'stock', 'stocks', 'invest', 'investing', 'crypto', 'bitcoin', 'ethereum', 'btc', 'eth', 'price', 'prices'],
      text: 'For markets, open CoinCompass for live prices and trends, or read the market briefing for context.',
      actions: [A('Open CoinCompass', '/coincompass'), A('Read the blog', '/blog'), A('Live tech news', '/news')]
    },
    {
      keys: ['news', 'headline', 'headlines', 'techcrunch', 'latest', 'current'],
      text: 'The live desk pulls fresh TechCrunch headlines. I can also take you to the guides that explain the story.',
      actions: [A('Open the news desk', '/news'), A('Browse guides', '/techtopics'), A('Read the blog', '/blog')]
    },
    {
      keys: ['quiz', 'quizzes', 'test', 'grade', 'trivia', 'questions'],
      text: 'The quiz has six topics and five questions each. Pick a topic, answer, and your best grade is saved on this device.',
      actions: [A('Take a quiz', '/quiz'), A('Browse guides', '/techtopics'), A('Live tech news', '/news')]
    },
    {
      keys: ['tool', 'tools', 'json', 'password generator', 'markdown', 'converter', 'calculator', 'utility'],
      text: 'The toolbox has 12 free browser utilities, including InfohubGPT, JSON, passwords, markdown and unit conversion.',
      actions: [A('Open the toolbox', '/software'), A('Open InfohubGPT', '/software/infohubgpt'), A('Try a quiz', '/quiz')]
    },
    {
      keys: ['game', 'games', 'arcade', 'snake', '2048', 'pong', 'break'],
      text: 'The arcade has eight browser games, including Snake, 2048, Pong and Memory. No download needed.',
      actions: [A('Enter the arcade', '/games'), A('Take a quiz', '/quiz'), A('Live tech news', '/news')]
    },
    {
      keys: ['guide', 'guides', 'topic', 'topics', 'learn', 'beginner', 'explain', 'explained'],
      text: 'The guide index has 30 plain-language explainers, from AI to smart cities. Each one ends with a practical next step.',
      actions: [A('Browse all 30 guides', '/techtopics'), A('Try a quiz', '/quiz'), A('Live tech news', '/news')]
    },
    {
      keys: ['ar', 'augmented reality', 'vr', 'virtual reality', 'headset'],
      text: 'The VR and AR guides cover training, design review, simulation and the comfort problems still holding headsets back.',
      actions: [A('VR guide', '/virtualreality'), A('AR guide', '/augmentedreality'), A('Browse guides', '/techtopics')]
    },
    {
      keys: ['space', 'satellite', 'rocket', 'launch'],
      text: 'The space technology guide covers reuse, launch costs and the access problem — without the sci-fi.',
      actions: [A('Space technology guide', '/spacetechnology'), A('Browse guides', '/techtopics'), A('Live tech news', '/news')]
    },
    {
      keys: ['nano', 'nanotechnology', 'materials'],
      text: 'The nanotechnology guide explains what changes at the nanoscale and where the real engineering limits are.',
      actions: [A('Nanotechnology guide', '/nanotechnology'), A('Semiconductor guide', '/semiconductors'), A('Browse guides', '/techtopics')]
    },
    {
      keys: ['wearable', 'wearables', 'watch', 'smartwatch'],
      text: 'The wearables guide covers health sensing, AR and ambient computing — and the battery and privacy trade-offs.',
      actions: [A('Wearables guide', '/wearabletechnology'), A('Browse guides', '/techtopics'), A('Try a quiz', '/quiz')]
    },
    {
      keys: ['smart city', 'smart cities', 'city', 'cities', 'urban'],
      text: 'The smart cities guide looks at sensors, data and public trust — the part that decides whether a pilot scales.',
      actions: [A('Smart cities guide', '/smartcities'), A('IoT guide', '/internetofthings'), A('Browse guides', '/techtopics')]
    },
    {
      keys: ['green', 'climate', 'sustainability', 'energy'],
      text: 'The green technology guide covers the engineering and the trade-offs behind cleaner infrastructure.',
      actions: [A('Green technology guide', '/greentechnology'), A('Smart cities guide', '/smartcities'), A('Browse guides', '/techtopics')]
    },
    {
      keys: ['iot', 'internet of things', 'sensor', 'sensors'],
      text: 'The IoT guide covers connected sensors, the data they create and the new doors every endpoint opens.',
      actions: [A('Read the IoT guide', '/internetofthings'), A('Smart cities guide', '/smartcities'), A('Browse guides', '/techtopics')]
    },
    {
      keys: ['5g', 'network', 'networks', 'latency'],
      text: 'The 5G and edge guides explain what low latency actually changes and where the network still stops.',
      actions: [A('5G networks guide', '/5gnetworks'), A('Edge computing guide', '/edgecomputing'), A('Browse guides', '/techtopics')]
    },
    {
      keys: ['open source', 'opensource', 'github', 'license'],
      text: 'The open source guide covers communities, licences and the maintenance burden behind free code.',
      actions: [A('Open source guide', '/opensource'), A('Browse guides', '/techtopics'), A('Live tech news', '/news')]
    },
    {
      keys: ['data', 'big data', 'analytics', 'database'],
      text: 'The big data guide covers pipelines, storage and the part most teams underestimate: cleaning and labelling.',
      actions: [A('Big data guide', '/bigdata'), A('AI guide', '/artificialintelligence'), A('Browse guides', '/techtopics')]
    },
    {
      keys: ['devops', 'deploy', 'deployment', 'pipeline', 'kubernetes'],
      text: 'The DevOps guide covers delivery, reliability and the trade-offs behind a calm deployment pipeline.',
      actions: [A('DevOps guide', '/devops'), A('Browse guides', '/techtopics'), A('Live tech news', '/news')]
    },
    {
      keys: ['product', 'products', 'laptop', 'phone', 'iphone', 'buy', 'buying'],
      text: 'The tech products section has buying guides and the technical explainers behind the specs.',
      actions: [A('Tech buying guides', '/techproducts'), A('Semiconductor guide', '/semiconductors'), A('Browse guides', '/techtopics')]
    }
  ];

  function hasWord(text, key) {
    if (key.indexOf(' ') !== -1) return text.indexOf(key) !== -1;
    return new RegExp('(^|[^a-z0-9])' + key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '([^a-z0-9]|$)', 'i').test(text);
  }

  function detect(q) {
    for (var i = 0; i < RULES.length; i++) {
      for (var j = 0; j < RULES[i].keys.length; j++) {
        if (hasWord(q, RULES[i].keys[j])) return RULES[i];
      }
    }
    return null;
  }

  var soundOn = read(SOUND_KEY) !== '0';
  var audioCtx = null;
  var userInteracted = false;
  var bubbleDismissed = false;
  var overlayOpen = false;
  var typeTimer = null;
  var typeTarget = null;
  var snoozeTimer = null;
  var avatar, bubble, bubbleSpeech, bubbleActions, overlay, modal, modalSpeech, modalActions;
  var modalArt, modalClose, modalInput, modalForm, modalSnooze;

  function markInteraction() { userInteracted = true; }
  document.addEventListener('pointerdown', markInteraction, { passive: true, once: true });
  document.addEventListener('keydown', markInteraction, { once: true });

  function playChime() {
    if (!soundOn || !userInteracted) return;
    try {
      var Ctx = window.AudioContext || window.webkitAudioContext;
      if (!Ctx) return;
      audioCtx = audioCtx || new Ctx();
      if (audioCtx.state === 'suspended') audioCtx.resume();
      var now = audioCtx.currentTime;
      [[620, 0, 0.09], [880, 0.075, 0.13]].forEach(function (note) {
        var osc = audioCtx.createOscillator();
        var gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(note[0], now + note[1]);
        gain.gain.setValueAtTime(0.0001, now + note[1]);
        gain.gain.exponentialRampToValueAtTime(0.05, now + note[1] + 0.012);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + note[1] + note[2]);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now + note[1]);
        osc.stop(now + note[1] + note[2] + 0.02);
      });
    } catch (e) {}
  }

  function snoozeUntil() {
    var value = parseInt(read(SNOOZE_KEY) || '0', 10);
    return value > Date.now() ? value : 0;
  }
  function isSnoozed() { return snoozeUntil() > 0; }
  function clockLabel(ts) {
    try { return new Date(ts).toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' }); }
    catch (e) { return 'later'; }
  }
  function updateAvatarState() {
    if (!avatar) return;
    var snoozed = isSnoozed();
    avatar.classList.toggle('is-snoozed', snoozed);
    avatar.setAttribute('aria-label', snoozed ? 'Digi is snoozed until ' + clockLabel(snoozeUntil()) + '. Tap to wake.' : 'Open Digi, the Digital Infohub site guide');
    avatar.title = snoozed ? 'Digi is snoozed until ' + clockLabel(snoozeUntil()) : 'Ask Digi';
  }
  function updateSoundButton() {
    var btn = document.getElementById('digiSound');
    if (!btn) return;
    btn.textContent = soundOn ? '🔊' : '🔇';
    btn.setAttribute('aria-pressed', soundOn ? 'true' : 'false');
    btn.setAttribute('aria-label', soundOn ? 'Mute Digi sound' : 'Turn on Digi sound');
    btn.title = soundOn ? 'Sound on' : 'Sound off';
  }

  function snooze(ms) {
    var until = Date.now() + ms;
    write(SNOOZE_KEY, until);
    updateAvatarState();
    closeBubble(true);
    closeCenter(false);
    notify('Digi snoozed until ' + clockLabel(until) + '.');
    if (snoozeTimer) clearTimeout(snoozeTimer);
    snoozeTimer = setTimeout(function () {
      updateAvatarState();
      notify('Digi is back.');
    }, ms + 80);
  }
  function wake() {
    remove(SNOOZE_KEY);
    if (snoozeTimer) { clearTimeout(snoozeTimer); snoozeTimer = null; }
    updateAvatarState();
  }

  function finishTyping() {
    if (!typeTimer) return;
    clearInterval(typeTimer);
    typeTimer = null;
    if (typeTarget) {
      typeTarget.textContent = typeTarget._digiFull || typeTarget.textContent;
      typeTarget.classList.remove('is-typing');
    }
    if (avatar) avatar.classList.remove('is-talking');
    if (modalArt) modalArt.classList.remove('is-talking');
  }

  function typeInto(el, text) {
    if (!el) return;
    finishTyping();
    typeTarget = el;
    el._digiFull = text;
    el.textContent = '';
    el.classList.add('is-typing');
    if (avatar) avatar.classList.add('is-talking');
    if (overlayOpen && modalArt) modalArt.classList.add('is-talking');
    if (reduced || !text) {
      el.textContent = text;
      el.classList.remove('is-typing');
      if (avatar) avatar.classList.remove('is-talking');
      if (modalArt) modalArt.classList.remove('is-talking');
      return;
    }
    var i = 0;
    var length = text.length;
    typeTimer = setInterval(function () {
      i += 1;
      el.textContent = text.slice(0, i);
      if (i >= length) {
        clearInterval(typeTimer);
        typeTimer = null;
        el.classList.remove('is-typing');
        if (avatar) avatar.classList.remove('is-talking');
        if (modalArt) modalArt.classList.remove('is-talking');
      }
    }, 10);
  }

  function actionNode(action) {
    var el;
    if (action.href) {
      el = document.createElement('a');
      el.href = action.href;
    } else {
      el = document.createElement('button');
      el.type = 'button';
      el.addEventListener('click', function () { ask(action.prompt || action.label); });
    }
    el.className = 'digi-action';
    el.textContent = action.label;
    return el;
  }

  function renderActions(container, actions) {
    if (!container) return;
    container.innerHTML = '';
    (actions || []).forEach(function (action) {
      if (action) container.appendChild(actionNode(action));
    });
    container.classList.toggle('is-empty', !container.children.length);
  }

  function speak(text, actions) {
    if (overlayOpen) {
      typeInto(modalSpeech, text);
      renderActions(modalActions, actions);
      return;
    }
    bubble.classList.add('is-open');
    bubble.setAttribute('aria-hidden', 'false');
    avatar.setAttribute('aria-expanded', 'true');
    typeInto(bubbleSpeech, text);
    renderActions(bubbleActions, actions);
  }

  function closeBubble(dismiss) {
    if (!bubble) return;
    finishTyping();
    bubble.classList.remove('is-open');
    bubble.setAttribute('aria-hidden', 'true');
    avatar.setAttribute('aria-expanded', 'false');
    if (dismiss) bubbleDismissed = true;
  }

  function openBubble() {
    if (overlayOpen) return;
    if (isSnoozed()) wake();
    if (bubble.classList.contains('is-open')) {
      closeBubble(true);
      return;
    }
    var ctx = pageContext();
    var text = Math.random() < 0.55 ? ctx.fact : ctx.intro;
    speak(text, ctx.actions);
    playChime();
  }

  function openCenter() {
    if (location.pathname.replace(/\/+$/, '').replace(/\.html$/, '') === '/digi') {
      location.href = '/digi';
      return;
    }
    if (overlayOpen) return;
    if (isSnoozed()) wake();
    closeBubble(false);
    var ctx = pageContext();
    overlayOpen = true;
    overlay.classList.add('is-open');
    overlay.setAttribute('aria-hidden', 'false');
    document.documentElement.classList.add('digi-modal-open');
    document.body.classList.add('digi-modal-open');
    typeInto(modalSpeech, ctx.intro + ' ' + ctx.fact);
    renderActions(modalActions, ctx.actions);
    playChime();
    setTimeout(function () { if (overlayOpen) modalClose.focus(); }, 70);
  }

  function closeCenter(restoreFocus) {
    if (!overlayOpen) return;
    overlayOpen = false;
    overlay.classList.remove('is-open');
    overlay.setAttribute('aria-hidden', 'true');
    document.documentElement.classList.remove('digi-modal-open');
    document.body.classList.remove('digi-modal-open');
    finishTyping();
    if (restoreFocus !== false && avatar) avatar.focus();
  }

  function ask(input) {
    var ctx = pageContext();
    var q = String(input || '').toLowerCase().replace(/\s+/g, ' ').trim();
    if (!q) {
      speak(ctx.intro, ctx.actions);
      return;
    }
    if (/(^|\b)(snooze|quiet|hide)(\b|$)/.test(q)) {
      snooze(60 * 60 * 1000);
      return;
    }
    if (/(^|\b)(close|dismiss)(\b|$)/.test(q)) {
      closeBubble(true);
      return;
    }
    if (/(^|\b)(hello|hi|hey|yo)(\b|$)/.test(q)) {
      speak("Hi — I'm Digi. I can route you to a guide, the quiz, the live news desk or a free tool. What do you need?", ctx.actions);
      return;
    }
    if (/(did you know|surprise me|something new|^fact$)/.test(q)) {
      speak(ctx.fact, ctx.actions);
      return;
    }
    if (/(where am i|this page|what is this)/.test(q)) {
      speak(ctx.intro, ctx.actions);
      return;
    }
    if (/(who are you|your name|what are you)/.test(q)) {
      speak("I'm Digi, Digital Infohub's rule-based site guide. I don't browse the web — I route you around the hub.", [A('Browse the guides', '/techtopics'), A('Take a quiz', '/quiz')]);
      return;
    }
    if (/(help|what can you do|how do you work)/.test(q)) {
      speak('I know 30 guides, 12 free tools, six quizzes, eight games and the live news desk. Ask about a topic, or tap one of these.', ctx.actions);
      return;
    }
    if (/(thank|thanks|cheers)/.test(q)) {
      speak('Any time. The guide index is always a good next stop.', [A('Browse guides', '/techtopics'), A('Live tech news', '/news')]);
      return;
    }

    var rule = detect(q);
    if (rule) {
      speak(rule.text, rule.actions);
      return;
    }
    speak("I don't have a rule for that one yet. I know this site's topics best: AI, security, cloud, chips, robotics, quantum, markets, news, tools, games and the quiz.", [
      A('Browse all 30 guides', '/techtopics'),
      A('Try a quiz', '/quiz'),
      A('Live tech news', '/news')
    ]);
  }

  function buildUI() {
    var root = document.createElement('div');
    root.id = 'digiRoot';
    root.className = 'digi-corner';
    root.innerHTML =
      '<div class="digi-bubble" id="digiBubble" role="dialog" aria-modal="false" aria-label="Digi, the Digital Infohub site guide" aria-hidden="true">' +
        '<div class="digi-head">' +
          '<span class="digi-kicker"><span class="digi-pip" aria-hidden="true"></span>DIGI · SITE GUIDE</span>' +
          '<div class="digi-tools">' +
            '<button type="button" class="digi-tool" id="digiExpand" aria-label="Open Digi in the center" title="Open big card">⤢</button>' +
            '<button type="button" class="digi-tool" id="digiSound" aria-label="Mute Digi sound" aria-pressed="true" title="Sound on">🔊</button>' +
            '<button type="button" class="digi-tool" id="digiSnooze" aria-label="Snooze Digi for one hour" title="Snooze 1 hour">☾</button>' +
            '<button type="button" class="digi-tool" id="digiClose" aria-label="Close Digi message" title="Close">✕</button>' +
          '</div>' +
        '</div>' +
        '<p class="digi-speech" id="digiSpeech" aria-live="polite"></p>' +
        '<div class="digi-actions" id="digiActions"></div>' +
        '<form class="digi-form" id="digiForm">' +
          '<input class="digi-input" id="digiInput" type="text" placeholder="Ask Digi about a tech topic…" autocomplete="off" maxlength="80" aria-label="Ask Digi about a tech topic">' +
          '<button class="digi-send" type="submit">Ask</button>' +
        '</form>' +
        '<p class="digi-credit">Artwork by <a href="' + ARTIFY + '" target="_blank" rel="noopener noreferrer">Artify Space</a> <span aria-hidden="true">·</span> <a href="' + ARTIFY + '" target="_blank" rel="noopener noreferrer">See what they make</a></p>' +
      '</div>' +
      '<button type="button" class="digi-avatar" id="digiAvatar" aria-label="Open Digi, the Digital Infohub site guide" aria-expanded="false" aria-controls="digiBubble">' +
        '<span class="digi-avatar-glow" aria-hidden="true"></span>' +
        '<img src="/assets/digi.png" alt="Digi, Digital Infohub&#39;s site guide — artwork by Artify Space" width="96" height="116" draggable="false" decoding="async">' +
        '<span class="digi-avatar-dot" aria-hidden="true"></span>' +
      '</button>';

    var overlayEl = document.createElement('div');
    overlayEl.id = 'digiOverlay';
    overlayEl.className = 'digi-overlay';
    overlayEl.setAttribute('aria-hidden', 'true');
    overlayEl.innerHTML =
      '<div class="digi-modal" id="digiModal" role="dialog" aria-modal="true" aria-labelledby="digiModalTitle" tabindex="-1">' +
        '<button type="button" class="digi-modal-close" id="digiModalClose" aria-label="Close Digi">✕</button>' +
        '<div class="digi-modal-art" id="digiModalArt">' +
          '<img src="/assets/digi.png" alt="Digi, Digital Infohub&#39;s site guide — artwork by Artify Space" width="180" height="218" draggable="false" decoding="async">' +
          '<span class="digi-modal-art-label">MEET DIGI</span>' +
        '</div>' +
        '<div class="digi-modal-body">' +
          '<span class="digi-kicker"><span class="digi-pip" aria-hidden="true"></span>YOUR DIGITAL INFOHUB COMPANION</span>' +
          '<h2 id="digiModalTitle">Meet Digi</h2>' +
          '<p class="digi-modal-speech" id="digiModalSpeech" aria-live="polite"></p>' +
          '<div class="digi-actions" id="digiModalActions"></div>' +
          '<form class="digi-form" id="digiModalForm">' +
            '<input class="digi-input" id="digiModalInput" type="text" placeholder="Ask Digi about a tech topic…" autocomplete="off" maxlength="80" aria-label="Ask Digi about a tech topic">' +
            '<button class="digi-send" type="submit">Ask</button>' +
          '</form>' +
          '<p class="digi-credit">Digi artwork by <a href="' + ARTIFY + '" target="_blank" rel="noopener noreferrer">Artify Space</a>. <a href="' + ARTIFY + '" target="_blank" rel="noopener noreferrer">Learn more about Artify Space →</a></p>' +
          '<button type="button" class="digi-snooze-today" id="digiModalSnooze">Snooze Digi for today</button>' +
        '</div>' +
      '</div>';

    document.body.appendChild(root);
    document.body.appendChild(overlayEl);

    bubble = document.getElementById('digiBubble');
    bubbleSpeech = document.getElementById('digiSpeech');
    bubbleActions = document.getElementById('digiActions');
    avatar = document.getElementById('digiAvatar');
    overlay = document.getElementById('digiOverlay');
    modal = document.getElementById('digiModal');
    modalArt = document.getElementById('digiModalArt');
    modalSpeech = document.getElementById('digiModalSpeech');
    modalActions = document.getElementById('digiModalActions');
    modalClose = document.getElementById('digiModalClose');
    modalInput = document.getElementById('digiModalInput');
    modalForm = document.getElementById('digiModalForm');
    modalSnooze = document.getElementById('digiModalSnooze');

    bubbleSpeech.addEventListener('click', finishTyping);
    modalSpeech.addEventListener('click', finishTyping);

    document.getElementById('digiForm').addEventListener('submit', function (e) {
      e.preventDefault();
      var input = document.getElementById('digiInput');
      var value = input.value;
      input.value = '';
      ask(value);
    });
    document.getElementById('digiModalForm').addEventListener('submit', function (e) {
      e.preventDefault();
      var value = modalInput.value;
      modalInput.value = '';
      ask(value);
    });

    avatar.addEventListener('click', openBubble);
    document.getElementById('digiClose').addEventListener('click', function () { closeBubble(true); });
    document.getElementById('digiSnooze').addEventListener('click', function () { snooze(60 * 60 * 1000); });
    document.getElementById('digiExpand').addEventListener('click', openCenter);
    document.getElementById('digiSound').addEventListener('click', function () {
      soundOn = !soundOn;
      write(SOUND_KEY, soundOn ? '1' : '0');
      updateSoundButton();
      if (soundOn) playChime();
      else notify('Digi sound off.');
    });
    document.getElementById('digiModalClose').addEventListener('click', function () { closeCenter(); });
    document.getElementById('digiModalSnooze').addEventListener('click', function () {
      var midnight = new Date();
      midnight.setHours(24, 0, 0, 0);
      snooze(midnight.getTime() - Date.now());
    });
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) closeCenter();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      if (overlayOpen) closeCenter();
      else if (bubble.classList.contains('is-open')) closeBubble(true);
    });

    var fallback = 'https://raw.githubusercontent.com/digitalinfohub/digitalinfohub/refs/heads/main/digi.png';
    document.querySelectorAll('#digiRoot img, #digiOverlay img').forEach(function (img) {
      img.addEventListener('error', function () {
        if (img.getAttribute('src') !== fallback) img.src = fallback;
      });
    });

    updateSoundButton();
    updateAvatarState();
  }

  function start() {
    document.body.classList.add('digi-on');
    buildUI();
    var ctx = pageContext();
    if (!ctx || !bubble) return;

    /* Keep the automatic nudge out of the way on phones and on the pages
       that already lead with Digi or a dense dashboard. The corner avatar
       still opens the guide on demand. */
    var quietPage = path === '/' || path === '/coincompass';
    if (window.innerWidth > 720 && !quietPage) {
      setTimeout(function () {
        if (overlayOpen || isSnoozed() || bubbleDismissed || document.hidden) return;
        var current = pageContext();
        speak(Math.random() < 0.55 ? current.fact : current.intro, current.actions);
        playChime();
      }, 6500);
    }

    var seen = false;
    try { seen = window.sessionStorage.getItem(CENTER_KEY) === '1'; } catch (e) {}
    /* The homepage has a prominent Ask Digi bar; do not cover it with an
       automatic full-screen card. The corner helper still introduces Digi. */
    if (!seen && !quietPage && window.innerWidth > 720) {
      setTimeout(function () {
        if (overlayOpen || isSnoozed() || document.hidden || userInteracted) return;
        try { window.sessionStorage.setItem(CENTER_KEY, '1'); } catch (e) {}
        openCenter();
      }, 18000);
    }
    if (/[?&]digi=center/.test(location.search)) setTimeout(openCenter, 700);

    window.Digi = {
      open: openCenter,
      center: openCenter,
      bubble: openBubble,
      say: function (text) { speak(text, pageContext().actions); },
      snooze: snooze,
      wake: wake,
      close: function () { closeBubble(true); closeCenter(); },
      state: function () {
        return {
          snoozed: isSnoozed(),
          sound: soundOn,
          bubbleOpen: bubble.classList.contains('is-open'),
          centerOpen: overlayOpen
        };
      }
    };
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
