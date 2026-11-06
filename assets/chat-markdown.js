/* Digital Infohub — small, dependency-free markdown renderer.
 * Used by the homepage assistant and the Pollinations chat tools so tables,
 * lists, headings and code blocks render as real HTML instead of raw pipes.
 * All text is escaped first; only a small allowlist of links is emitted.
 */
(function () {
  'use strict';

  function escapeHtml(value) {
    return String(value == null ? '' : value).replace(/[&<>"']/g, function (ch) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[ch];
    });
  }

  function safeHref(raw) {
    var url = String(raw || '').trim();
    if (/^(https?:\/\/|\/|#|mailto:)/i.test(url)) return escapeHtml(url);
    return '';
  }

  var codeStore = [];

  function inline(text) {
    var value = escapeHtml(text);
    codeStore = [];

    // Protect inline code before applying emphasis/link rules.
    value = value.replace(/`([^`\n]+)`/g, function (_, code) {
      var token = '\u0000C' + codeStore.length + '\u0000';
      codeStore.push('<code>' + code + '</code>');
      return token;
    });

    value = value.replace(/\[([^\]\n]+)\]\(([^)\s]+)\)/g, function (_, label, href) {
      var url = safeHref(href);
      if (!url) return label;
      var external = /^https?:\/\//i.test(href);
      return '<a href="' + url + '"' + (external ? ' target="_blank" rel="noopener noreferrer"' : '') + '>' + label + '</a>';
    });

    value = value.replace(/\*\*([^*\n]+)\*\*/g, '<strong>$1</strong>');
    value = value.replace(/__([^_\n]+)__/g, '<strong>$1</strong>');
    value = value.replace(/~~([^~\n]+)~~/g, '<del>$1</del>');
    value = value.replace(/(^|[\s(])\*([^*\n]+)\*(?=$|[\s).,!?:;])/g, '$1<em>$2</em>');
    value = value.replace(/(^|[\s(])_([^_\n]+)_(?=$|[\s).,!?:;])/g, '$1<em>$2</em>');

    value = value.replace(/\u0000C(\d+)\u0000/g, function (_, index) {
      return codeStore[Number(index)] || '';
    });

    return value;
  }

  function splitRow(line) {
    var trimmed = String(line || '').trim().replace(/^\|/, '').replace(/\|$/, '');
    var cells = [];
    var current = '';
    for (var i = 0; i < trimmed.length; i++) {
      var ch = trimmed[i];
      if (ch === '\\' && trimmed[i + 1] === '|') {
        current += '|';
        i++;
      } else if (ch === '|') {
        cells.push(current.trim());
        current = '';
      } else {
        current += ch;
      }
    }
    cells.push(current.trim());
    return cells;
  }

  function isTableSeparator(line) {
    var cells = splitRow(line);
    if (!cells.length || cells.length < 1) return false;
    return cells.every(function (cell) {
      return /^:?-{3,}:?$/.test(cell.replace(/\s+/g, ''));
    });
  }

  function alignment(cell) {
    var left = /^:/.test(cell);
    var right = /:$/.test(cell);
    if (left && right) return 'center';
    if (right) return 'right';
    if (left) return 'left';
    return '';
  }

  function renderTable(headerLine, separatorLine, rows) {
    var headers = splitRow(headerLine);
    var separators = splitRow(separatorLine);
    var aligns = headers.map(function (_, i) { return alignment(separators[i] || ''); });
    var head = '<thead><tr>' + headers.map(function (cell, i) {
      var style = aligns[i] ? ' style="text-align:' + aligns[i] + '"' : '';
      return '<th' + style + '>' + inline(cell) + '</th>';
    }).join('') + '</tr></thead>';
    var body = rows.map(function (row) {
      var cells = splitRow(row);
      return '<tr>' + headers.map(function (_, i) {
        var style = aligns[i] ? ' style="text-align:' + aligns[i] + '"' : '';
        return '<td' + style + '>' + inline(cells[i] || '') + '</td>';
      }).join('') + '</tr>';
    }).join('');
    return '<div class="md-table-wrap"><table class="md-table">' + head + (body ? '<tbody>' + body + '</tbody>' : '') + '</table></div>';
  }

  function isBlockStart(line) {
    return /^\s*(#{1,6}\s|```|~~~|>\s?|[-*+]\s+|\d+[.)]\s+|---+\s*$|\*\*\*\s*$|___+\s*$)/.test(line);
  }

  function render(text) {
    var lines = String(text == null ? '' : text).replace(/\r\n?/g, '\n').split('\n');
    var out = [];
    var i = 0;

    while (i < lines.length) {
      var line = lines[i];

      if (!line.trim()) { i++; continue; }

      var fence = line.match(/^\s*(```|~~~)\s*([\w-]*)\s*$/);
      if (fence) {
        var marker = fence[1];
        var lang = fence[2] || '';
        var codeLines = [];
        i++;
        while (i < lines.length && !new RegExp('^\\s*' + marker + '\\s*$').test(lines[i])) {
          codeLines.push(lines[i]);
          i++;
        }
        if (i < lines.length) i++;
        out.push('<pre class="md-pre"><code' + (lang ? ' class="language-' + escapeHtml(lang) + '"' : '') + '>' + escapeHtml(codeLines.join('\n')) + '</code></pre>');
        continue;
      }

      if (line.indexOf('|') !== -1 && i + 1 < lines.length && isTableSeparator(lines[i + 1])) {
        var tableRows = [];
        var j = i + 2;
        while (j < lines.length && lines[j].trim() && lines[j].indexOf('|') !== -1) {
          tableRows.push(lines[j]);
          j++;
        }
        out.push(renderTable(line, lines[i + 1], tableRows));
        i = j;
        continue;
      }

      var heading = line.match(/^\s*(#{1,6})\s+(.*?)\s*#*\s*$/);
      if (heading) {
        var level = heading[1].length;
        out.push('<h' + level + '>' + inline(heading[2]) + '</h' + level + '>');
        i++;
        continue;
      }

      if (/^\s*(---+|\*\*\*+|___+)\s*$/.test(line)) {
        out.push('<hr>');
        i++;
        continue;
      }

      if (/^\s*>\s?/.test(line)) {
        var quote = [];
        while (i < lines.length && /^\s*>\s?/.test(lines[i])) {
          quote.push(lines[i].replace(/^\s*>\s?/, ''));
          i++;
        }
        out.push('<blockquote>' + inline(quote.join('\n')).replace(/\n/g, '<br>') + '</blockquote>');
        continue;
      }

      var ul = line.match(/^\s*[-*+]\s+(.*)$/);
      var ol = line.match(/^\s*\d+[.)]\s+(.*)$/);
      if (ul || ol) {
        var ordered = !!ol;
        var items = [];
        while (i < lines.length) {
          var m = ordered ? lines[i].match(/^\s*\d+[.)]\s+(.*)$/) : lines[i].match(/^\s*[-*+]\s+(.*)$/);
          if (!m) break;
          var item = m[1];
          var task = item.match(/^\[([ xX])\]\s+(.*)$/);
          if (task) {
            items.push('<li class="md-task"><input type="checkbox" disabled' + (task[1].toLowerCase() === 'x' ? ' checked' : '') + '> ' + inline(task[2]) + '</li>');
          } else {
            items.push('<li>' + inline(item) + '</li>');
          }
          i++;
        }
        out.push('<' + (ordered ? 'ol' : 'ul') + '>' + items.join('') + '</' + (ordered ? 'ol' : 'ul') + '>');
        continue;
      }

      var para = [line];
      i++;
      while (i < lines.length && lines[i].trim() && !isBlockStart(lines[i])) {
        para.push(lines[i]);
        i++;
      }
      out.push('<p>' + inline(para.join('\n')).replace(/\n/g, '<br>') + '</p>');
    }

    return out.join('');
  }

  window.dihMarkdown = render;
  window.dihEscapeHtml = escapeHtml;
})();
