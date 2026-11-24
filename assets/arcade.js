/* Digital Infohub — Pixel Palace game engine.
   Every game lives at /games/<name> but shares this file. Each mount gets a
   board, a scoreline and the same keyboard/touch conventions. */
(function () {
  'use strict';
  if (window.Arcade) return;

  function h(tag, cls, text) {
    var el = document.createElement(tag);
    if (cls) el.className = cls;
    if (text != null) el.textContent = text;
    return el;
  }
  function sound(name) {
    if (window.DIH && window.DIH.sfx) window.DIH.sfx.play(name || 'click');
  }
  function esc(s) {
    return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  function store(key, value) {
    try {
      if (value === undefined) return localStorage.getItem(key);
      localStorage.setItem(key, String(value));
    } catch (e) { return null; }
  }
  function best(key, score) {
    var current = Number(store(key) || 0);
    if (score > current) { store(key, score); return score; }
    return current;
  }

  function shell(el, opts) {
    el.innerHTML = '';
    el.classList.add('arcade');
    var head = h('div', 'arcade-bar');
    var stats = h('div', 'arcade-stats');
    var stat = function (label, id) {
      var box = h('div', 'arcade-stat');
      box.appendChild(h('span', null, label));
      var b = h('b', null, '0');
      b.id = id;
      box.appendChild(b);
      stats.appendChild(box);
      return b;
    };
    head.appendChild(stats);
    var tools = h('div', 'arcade-tools');
    var restart = h('button', 'arcade-btn', 'Restart');
    restart.type = 'button';
    tools.appendChild(restart);
    head.appendChild(tools);
    el.appendChild(head);

    var stage = h('div', 'arcade-stage');
    el.appendChild(stage);

    var msg = h('div', 'arcade-msg');
    stage.appendChild(msg);

    var controls = h('div', 'arcade-controls');
    el.appendChild(controls);

    return { stage: stage, msg: msg, stats: stats, stat: stat, restart: restart, controls: controls };
  }

  var G = {};

  /* ------------------------------------------------------------------ snake */
  G.snake = function (el) {
    var ui = shell(el);
    var scoreEl = ui.stat('Score', 'snakeScore');
    var bestEl = ui.stat('Best', 'snakeBest');
    var canvas = h('canvas', 'arcade-canvas');
    canvas.width = 400; canvas.height = 400;
    canvas.setAttribute('aria-label', 'Snake board');
    ui.stage.appendChild(canvas);
    var ctx = canvas.getContext('2d');
    var SIZE = 20, CELL = canvas.width / SIZE;
    var snake, dir, next, food, timer, score, alive, speed;

    ui.controls.innerHTML = '<span class="arcade-hint">Arrow keys / WASD to steer · Space to pause · swipe on touch</span>';

    function reset() {
      snake = [{ x: 8, y: 10 }, { x: 7, y: 10 }, { x: 6, y: 10 }];
      dir = { x: 1, y: 0 }; next = dir;
      food = { x: 14, y: 10 };
      score = 0; alive = true; speed = 130;
      scoreEl.textContent = '0';
      bestEl.textContent = store('dih_snake_best') || '0';
      ui.msg.textContent = '';
      ui.msg.classList.remove('show');
      draw();
      clearInterval(timer);
      timer = setInterval(tick, speed);
    }
    function placeFood() {
      do {
        food = { x: Math.floor(Math.random() * SIZE), y: Math.floor(Math.random() * SIZE) };
      } while (snake.some(function (s) { return s.x === food.x && s.y === food.y; }));
    }
    function tick() {
      if (!alive) return;
      dir = next;
      var head = { x: snake[0].x + dir.x, y: snake[0].y + dir.y };
      if (head.x < 0 || head.y < 0 || head.x >= SIZE || head.y >= SIZE ||
          snake.some(function (s) { return s.x === head.x && s.y === head.y; })) {
        return die();
      }
      snake.unshift(head);
      if (head.x === food.x && head.y === food.y) {
        score += 10;
        scoreEl.textContent = String(score);
        bestEl.textContent = String(best('dih_snake_best', score));
        placeFood();
        sound('success');
        if (speed > 65) {
          speed -= 4;
          clearInterval(timer);
          timer = setInterval(tick, speed);
        }
      } else {
        snake.pop();
      }
      draw();
    }
    function die() {
      alive = false;
      clearInterval(timer);
      sound('error');
      ui.msg.innerHTML = '<strong>Game over</strong><span>Score ' + score + ' · press Space or Restart</span>';
      ui.msg.classList.add('show');
    }
    function draw() {
      ctx.fillStyle = '#0a0c14';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.strokeStyle = 'rgba(255,255,255,.04)';
      for (var i = 1; i < SIZE; i++) {
        ctx.beginPath(); ctx.moveTo(i * CELL, 0); ctx.lineTo(i * CELL, canvas.height); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(0, i * CELL); ctx.lineTo(canvas.width, i * CELL); ctx.stroke();
      }
      ctx.fillStyle = '#ff6b6b';
      ctx.beginPath();
      ctx.arc(food.x * CELL + CELL / 2, food.y * CELL + CELL / 2, CELL * 0.33, 0, Math.PI * 2);
      ctx.fill();
      snake.forEach(function (s, i) {
        ctx.fillStyle = i === 0 ? '#7fd3ff' : 'rgba(76,141,255,' + (0.9 - i * 0.03) + ')';
        ctx.fillRect(s.x * CELL + 1.5, s.y * CELL + 1.5, CELL - 3, CELL - 3);
      });
    }
    function turn(x, y) {
      /* Compare against the queued direction, not the last tick's one:
         otherwise two fast turns can reverse the snake into itself. */
      if (x === -next.x && y === -next.y) return;
      next = { x: x, y: y };
    }
    function onKey(e) {
      var k = e.key.toLowerCase();
      if (['arrowup', 'w'].indexOf(k) !== -1) { turn(0, -1); e.preventDefault(); }
      if (['arrowdown', 's'].indexOf(k) !== -1) { turn(0, 1); e.preventDefault(); }
      if (['arrowleft', 'a'].indexOf(k) !== -1) { turn(-1, 0); e.preventDefault(); }
      if (['arrowright', 'd'].indexOf(k) !== -1) { turn(1, 0); e.preventDefault(); }
      if (k === ' ') { e.preventDefault(); if (!alive) reset(); }
    }
    document.addEventListener('keydown', onKey);
    var sx = 0, sy = 0;
    canvas.addEventListener('touchstart', function (e) {
      var t = e.changedTouches[0]; sx = t.clientX; sy = t.clientY;
    }, { passive: true });
    canvas.addEventListener('touchend', function (e) {
      var t = e.changedTouches[0];
      var dx = t.clientX - sx, dy = t.clientY - sy;
      if (Math.abs(dx) < 18 && Math.abs(dy) < 18) return;
      if (Math.abs(dx) > Math.abs(dy)) turn(dx > 0 ? 1 : -1, 0); else turn(0, dy > 0 ? 1 : -1);
    }, { passive: true });
    ui.restart.addEventListener('click', reset);
    reset();
    return function () { clearInterval(timer); document.removeEventListener('keydown', onKey); };
  };

  /* ------------------------------------------------------------------- 2048 */
  G['2048'] = function (el) {
    var ui = shell(el);
    var scoreEl = ui.stat('Score', 'g2048Score');
    var bestEl = ui.stat('Best', 'g2048Best');
    var board = h('div', 'tile-board');
    board.setAttribute('role', 'grid');
    board.setAttribute('aria-label', '2048 board');
    ui.stage.appendChild(board);
    ui.controls.innerHTML = '<span class="arcade-hint">Arrow keys, WASD or swipe to move tiles.</span>';
    var grid, score, over;

    function reset() {
      grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];
      score = 0; over = false;
      add(); add(); draw();
      ui.msg.textContent = ''; ui.msg.classList.remove('show');
      bestEl.textContent = store('dih_2048_best') || '0';
    }
    function add() {
      var free = [];
      for (var y = 0; y < 4; y++) for (var x = 0; x < 4; x++) if (!grid[y][x]) free.push([x, y]);
      if (!free.length) return;
      var spot = free[Math.floor(Math.random() * free.length)];
      grid[spot[1]][spot[0]] = Math.random() < 0.9 ? 2 : 4;
    }
    function draw() {
      board.innerHTML = '';
      for (var y = 0; y < 4; y++) for (var x = 0; x < 4; x++) {
        var v = grid[y][x];
        var cell = h('div', 'tile' + (v ? ' tile-' + Math.min(v, 2048) : ''), v || '');
        cell.setAttribute('role', 'gridcell');
        board.appendChild(cell);
      }
      scoreEl.textContent = String(score);
    }
    function line(vals) {
      var out = vals.filter(function (v) { return v; });
      for (var i = 0; i < out.length - 1; i++) {
        if (out[i] === out[i + 1]) { out[i] *= 2; score += out[i]; out.splice(i + 1, 1); }
      }
      while (out.length < 4) out.push(0);
      return out;
    }
    function move(dx, dy) {
      if (over) return;
      var before = JSON.stringify(grid);
      for (var i = 0; i < 4; i++) {
        var vals = [];
        for (var j = 0; j < 4; j++) {
          var x = dx === 1 ? 3 - j : dx === -1 ? j : i;
          var y = dy === 1 ? 3 - j : dy === -1 ? j : i;
          vals.push(grid[y][x]);
        }
        var merged = line(vals);
        for (var k = 0; k < 4; k++) {
          var x2 = dx === 1 ? 3 - k : dx === -1 ? k : i;
          var y2 = dy === 1 ? 3 - k : dy === -1 ? k : i;
          grid[y2][x2] = merged[k];
        }
      }
      if (JSON.stringify(grid) !== before) {
        add();
        sound('click');
        draw();
        bestEl.textContent = String(best('dih_2048_best', score));
        check();
      }
    }
    function check() {
      for (var y = 0; y < 4; y++) for (var x = 0; x < 4; x++) {
        if (!grid[y][x]) return;
        if (x < 3 && grid[y][x] === grid[y][x + 1]) return;
        if (y < 3 && grid[y][x] === grid[y + 1][x]) return;
      }
      over = true;
      sound('error');
      ui.msg.innerHTML = '<strong>No moves left</strong><span>Score ' + score + ' · restart to try again</span>';
      ui.msg.classList.add('show');
    }
    function onKey(e) {
      var k = e.key.toLowerCase();
      if (k === 'arrowup' || k === 'w') { move(0, -1); e.preventDefault(); }
      if (k === 'arrowdown' || k === 's') { move(0, 1); e.preventDefault(); }
      if (k === 'arrowleft' || k === 'a') { move(-1, 0); e.preventDefault(); }
      if (k === 'arrowright' || k === 'd') { move(1, 0); e.preventDefault(); }
    }
    document.addEventListener('keydown', onKey);
    var sx = 0, sy = 0;
    board.addEventListener('touchstart', function (e) {
      var t = e.changedTouches[0]; sx = t.clientX; sy = t.clientY;
    }, { passive: true });
    board.addEventListener('touchend', function (e) {
      var t = e.changedTouches[0];
      var dx = t.clientX - sx, dy = t.clientY - sy;
      if (Math.max(Math.abs(dx), Math.abs(dy)) < 22) return;
      if (Math.abs(dx) > Math.abs(dy)) move(dx > 0 ? 1 : -1, 0); else move(0, dy > 0 ? 1 : -1);
    }, { passive: true });
    ui.restart.addEventListener('click', reset);
    reset();
    return function () { document.removeEventListener('keydown', onKey); };
  };

  /* ------------------------------------------------------------------- pong */
  G.pong = function (el) {
    var ui = shell(el);
    var youEl = ui.stat('You', 'pongYou');
    var cpuEl = ui.stat('CPU', 'pongCpu');
    var canvas = h('canvas', 'arcade-canvas arcade-wide');
    canvas.width = 520; canvas.height = 300;
    ui.stage.appendChild(canvas);
    ui.controls.innerHTML = '<span class="arcade-hint">Move with the mouse, touch or ↑ ↓. First to 7 wins.</span>';
    var ctx = canvas.getContext('2d');
    var W = canvas.width, H = canvas.height;
    var playerY = H / 2 - 32, cpuY = H / 2 - 32, PH = 64, PW = 9;
    var ball = { x: W / 2, y: H / 2, vx: 3.6, vy: 2.4, r: 6 };
    var you = 0, cpu = 0, running = true, raf = 0;

    function serve(dir) {
      ball.x = W / 2; ball.y = H / 2;
      ball.vx = 3.6 * dir; ball.vy = (Math.random() * 2 + 1.6) * (Math.random() < 0.5 ? 1 : -1);
    }
    function draw() {
      ctx.fillStyle = '#080a12';
      ctx.fillRect(0, 0, W, H);
      ctx.strokeStyle = 'rgba(255,255,255,.14)';
      ctx.setLineDash([6, 8]);
      ctx.beginPath(); ctx.moveTo(W / 2, 0); ctx.lineTo(W / 2, H); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = '#7fd3ff';
      ctx.fillRect(12, playerY, PW, PH);
      ctx.fillStyle = 'rgba(255,255,255,.8)';
      ctx.fillRect(W - 12 - PW, cpuY, PW, PH);
      ctx.beginPath();
      ctx.arc(ball.x, ball.y, ball.r, 0, Math.PI * 2);
      ctx.fillStyle = '#fff';
      ctx.fill();
    }
    function step() {
      if (!running) return;
      ball.x += ball.vx; ball.y += ball.vy;
      if (ball.y < ball.r || ball.y > H - ball.r) { ball.vy *= -1; sound('click'); }
      var target = ball.y - PH / 2 + (ball.vx > 0 ? (Math.random() - 0.5) * 14 : 0);
      cpuY += Math.max(-3.2, Math.min(3.2, target - cpuY));
      if (ball.x - ball.r < 12 + PW && ball.x > 12 && ball.y > playerY && ball.y < playerY + PH && ball.vx < 0) {
        ball.vx = Math.abs(ball.vx) * 1.05;
        ball.vy += (ball.y - (playerY + PH / 2)) * 0.045;
        sound('open');
      }
      if (ball.x + ball.r > W - 12 - PW && ball.x < W - 12 && ball.y > cpuY && ball.y < cpuY + PH && ball.vx > 0) {
        ball.vx = -Math.abs(ball.vx) * 1.05;
        ball.vy += (ball.y - (cpuY + PH / 2)) * 0.045;
      }
      if (ball.x < -20) { cpu++; cpuEl.textContent = String(cpu); serve(1); }
      if (ball.x > W + 20) { you++; youEl.textContent = String(you); serve(-1); }
      if (you >= 7 || cpu >= 7) {
        running = false;
        sound(you >= 7 ? 'success' : 'error');
        ui.msg.innerHTML = '<strong>' + (you >= 7 ? 'You win' : 'CPU wins') + '</strong><span>' + you + ' – ' + cpu + ' · restart for another round</span>';
        ui.msg.classList.add('show');
      }
      draw();
      raf = requestAnimationFrame(step);
    }
    function moveTo(clientY) {
      var rect = canvas.getBoundingClientRect();
      var y = ((clientY - rect.top) / rect.height) * H;
      playerY = Math.max(0, Math.min(H - PH, y - PH / 2));
    }
    canvas.addEventListener('mousemove', function (e) { moveTo(e.clientY); });
    canvas.addEventListener('touchmove', function (e) {
      if (e.touches[0]) { moveTo(e.touches[0].clientY); e.preventDefault(); }
    }, { passive: false });
    function onKey(e) {
      if (e.key === 'ArrowUp') { playerY = Math.max(0, playerY - 26); e.preventDefault(); }
      if (e.key === 'ArrowDown') { playerY = Math.min(H - PH, playerY + 26); e.preventDefault(); }
    }
    document.addEventListener('keydown', onKey);
    function reset() {
      you = 0; cpu = 0; youEl.textContent = '0'; cpuEl.textContent = '0';
      playerY = H / 2 - PH / 2; cpuY = H / 2 - PH / 2;
      running = true; serve(Math.random() < 0.5 ? 1 : -1);
      ui.msg.textContent = ''; ui.msg.classList.remove('show');
      cancelAnimationFrame(raf);
      draw();
      raf = requestAnimationFrame(step);
    }
    ui.restart.addEventListener('click', reset);
    reset();
    return function () { running = false; cancelAnimationFrame(raf); document.removeEventListener('keydown', onKey); };
  };

  /* ----------------------------------------------------------------- memory */
  G.memory = function (el) {
    var ui = shell(el);
    var movesEl = ui.stat('Moves', 'memMoves');
    var pairsEl = ui.stat('Pairs', 'memPairs');
    var board = h('div', 'mem-board');
    ui.stage.appendChild(board);
    ui.controls.innerHTML = '<span class="arcade-hint">Flip two cards. Match all eight pairs in as few moves as you can.</span>';
    var ICONS = ['🌊', '🍡', '🛰️', '🎧', '🌿', '🔭', '🎲', '🧭'];
    var first = null, lock = false, moves = 0, matched = 0;

    function reset() {
      var cards = ICONS.concat(ICONS).map(function (icon) {
        return { icon: icon, open: false, done: false };
      });
      for (var i = cards.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var t = cards[i]; cards[i] = cards[j]; cards[j] = t;
      }
      board.innerHTML = '';
      first = null; lock = false; moves = 0; matched = 0;
      movesEl.textContent = '0'; pairsEl.textContent = '0';
      ui.msg.textContent = ''; ui.msg.classList.remove('show');
      cards.forEach(function (card) {
        var btn = h('button', 'mem-card');
        btn.type = 'button';
        btn.setAttribute('aria-label', 'Hidden card');
        btn.innerHTML = '<span>?</span>';
        btn.addEventListener('click', function () { flip(card, btn); });
        card.el = btn;
        board.appendChild(btn);
      });
    }
    function flip(card, btn) {
      if (lock || card.done || card.open) return;
      card.open = true;
      btn.classList.add('is-open');
      btn.querySelector('span').textContent = card.icon;
      sound('click');
      if (!first) { first = card; return; }
      moves += 1;
      movesEl.textContent = String(moves);
      if (first.icon === card.icon) {
        first.done = true; card.done = true;
        first.el.classList.add('is-done');
        card.el.classList.add('is-done');
        first = null;
        matched += 1;
        pairsEl.textContent = String(matched);
        sound('success');
        if (matched === ICONS.length) {
          ui.msg.innerHTML = '<strong>All matched</strong><span>' + moves + ' moves · restart to beat it</span>';
          ui.msg.classList.add('show');
        }
      } else {
        lock = true;
        var a = first;
        setTimeout(function () {
          [a, card].forEach(function (c) {
            c.open = false;
            c.el.classList.remove('is-open');
            c.el.querySelector('span').textContent = '?';
          });
          first = null; lock = false;
        }, 720);
      }
    }
    ui.restart.addEventListener('click', reset);
    reset();
    return function () {};
  };

  /* ------------------------------------------------------------------- mole */
  G.mole = function (el) {
    var ui = shell(el);
    var scoreEl = ui.stat('Score', 'moleScore');
    var timeEl = ui.stat('Time', 'moleTime');
    var board = h('div', 'mole-board');
    ui.stage.appendChild(board);
    ui.controls.innerHTML = '<span class="arcade-hint">Tap the mole. Thirty seconds, and it gets faster.</span>';
    var holes = [], score = 0, left = 30, timer = 0, spawn = 0, active = -1, speed = 760;

    function reset() {
      board.innerHTML = '';
      holes = [];
      score = 0; left = 30; speed = 760; active = -1;
      scoreEl.textContent = '0'; timeEl.textContent = '30s';
      ui.msg.textContent = ''; ui.msg.classList.remove('show');
      for (var i = 0; i < 9; i++) {
        var hole = h('button', 'mole-hole');
        hole.type = 'button';
        hole.setAttribute('aria-label', 'Empty hole');
        hole.innerHTML = '<span>·</span>';
        (function (idx, node) {
          node.addEventListener('click', function () {
            if (idx !== active) return;
            score += 1;
            scoreEl.textContent = String(score);
            node.classList.remove('is-up');
            node.querySelector('span').textContent = '·';
            active = -1;
            sound('success');
          });
        })(i, hole);
        holes.push(hole);
        board.appendChild(hole);
      }
      clearInterval(timer); clearTimeout(spawn);
      timer = setInterval(function () {
        left -= 1;
        timeEl.textContent = left + 's';
        if (left <= 0) end();
      }, 1000);
      pop();
    }
    function pop() {
      if (left <= 0) return;
      if (active >= 0) {
        holes[active].classList.remove('is-up');
        holes[active].querySelector('span').textContent = '·';
      }
      active = Math.floor(Math.random() * 9);
      holes[active].classList.add('is-up');
      holes[active].querySelector('span').textContent = '🐹';
      spawn = setTimeout(function () {
        if (active >= 0) {
          holes[active].classList.remove('is-up');
          holes[active].querySelector('span').textContent = '·';
          active = -1;
        }
        if (speed > 430) speed -= 14;
        pop();
      }, speed);
    }
    function end() {
      clearInterval(timer); clearTimeout(spawn);
      if (active >= 0) { holes[active].classList.remove('is-up'); holes[active].querySelector('span').textContent = '·'; }
      ui.msg.innerHTML = '<strong>Time</strong><span>' + score + ' hits · best ' + best('dih_mole_best', score) + '</span>';
      ui.msg.classList.add('show');
      sound('success');
    }
    ui.restart.addEventListener('click', reset);
    reset();
    return function () { clearInterval(timer); clearTimeout(spawn); };
  };

  /* --------------------------------------------------------------- reaction */
  G.reaction = function (el) {
    var ui = shell(el);
    var lastEl = ui.stat('Last', 'rxLast');
    var bestEl = ui.stat('Best', 'rxBest');
    var triesEl = ui.stat('Tries', 'rxTries');
    var pad = h('button', 'rx-pad', 'Wait for green, then click');
    pad.type = 'button';
    ui.stage.appendChild(pad);
    ui.controls.innerHTML = '<span class="arcade-hint">Five tries. Anything under 250 ms is quick.</span>';
    var state = 'idle', start = 0, timer = 0, tries = 0, total = 0;
    bestEl.textContent = (store('dih_reaction_best') ? store('dih_reaction_best') + ' ms' : '—');

    function reset() {
      state = 'idle'; tries = 0; total = 0;
      triesEl.textContent = '0 / 5';
      pad.className = 'rx-pad';
      pad.textContent = 'Wait for green, then click';
      lastEl.textContent = '—';
      ui.msg.textContent = ''; ui.msg.classList.remove('show');
    }
    pad.addEventListener('click', function () {
      if (state === 'idle') {
        state = 'waiting';
        pad.className = 'rx-pad is-waiting';
        pad.textContent = 'Wait…';
        timer = setTimeout(function () {
          state = 'ready';
          start = performance.now();
          pad.className = 'rx-pad is-ready';
          pad.textContent = 'CLICK!';
          sound('open');
        }, 900 + Math.random() * 2600);
      } else if (state === 'waiting') {
        clearTimeout(timer);
        state = 'idle';
        pad.className = 'rx-pad is-early';
        pad.textContent = 'Too early — click to try again';
        sound('error');
      } else if (state === 'ready') {
        var ms = Math.round(performance.now() - start);
        tries += 1; total += ms;
        lastEl.textContent = ms + ' ms';
        triesEl.textContent = tries + ' / 5';
        var bestTime = Number(store('dih_reaction_best') || 99999);
        if (ms < bestTime) { store('dih_reaction_best', ms); bestEl.textContent = ms + ' ms'; }
        if (tries >= 5) {
          state = 'done';
          pad.className = 'rx-pad';
          pad.textContent = 'Average ' + Math.round(total / 5) + ' ms';
          ui.msg.innerHTML = '<strong>Average ' + Math.round(total / 5) + ' ms</strong><span>Best ' + Math.min.apply(null, [ms, Number(store('dih_reaction_best'))]) + ' ms · restart to run five more</span>';
          ui.msg.classList.add('show');
          sound('success');
        } else {
          state = 'idle';
          pad.className = 'rx-pad';
          pad.textContent = ms + ' ms — click for the next try';
        }
      } else if (state === 'done') {
        reset();
      }
    });
    ui.restart.addEventListener('click', reset);
    reset();
    return function () { clearTimeout(timer); };
  };

  /* ------------------------------------------------------------------ simon */
  G.simon = function (el) {
    var ui = shell(el);
    var levelEl = ui.stat('Level', 'simonLevel');
    var bestEl = ui.stat('Best', 'simonBest');
    var board = h('div', 'simon-board');
    ui.stage.appendChild(board);
    ui.controls.innerHTML = '<span class="arcade-hint">Watch the sequence, then repeat it. One more step each round.</span>';
    var pads = [], seq = [], input = 0, level = 0, busy = false;
    var COLORS = ['#4c8dff', '#f2c94c', '#6ee7a8', '#ff6b9d'];
    bestEl.textContent = store('dih_simon_best') || '0';

    function reset() {
      board.innerHTML = '';
      pads = [];
      seq = []; level = 0; input = 0; busy = false;
      levelEl.textContent = '0';
      ui.msg.textContent = ''; ui.msg.classList.remove('show');
      COLORS.forEach(function (color, i) {
        var pad = h('button', 'simon-pad');
        pad.type = 'button';
        pad.style.setProperty('--pad', color);
        pad.setAttribute('aria-label', 'Pad ' + (i + 1));
        pad.addEventListener('click', function () { tap(i); });
        pads.push(pad);
        board.appendChild(pad);
      });
      setTimeout(next, 500);
    }
    function tone(freq) {
      if (!(window.DIH && window.DIH.sfx && window.DIH.sfx.enabled && window.DIH.sfx.enabled())) return;
      try {
        var AC = window.AudioContext || window.webkitAudioContext;
        if (!AC) return;
        var ac = new AC();
        var osc = ac.createOscillator();
        var amp = ac.createGain();
        osc.frequency.value = freq;
        osc.type = 'sine';
        amp.gain.value = 0.05;
        osc.connect(amp); amp.connect(ac.destination);
        osc.start();
        amp.gain.exponentialRampToValueAtTime(0.0001, ac.currentTime + 0.24);
        osc.stop(ac.currentTime + 0.26);
        setTimeout(function () { ac.close(); }, 400);
      } catch (e) {}
    }
    function flash(i, ms) {
      pads[i].classList.add('is-lit');
      tone([392, 494, 587, 698][i]);
      setTimeout(function () { pads[i].classList.remove('is-lit'); }, ms || 320);
    }
    function next() {
      level += 1;
      levelEl.textContent = String(level);
      seq.push(Math.floor(Math.random() * 4));
      input = 0;
      busy = true;
      seq.forEach(function (step, i) {
        setTimeout(function () { flash(step, 340); }, 520 * i + 300);
      });
      setTimeout(function () { busy = false; }, seq.length * 520 + 400);
    }
    function tap(i) {
      if (busy) return;
      flash(i, 180);
      if (seq[input] !== i) {
        busy = true;
        sound('error');
        ui.msg.innerHTML = '<strong>Wrong pad</strong><span>Level ' + (level - 1) + ' · restart to try again</span>';
        ui.msg.classList.add('show');
        bestEl.textContent = String(best('dih_simon_best', level - 1));
        return;
      }
      input += 1;
      if (input === seq.length) {
        busy = true;
        bestEl.textContent = String(best('dih_simon_best', level));
        setTimeout(next, 700);
      }
    }
    ui.restart.addEventListener('click', reset);
    reset();
    return function () {};
  };

  /* ------------------------------------------------------------- tictactoe */
  G.tictactoe = function (el) {
    var ui = shell(el);
    var statusEl = h('div', 'arcade-status', 'You are X. It is your move.');
    ui.stats.appendChild(statusEl);
    var board = h('div', 'ttt-board');
    ui.stage.appendChild(board);
    ui.controls.innerHTML = '<span class="arcade-hint">You are X. The hub plays O and does not lose.</span>';
    var cells = [], state = ['', '', '', '', '', '', '', '', ''], over = false;

    function reset() {
      state = ['', '', '', '', '', '', '', '', ''];
      over = false;
      statusEl.textContent = 'You are X. It is your move.';
      board.innerHTML = '';
      cells = [];
      state.forEach(function (_, i) {
        var b = h('button', 'ttt-cell');
        b.type = 'button';
        b.setAttribute('aria-label', 'Square ' + (i + 1));
        b.addEventListener('click', function () { play(i); });
        cells.push(b);
        board.appendChild(b);
      });
      ui.msg.textContent = ''; ui.msg.classList.remove('show');
    }
    function winner(s) {
      var lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
      for (var i = 0; i < lines.length; i++) {
        var l = lines[i];
        if (s[l[0]] && s[l[0]] === s[l[1]] && s[l[1]] === s[l[2]]) return s[l[0]];
      }
      return s.indexOf('') === -1 ? 'draw' : '';
    }
    function play(i) {
      if (over || state[i]) return;
      state[i] = 'X';
      paint();
      var result = winner(state);
      if (result) return finish(result);
      over = true;
      statusEl.textContent = 'Thinking…';
      setTimeout(function () { ai(); }, 240);
    }
    function ai() {
      var bestScore = -Infinity, move = -1;
      for (var i = 0; i < 9; i++) {
        if (!state[i]) {
          state[i] = 'O';
          var score = minimax(state, 0, false);
          state[i] = '';
          if (score > bestScore) { bestScore = score; move = i; }
        }
      }
      if (move >= 0) state[move] = 'O';
      paint();
      over = false;
      var result = winner(state);
      if (result) return finish(result);
      statusEl.textContent = 'Your move.';
    }
    function minimax(s, depth, maximizing) {
      var result = winner(s);
      if (result === 'O') return 10 - depth;
      if (result === 'X') return depth - 10;
      if (result === 'draw') return 0;
      if (maximizing) {
        var bestV = -Infinity;
        for (var i = 0; i < 9; i++) if (!s[i]) {
          s[i] = 'O'; bestV = Math.max(bestV, minimax(s, depth + 1, false)); s[i] = '';
        }
        return bestV;
      }
      var low = Infinity;
      for (var j = 0; j < 9; j++) if (!s[j]) {
        s[j] = 'X'; low = Math.min(low, minimax(s, depth + 1, true)); s[j] = '';
      }
      return low;
    }
    function paint() {
      state.forEach(function (v, i) {
        cells[i].textContent = v;
        cells[i].classList.toggle('is-x', v === 'X');
        cells[i].classList.toggle('is-o', v === 'O');
      });
    }
    function finish(result) {
      over = true;
      statusEl.textContent = result === 'draw' ? 'Draw.' : result === 'X' ? 'You win!' : 'The hub wins.';
      ui.msg.innerHTML = result === 'X'
        ? '<strong>You win</strong><span>Careful play beats a perfect defence. Restart for another.</span>'
        : result === 'draw'
          ? '<strong>Draw</strong><span>That is the best result against perfect play.</span>'
          : '<strong>The hub wins</strong><span>Try the centre first next time.</span>';
      ui.msg.classList.add('show');
      sound(result === 'X' ? 'success' : result === 'draw' ? 'click' : 'error');
    }
    ui.restart.addEventListener('click', reset);
    reset();
    return function () {};
  };

  /* ----------------------------------------------------------------- typing */
  G.typing = function (el) {
    var ui = shell(el);
    var wpmEl = ui.stat('WPM', 'typeWpm');
    var accEl = ui.stat('Accuracy', 'typeAcc');
    var timeEl = ui.stat('Time', 'typeTime');
    var passage = h('div', 'type-passage');
    ui.stage.appendChild(passage);
    var input = h('textarea', 'type-input');
    input.rows = 3;
    input.setAttribute('aria-label', 'Type the passage here');
    input.placeholder = 'Start typing… the timer starts on your first key.';
    ui.stage.appendChild(input);
    ui.controls.innerHTML = '<span class="arcade-hint">60 seconds. The timer starts with your first keystroke.</span>';
    var TEXT = 'Clear tools beat clever tools. A page that loads fast, answers one question and gets out of the way is worth more than a dashboard nobody opens. Keep the words short, the numbers honest and the next step obvious. That is how a digital place becomes a habit, and how a habit becomes a home for curious people who want to understand the world without being talked down to.';
    var started = false, left = 60, timer = 0, typedChars = 0, correct = 0;

    function reset() {
      clearInterval(timer);
      started = false; left = 60; typedChars = 0; correct = 0;
      input.value = '';
      wpmEl.textContent = '0'; accEl.textContent = '100%'; timeEl.textContent = '60s';
      ui.msg.textContent = ''; ui.msg.classList.remove('show');
      paint('');
    }
    function paint(value) {
      var i = 0;
      passage.innerHTML = TEXT.split('').map(function (ch, idx) {
        var cls = 'type-ch';
        if (idx < value.length) cls += value[idx] === ch ? ' is-ok' : ' is-bad';
        return '<span class="' + cls + '">' + (ch === ' ' ? '&nbsp;' : esc(ch)) + '</span>';
      }).join('');
    }
    function stats() {
      var minutes = (60 - left) / 60;
      var wpm = minutes > 0 ? Math.round((typedChars / 5) / minutes) : 0;
      wpmEl.textContent = String(wpm);
      accEl.textContent = typedChars ? Math.round((correct / typedChars) * 100) + '%' : '100%';
    }
    input.addEventListener('input', function () {
      if (!started) {
        started = true;
        timer = setInterval(function () {
          left -= 1;
          timeEl.textContent = left + 's';
          stats();
          if (left <= 0) end();
        }, 1000);
      }
      var value = input.value;
      typedChars = value.length;
      correct = 0;
      for (var i = 0; i < value.length; i++) if (value[i] === TEXT[i]) correct += 1;
      paint(value);
      stats();
      if (value.length >= TEXT.length) end();
    });
    function end() {
      clearInterval(timer);
      input.disabled = true;
      var minutes = Math.max(1 / 60, (60 - left) / 60);
      var wpm = Math.round((typedChars / 5) / minutes);
      ui.msg.innerHTML = '<strong>' + wpm + ' WPM</strong><span>' + (typedChars ? Math.round((correct / typedChars) * 100) : 0) + '% accurate · restart for another run</span>';
      ui.msg.classList.add('show');
      sound('success');
    }
    ui.restart.addEventListener('click', function () { input.disabled = false; reset(); input.focus(); });
    reset();
    return function () { clearInterval(timer); };
  };

  window.Arcade = {
    mount: function (name, el) {
      if (!G[name]) return null;
      return G[name](el);
    },
    names: Object.keys(G)
  };
})();
