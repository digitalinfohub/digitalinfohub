/* QR Code Generator — uses the locally bundled qrcodejs library (MIT). */
(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };
  var text = $('qrText'), size = $('qrSize'), ec = $('qrEc');
  var stage = $('stage'), meta = $('meta'), err = $('qrError');
  var generateBtn = $('generate'), downloadBtn = $('download'), download2 = $('download2'), copyBtn = $('copyImage');
  var canvas = null;

  function libReady() { return typeof window.QRCode !== 'undefined'; }
  function showError(message) { err.textContent = message; err.style.display = 'block'; }

  function generate() {
    var value = text.value.trim() || 'https://digitalinfohub.net';
    if (!libReady()) { showError('The QR library could not load. Check your connection and reload the page.'); return; }
    err.style.display = 'none';
    stage.innerHTML = '';
    var box = document.createElement('div');
    stage.appendChild(box);
    try {
      new window.QRCode(box, {
        text: value,
        width: 640,
        height: 640,
        colorDark: '#07070c',
        colorLight: '#ffffff',
        correctLevel: window.QRCode.CorrectLevel[ec.value] || window.QRCode.CorrectLevel.M
      });
    } catch (error) {
      showError('Could not create that QR code. Try shorter text.');
      return;
    }
    canvas = box.querySelector('canvas');
    var fallbackImg = box.querySelector('img');
    if (fallbackImg) fallbackImg.style.display = 'none';
    if (!canvas) { showError('Could not draw the QR code in this browser.'); return; }
    meta.textContent = value.length + ' characters · ' + ec.value + ' error correction';
    [downloadBtn, download2, copyBtn].forEach(function (b) { b.disabled = false; });
  }

  function download() {
    if (!canvas) return;
    var target = parseInt(size.value, 10) || 1024;
    var out = document.createElement('canvas');
    out.width = out.height = target;
    var ctx = out.getContext('2d');
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, target, target);
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(canvas, 0, 0, target, target);
    out.toBlob(function (blob) {
      if (!blob) return;
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'qrcode-' + target + '.png';
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 4000);
    }, 'image/png');
  }

  generateBtn.addEventListener('click', generate);
  text.addEventListener('input', function () {
    clearTimeout(text.t);
    text.t = setTimeout(generate, 350);
  });
  ec.addEventListener('change', generate);
  downloadBtn.addEventListener('click', download);
  download2.addEventListener('click', download);
  copyBtn.addEventListener('click', function () {
    if (!canvas || !navigator.clipboard || !window.ClipboardItem) return;
    canvas.toBlob(function (blob) {
      navigator.clipboard.write([new ClipboardItem({ 'image/png': blob })]).then(function () {
        copyBtn.textContent = 'Copied ✓';
        setTimeout(function () { copyBtn.textContent = 'Copy image'; }, 1500);
      }).catch(function () {});
    }, 'image/png');
  });

  window.addEventListener('load', function () {
    if (!libReady()) { showError('The QR library could not load. Check your connection and reload the page.'); return; }
    generate();
  });
})();
