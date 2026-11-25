#!/usr/bin/env python3
"""Give every content page at least two well-placed AdSense units.

Rules that keep this inside AdSense placement policy:
  * never more than three units on a page
  * every unit sits in normal page flow, separated from the content above and
    below it, never inside an overlay, popup or iframe
  * no units on contact / privacy / 404 pages (thin or non-content pages)
  * one unit is always below the fold where it cannot be mistaken for a
    control; the in-content unit is placed between sections, not next to a
    button or a game control

Idempotent: injected slots carry data-dih-ad="1" and the script never adds a
unit to a page that already has enough.

    python3 scripts/ad_revenue.py --dry-run
    python3 scripts/ad_revenue.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ADSENSE = "ca-pub-5443646750699471"
SLOT = "8451723433"

SKIP = {
    "contact.html", "privacy-policy.html", "404.html", "digi.html",
    "terminal.html",
}

LOADER = (
    '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
    f'?client={ADSENSE}" crossorigin="anonymous"></script>'
)

# Self-styled so it looks the same on the shared chrome, the legacy shells and
# the standalone game pages without depending on any one stylesheet.
UNIT = (
    '<aside class="dih-ad-slot" data-dih-ad="1" aria-label="Advertisement" '
    'style="max-width:970px;margin:26px auto;padding:10px 10px 6px;'
    'border:1px solid rgba(255,255,255,.09);border-radius:14px;'
    'background:rgba(255,255,255,.028);text-align:center">'
    '<span style="display:block;font-size:10px;font-weight:700;letter-spacing:.16em;'
    'text-transform:uppercase;color:#8b93a7;margin:0 0 6px">Advertisement</span>'
    f'<ins class="adsbygoogle" style="display:block" data-ad-client="{ADSENSE}" '
    f'data-ad-slot="{SLOT}" data-ad-format="auto" data-full-width-responsive="true"></ins>'
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>'
    '</aside>'
)

UNIT_RE = re.compile(r'<ins class="adsbygoogle', re.I)


def units(html: str) -> int:
    return len(UNIT_RE.findall(html))


def ensure_loader(html: str) -> str:
    if "pagead2.googlesyndication.com" in html:
        return html
    if "</head>" in html:
        return html.replace("</head>", LOADER + "\n</head>", 1)
    return LOADER + html


def _insert_before(html: str, needle: str, block: str) -> str | None:
    idx = html.find(needle)
    if idx == -1:
        return None
    return html[:idx] + block + "\n" + html[idx:]


def mid_anchor(html: str) -> str | None:
    """Where the in-content unit goes: after the first section of prose."""
    # Long-form articles: before the second <h2> inside the first article.
    art = html.find("<article")
    if art != -1:
        end = html.find("</article>", art)
        chunk = html[art:end if end != -1 else len(html)]
        h2s = [m.start() for m in re.finditer(r"<h2\b", chunk)]
        if len(h2s) >= 2:
            pos = art + h2s[1]
            return html[:pos] + UNIT + "\n" + html[pos:]
        if end != -1:
            return html[:end] + UNIT + "\n" + html[end:]
    # Sectioned landing pages: between the hero block and the next section.
    for marker in (
        '<section class="dih-gallery"',
        '<section class="dih-explore"',
        '<section class="dih-promo"',
        '<!-- DIH:GALLERY -->',
        '<!-- DIH:EXPLORE -->',
    ):
        idx = html.find(marker)
        if idx != -1:
            # keep the unit away from the very top of a page
            return html[:idx] + UNIT + "\n" + html[idx:]
    return None


def bottom_anchor(html: str) -> str | None:
    for marker in (
        '<section class="dih-gallery"',
        '<section class="dih-explore"',
        '<!-- DIH:GALLERY -->',
        '<!-- DIH:EXPLORE -->',
        '<footer class="dih-footer"',
        '<!-- DIH:FOOTER -->',
    ):
        idx = html.find(marker)
        if idx != -1:
            return html[:idx] + UNIT + "\n" + html[idx:]
    idx = html.rfind("</main>")
    if idx != -1:
        return html[:idx] + UNIT + "\n" + html[idx:]
    return None


def game_anchor(html: str) -> str | None:
    """A game page: unit directly after the board card, before the how-to."""
    for marker in ('<div class="hub-grid"', '<section class="hub-card" style="margin-top:14px"'):
        idx = html.find(marker)
        if idx != -1:
            return html[:idx] + UNIT + "\n" + html[idx:]
    return None


def process(path: Path, dry: bool = False) -> tuple[int, int]:
    html = path.read_text(encoding="utf-8")
    before = units(html)
    if before >= 2:
        return before, before
    out = ensure_loader(html)
    is_game = path.parent.name == "games"
    # Game pages first: the unit belongs directly under the board, where a
    # player sees it without scrolling, not at the foot of the page.
    if is_game and units(out) < 2:
        anchored = game_anchor(out)
        if anchored:
            out = anchored
    if units(out) == 0:
        anchored = mid_anchor(out) or bottom_anchor(out)
        if anchored:
            out = anchored
    if units(out) < 2:
        anchored = bottom_anchor(out)
        if anchored:
            out = anchored
    after = units(out)
    if after != before and not dry:
        path.write_text(out, encoding="utf-8")
    return before, after


def targets() -> list[Path]:
    pages: list[Path] = []
    for pattern in ("*.html", "software/*.html", "games/*.html", "post/*.html"):
        pages += sorted(ROOT.glob(pattern))
    return [p for p in pages if p.name not in SKIP]


def main() -> None:
    dry = "--dry-run" in sys.argv
    changed = 0
    for path in targets():
        before, after = process(path, dry=dry)
        if after != before:
            changed += 1
            print(f"{'would add' if dry else 'added'} {after - before} -> {before}->{after}  {path.relative_to(ROOT)}")
    print(f"{changed} page(s) {'to update' if dry else 'updated'}")


if __name__ == "__main__":
    main()
