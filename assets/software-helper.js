/* Rule-based tool guide for Digital Infohub software.
   Runs locally, makes no network requests, and answers from a per-tool script. */
(function () {
  'use strict';
  var DATA = {
    'ascii-art': {
      name: 'Image to ASCII',
      tips: ['Use a high-contrast photo with one clear subject.', 'Width 80–120 reads best on a phone.', 'Pick full colour text or blocks, then download a transparent PNG.'],
      qa: [
        { q: 'Why is my image blank?', k: ['blank', 'empty', 'nothing'], a: 'Try a JPG or PNG with visible contrast. Very dark or very light images can collapse into one character; raise contrast to about 1.4 and convert again.' },
        { q: 'How do I get a transparent PNG?', k: ['transparent', 'png', 'download'], a: 'Choose full colour text or blocks, convert your image, then press “Download PNG”. The canvas has no background, so the PNG is transparent.' },
        { q: 'How do I change the colour?', k: ['colour', 'color', 'palette'], a: 'Set “Colour mode” to full colour text or full colour blocks to keep the photo palette. In monochrome mode, use the text colour picker for a single-colour stencil.' }
      ]
    },
    'color-picker': {
      name: 'Hex Colour Picker',
      tips: ['Paste a hex value, or use the native picker.', 'Click any shade, tint or harmony to load it.', 'The contrast checker follows WCAG AA thresholds.'],
      qa: [
        { q: 'How do I copy a value?', k: ['copy', 'hex', 'rgb'], a: 'Click any value row (HEX, RGB, HSL, CMYK) to copy it. The toast confirms what was copied.' },
        { q: 'What contrast do I need?', k: ['contrast', 'wcag', 'accessibility'], a: 'Aim for 4.5:1 for normal text and 3:1 for large text. The badge tells you when you only meet the large-text threshold.' },
        { q: 'Where are my recent colours?', k: ['recent', 'saved', 'history'], a: 'Recent colours are stored in this browser only. Clearing site data removes them.' }
      ]
    },
    'task-timer': {
      name: 'Task Timer',
      tips: ['Add a task, then press Start.', 'Space toggles start and pause.', 'A short beep plays when the timer ends.'],
      qa: [
        { q: 'Why is no sound playing?', k: ['sound', 'audio', 'beep', 'silent'], a: 'Browsers block audio until you interact with the page. Press Start once, and the finish beep will work for that session.' },
        { q: 'Can I run two timers?', k: ['two', 'multiple', 'parallel'], a: 'No. The timer is intentionally single-task so a time box cannot silently run twice.' },
        { q: 'Does it keep counting in the background?', k: ['background', 'tab', 'close'], a: 'The countdown continues while the tab is open. Closing the tab resets the timer.' }
      ]
    },
    'todo': {
      name: 'To-do List',
      tips: ['Press Enter to add a task.', 'Click the text to tick it off.', 'Everything saves in this browser.'],
      qa: [
        { q: 'Where are my tasks saved?', k: ['save', 'storage', 'lost', 'persist'], a: 'In local storage on this device. Private browsing or clearing site data will remove them.' },
        { q: 'Can I recover deleted tasks?', k: ['recover', 'undo', 'deleted'], a: 'Deletion is immediate. There is no undo, so export anything important before clearing the list.' },
        { q: 'Can I sync between devices?', k: ['sync', 'phone', 'laptop'], a: 'No. The list never leaves this browser, which is what keeps it private.' }
      ]
    },
    'webp-to-png': {
      name: 'WebP to PNG',
      tips: ['Drop several files at once.', 'PNG is lossless, so files often get larger.', 'Transparency is preserved.'],
      qa: [
        { q: 'Why did my file get bigger?', k: ['bigger', 'size', 'larger'], a: 'WebP compresses more aggressively. PNG is lossless, so the converted file is usually larger — that is expected.' },
        { q: 'Why did a file fail?', k: ['fail', 'error', 'not working'], a: 'Some WebP variants or corrupt files cannot be decoded by the browser. Re-export the source image and try again.' },
        { q: 'Are files uploaded?', k: ['upload', 'server', 'privacy'], a: 'No. Decoding and re-encoding happen in this tab.' }
      ]
    },
    'qr-code-generator': {
      name: 'QR Code Generator',
      tips: ['Short links scan faster.', 'Use High (H) correction for print.', 'Download at 1024px or larger for posters.'],
      qa: [
        { q: 'Why will my code not scan?', k: ['scan', 'not working', 'camera'], a: 'Increase the size, shorten the text, or raise error correction. Very long text creates a dense code that phone cameras struggle with.' },
        { q: 'Which size should I download?', k: ['size', 'download', 'print'], a: '512px for screens, 1024px for documents, 2048px for print. Keep at least 2cm of white space around the code.' },
        { q: 'Can I use it commercially?', k: ['commercial', 'business', 'license'], a: 'Yes. The code is generated locally and you own the resulting image.' }
      ]
    },
    'calendar': {
      name: 'Calendar',
      tips: ['Click any day to select it.', 'Add events with a time and title.', 'Use the day dropdown to jump between events.'],
      qa: [
        { q: 'Where are events stored?', k: ['save', 'storage', 'sync'], a: 'Locally in this browser. Nothing is sent to a server and there is no cross-device sync.' },
        { q: 'How do I see a day’s events?', k: ['agenda', 'dropdown', 'events'], a: 'Select the day, then use “Upcoming on this day”. Choosing an event highlights it in the list.' },
        { q: 'Can I delete an event?', k: ['delete', 'remove'], a: 'Press the × on the event row. Deletion is immediate.' }
      ]
    },
    'scrapbook': {
      name: 'Digital Scrapbook',
      tips: ['Add up to 8 photos for a balanced page.', 'Captions use a handwriting-style font.', 'Download a high-resolution paper page as PNG.'],
      qa: [
        { q: 'How many photos fit?', k: ['many', 'limit', 'photos'], a: 'Eight photos keep the page readable. You can add more, but the export gets crowded.' },
        { q: 'How do I change the paper?', k: ['paper', 'background', 'style'], a: 'Use the paper selector for cream, kraft or grid. The export uses the same paper.' },
        { q: 'Are photos uploaded?', k: ['upload', 'privacy', 'server'], a: 'No. Images stay in the tab and are only drawn to your own canvas.' }
      ]
    },
    'font-maker': {
      name: 'Font / Type Card Maker',
      tips: ['Type a short phrase for a poster-like card.', 'Letter spacing changes the whole feel.', 'Tick transparent background for overlays.'],
      qa: [
        { q: 'Can I download a font file?', k: ['font file', 'ttf', 'otf', 'install'], a: 'This tool creates a type specimen PNG, not an installable font file. Use it for headers, thumbnails and social cards.' },
        { q: 'How do I get a transparent PNG?', k: ['transparent', 'background'], a: 'Tick “Transparent background”, then download. The letters keep their colour and the canvas stays clear.' },
        { q: 'Why does my text overflow?', k: ['overflow', 'cut off', 'too big'], a: 'Lower the size, shorten the phrase, or switch to a narrower system font.' }
      ]
    },
    'graphic-design': {
      name: 'Graphic Designer',
      tips: ['Add text, rectangles or circles, then drag on the canvas.', 'Use the layer list to reorder objects.', 'Export a transparent PNG by unchecking the background.'],
      qa: [
        { q: 'How do I move an object?', k: ['move', 'drag', 'position'], a: 'Click the object on the canvas and drag it. You can also type exact X and Y values in the inspector.' },
        { q: 'Why can’t I select my text?', k: ['select', 'text', 'click'], a: 'Click directly on the letters. If objects overlap, use the layer list to select the one underneath.' },
        { q: 'Can I export with no background?', k: ['transparent', 'background'], a: 'Untick “Background” before exporting. The PNG will have a transparent canvas.' }
      ]
    },
    'html-coder': {
      name: 'HTML Coder',
      tips: ['Edit the code and the preview refreshes as you type.', 'Download the file or open it in a new tab.', 'Scripts run in a sandboxed preview.'],
      qa: [
        { q: 'Why is my preview blank?', k: ['blank', 'preview', 'nothing'], a: 'Check for an unclosed tag or a script error. The preview only runs HTML, CSS and JavaScript — no server-side code.' },
        { q: 'Can I use images?', k: ['image', 'img', 'photo'], a: 'Yes, with a full https URL. Local file paths will not resolve inside the preview.' },
        { q: 'Does it save my code?', k: ['save', 'storage', 'lost'], a: 'The editor keeps your current code in this browser. Download the .html file to keep a permanent copy.' }
      ]
    },
    'business-card': {
      name: 'Business Card Maker',
      tips: ['Fill the fields and the card updates live.', 'Download a print-ready PNG.', 'Share uses your device’s share sheet where supported.'],
      qa: [
        { q: 'What size is the export?', k: ['size', 'resolution', 'print'], a: 'The PNG is 1050×600 pixels, a 3.5:2 card ratio suitable for digital sharing and small-print proofs.' },
        { q: 'How does sharing work?', k: ['share', 'send', 'whatsapp'], a: 'On supported phones it opens the system share sheet with the PNG. Elsewhere it copies the card details as a vCard.' },
        { q: 'Why is my text cut off?', k: ['cut off', 'overflow', 'long'], a: 'Keep the name under 28 characters, the role under 34 and the other lines short. The PNG export draws a single line per field, so very long text is clipped rather than wrapped.' }
      ]
    },
    'travel-planner': {
      name: 'Travel Planner',
      tips: ['Set a budget first, then add activities with costs.', 'The bar shows how much of the budget is planned.', 'Everything saves in this browser.'],
      qa: [
        { q: 'How is the budget calculated?', k: ['budget', 'cost', 'total'], a: 'Activity costs are added up and compared with your budget. The remaining figure updates as you edit.' },
        { q: 'Can I plan multiple trips?', k: ['multiple', 'trips', 'another'], a: 'This planner holds one trip at a time. Download or copy the plan before starting another.' },
        { q: 'Does it convert currencies?', k: ['currency', 'convert', 'exchange'], a: 'No. Enter every cost in the same currency and the totals stay consistent.' }
      ]
    },
    'marketing-assistant': {
      name: 'Marketing Assistant',
      tips: ['Be specific about the product and audience.', 'Generate, then edit the copy in your own voice.', 'Everything is rule-based and stays on your device.'],
      qa: [
        { q: 'Is this real AI?', k: ['ai', 'model', 'chatgpt'], a: 'No. It is a rule-based copy generator: it combines proven structures with your inputs. No text leaves your browser.' },
        { q: 'Why do the ideas repeat?', k: ['repeat', 'same', 'different'], a: 'Change the tone or goal and regenerate. More specific inputs produce more varied output.' },
        { q: 'Can I use the copy commercially?', k: ['commercial', 'use', 'copyright'], a: 'Yes, edit it and use it freely. Check any claims you add for accuracy before publishing.' }
      ]
    },
    'save-money-assistant': {
      name: 'Save Money Assistant',
      tips: ['Enter monthly figures after tax.', 'The 50/30/20 view is a guide, not a rule.', 'Adjust one category to see the effect immediately.'],
      qa: [
        { q: 'How is the savings rate calculated?', k: ['savings rate', 'percent', 'calculate'], a: 'Leftover income divided by income. A negative leftover means you are spending more than you earn.' },
        { q: 'What is 50/30/20?', k: ['50/30/20', 'budget rule'], a: 'A simple guide: 50% needs, 30% wants and 20% savings. High housing costs often make it unrealistic, so treat it as a target.' },
        { q: 'Is my data private?', k: ['private', 'data', 'upload'], a: 'Yes. Figures are stored only in this browser and never uploaded.' }
      ]
    },
    'calculator': { name: 'Calculator', tips: ['Use the keyboard for fast entry.', 'C clears the current sum.', 'Results are not saved.'], qa: [{ q: 'Does it keep history?', k: ['history', 'save'], a: 'No. The calculator resets when you reload the page.' }] },
    'converter': { name: 'Unit Converter', tips: ['Pick a category, then a unit pair.', 'Values update as you type.', 'Conversions use standard factors.'], qa: [{ q: 'Which units are supported?', k: ['units', 'support'], a: 'Length, weight, temperature and common volume units. Switch category to see the full list.' }] },
    'password': { name: 'Password Generator', tips: ['Longer is stronger.', 'Mix symbols for maximum strength.', 'Generate locally; nothing is sent.'], qa: [{ q: 'Are passwords stored?', k: ['store', 'save', 'history'], a: 'No. Each password exists only on screen. Save it in a password manager.' }] },
    'json': { name: 'JSON Formatter', tips: ['Paste JSON to validate it.', 'Format for readable output.', 'Minify before shipping.'], qa: [{ q: 'Why does it say invalid?', k: ['invalid', 'error'], a: 'Check for trailing commas, single quotes or unquoted keys. The error position points to the problem.' }] },
    'markdown': { name: 'Markdown Preview', tips: ['Write on the left, preview on the right.', 'Use the toolbar for common syntax.', 'Copy the rendered HTML when done.'], qa: [{ q: 'Does it support tables?', k: ['table', 'support'], a: 'Yes, standard GitHub-style tables are supported in the preview.' }] }
  };

  var slug = location.pathname.replace(/\/+$/, '').split('/').pop().replace(/\.html$/, '');
  if (slug === 'software') return;
  var data = DATA[slug] || {
    name: (document.title.split('—')[0] || 'this tool').trim(),
    tips: ['Everything runs locally in your browser.', 'Use the controls on the left, then export when ready.', 'Reload the page to start fresh.'],
    qa: []
  };

  var css = document.createElement('style');
  css.textContent = '.sh-btn{position:fixed;left:18px;bottom:18px;z-index:9996;display:inline-flex;align-items:center;gap:7px;padding:10px 14px;border-radius:99px;border:1px solid rgba(255,255,255,.16);background:#15151f;color:#eef1fa;font:600 12px/1 Inter,sans-serif;cursor:pointer;box-shadow:0 10px 30px rgba(0,0,0,.35)}.sh-btn:hover{border-color:#4c8dff;color:#8fb6ff}.sh-panel{position:fixed;left:18px;bottom:64px;z-index:9997;width:min(340px,calc(100vw - 36px));max-height:min(520px,calc(100vh - 100px));display:none;flex-direction:column;border:1px solid rgba(255,255,255,.14);border-radius:16px;background:#101018;color:#eef1fa;box-shadow:0 24px 60px rgba(0,0,0,.5);overflow:hidden;font:13px/1.5 Inter,sans-serif}.sh-panel.open{display:flex}.sh-head{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:12px 14px;border-bottom:1px solid rgba(255,255,255,.09);background:#15151f}.sh-head b{font-size:12px}.sh-head span{font-size:10px;color:#8b93a7}.sh-close{border:0;background:transparent;color:#8b93a7;font-size:16px;cursor:pointer}.sh-body{padding:12px 14px;overflow:auto}.sh-tips{margin:0 0 10px;padding-left:18px;color:#b9c0d4;font-size:11.5px}.sh-tips li{margin-bottom:4px}.sh-chips{display:flex;flex-wrap:wrap;gap:5px;margin:8px 0}.sh-chip{padding:5px 8px;border-radius:99px;border:1px solid rgba(255,255,255,.14);background:#1a1a24;color:#b9c0d4;font-size:10.5px;cursor:pointer}.sh-chip:hover{border-color:#4c8dff;color:#8fc0ff}.sh-answer{display:none;margin-top:8px;padding:9px 10px;border-radius:9px;border:1px solid rgba(76,141,255,.3);background:rgba(76,141,255,.1);color:#dbe5ff;font-size:11.5px}.sh-form{display:flex;gap:6px;padding:10px 12px;border-top:1px solid rgba(255,255,255,.09);background:#15151f}.sh-form input{flex:1;min-width:0;padding:8px 10px;border-radius:8px;border:1px solid rgba(255,255,255,.14);background:#1a1a24;color:#eef1fa;font:inherit;font-size:11.5px;outline:none}.sh-form input:focus{border-color:#4c8dff}.sh-send{border:1px solid transparent;border-radius:8px;padding:8px 11px;background:#4c8dff;color:#fff;font:700 11px Inter,sans-serif;cursor:pointer}';
  document.head.appendChild(css);

  var tipHtml = data.tips.map(function (t) { return '<li>' + t + '</li>'; }).join('');
  var chips = data.qa.map(function (item, i) { return '<button class="sh-chip" data-i="' + i + '">' + item.q + '</button>'; }).join('');
  var wrap = document.createElement('div');
  wrap.innerHTML = '<button class="sh-btn" type="button" aria-expanded="false">🧭 Tool guide</button>' +
    '<div class="sh-panel" role="dialog" aria-label="Tool guide"><div class="sh-head"><div><b>' + data.name + ' guide</b><br><span>Rule-based · works offline</span></div><button class="sh-close" type="button" aria-label="Close guide">✕</button></div>' +
    '<div class="sh-body"><ul class="sh-tips">' + tipHtml + '</ul>' + (chips ? '<div class="sh-chips">' + chips + '</div>' : '') + '<div class="sh-answer" aria-live="polite"></div></div>' +
    '<form class="sh-form"><input type="text" placeholder="Ask how this tool works…" aria-label="Ask the tool guide"><button class="sh-send" type="submit">Ask</button></form></div>';
  document.body.appendChild(wrap);

  var btn = wrap.querySelector('.sh-btn'), panel = wrap.querySelector('.sh-panel');
  var answer = wrap.querySelector('.sh-answer'), input = wrap.querySelector('.sh-form input');
  function open(state) { panel.classList.toggle('open', state); btn.setAttribute('aria-expanded', String(state)); if (state) input.focus(); }
  function reply(text) { answer.textContent = text; answer.style.display = 'block'; }
  function find(q) {
    q = q.toLowerCase();
    var best = null, bestScore = 0;
    data.qa.forEach(function (item) {
      var score = 0;
      item.k.forEach(function (key) { if (q.indexOf(key) > -1) score += key.length; });
      if (item.q.toLowerCase().split(' ').some(function (word) { return word.length > 3 && q.indexOf(word) > -1; })) score += 2;
      if (score > bestScore) { bestScore = score; best = item; }
    });
    return best;
  }
  function ask(q) {
    var hit = find(q);
    if (hit) { reply(hit.a); return; }
    var tip = data.tips[Math.floor(Math.random() * data.tips.length)];
    reply('I do not have a specific answer for that. Quick tip: ' + tip + ' For anything else, the controls on this page are the full feature set.');
  }
  btn.addEventListener('click', function () { open(!panel.classList.contains('open')); });
  wrap.querySelector('.sh-close').addEventListener('click', function () { open(false); });
  wrap.querySelectorAll('.sh-chip').forEach(function (chip) {
    chip.addEventListener('click', function () { reply(data.qa[Number(chip.dataset.i)].a); });
  });
  wrap.querySelector('.sh-form').addEventListener('submit', function (e) {
    e.preventDefault();
    var q = input.value.trim();
    if (!q) return;
    ask(q);
    input.value = '';
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') open(false); });
})();
