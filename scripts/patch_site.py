#!/usr/bin/env python3
"""Apply the shared chrome upgrades and copy clean-up to every static page.

Idempotent. Adds the terminal + sound controls to the header, the terminal
links to the drawer and footer, and replaces "clear English / clear"
phrasing with clearer wording across pages, post sources and generators.

Usage:
  python3 scripts/patch_site.py --dry-run
  python3 scripts/patch_site.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {".git", "node_modules", "post", "assets"}

REPLACEMENTS = [
    ("plain-language", "clear"),
    ("Plain-language", "Clear"),
    ("Plain-Language", "Clear"),
    ("plain language", "clear language"),
    ("Plain language", "Clear language"),
    ("Plain Language", "Clear Language"),
    ("plain-English", "clear"),
    ("Plain-English", "Clear"),
    ("plain English", "clear English"),
    ("Plain English", "Clear English"),
    ("plain english", "clear English"),
    ("in plain words", "in clear words"),
    ("Plainly explained", "Clearly explained"),
    ("plainly explained", "clearly explained"),
]

# Never rewrite this file (it would erase the rules above).
NEVER_PATCH = {Path(__file__).resolve()}

HEADER_MARK = "dih-term"
HEADER_ANCHOR = (
    '      <a class="dih-tools" href="/software#tools" title="Free browser tools" '
    'aria-label="Free browser tools">⚡<span>Tools</span></a>\n'
)
HEADER_ADD = (
    '      <a class="dih-icon dih-term" href="/terminal" title="Terminal mode — browse like a shell" '
    'aria-label="Open terminal mode">⌨<span class="dih-term-txt">Terminal</span></a>\n'
    '      <button class="dih-icon dih-sound" type="button" data-dih-sound aria-label="Sound on — tap to mute" '
    'aria-pressed="true" title="Sound on — tap to mute (Shift+S)">🔊</button>\n'
)

DRAWER_ANCHOR = '      <a class="dih-drawer-link" href="/contact">✉️ Contact</a>\n'
DRAWER_ADD = (
    '      <a class="dih-drawer-link" href="/terminal">⌨️ Terminal mode</a>\n'
    '      <a class="dih-drawer-link" href="/terminal#top">📊 Most opened pages</a>\n'
)

FOOTER_ANCHOR = '      <a href="/sitemap.xml">Sitemap</a>\n'
FOOTER_ADD = '      <a href="/terminal">Terminal</a>\n'


def html_files():
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        yield path


def text_files():
    """Post pages and sources plus shared scripts, so a rebuild keeps the wording."""
    for pattern in ("_posts/*.json", "scripts/*.py", "post/*.html", "assets/*.js"):
        for path in sorted(ROOT.glob(pattern)):
            if path.resolve() in NEVER_PATCH:
                continue
            yield path


def patch_html(path: Path, dry: bool):
    raw = path.read_text(encoding="utf-8", errors="ignore")
    html = raw
    notes = []

    head_block = html.split("<!-- /DIH:HEADER -->")[0]
    if HEADER_MARK not in head_block and HEADER_ANCHOR in html:
        html = html.replace(HEADER_ANCHOR, HEADER_ANCHOR + HEADER_ADD, 1)
        notes.append("header")

    if 'href="/terminal"' not in html.split("</div>\n<!-- /DIH:HEADER -->")[0] and DRAWER_ANCHOR in html:
        html = html.replace(DRAWER_ANCHOR, DRAWER_ANCHOR + DRAWER_ADD, 1)
        notes.append("drawer")

    if 'href="/terminal">Terminal</a>' not in html and FOOTER_ANCHOR in html:
        html = html.replace(FOOTER_ANCHOR, FOOTER_ANCHOR + FOOTER_ADD, 1)
        notes.append("footer")

    changes = 0
    for old, new in REPLACEMENTS:
        if old in html:
            changes += html.count(old)
            html = html.replace(old, new)
    if changes:
        notes.append(f"copy×{changes}")

    if html != raw:
        if not dry:
            path.write_text(html, encoding="utf-8")
        return notes
    return []


def patch_text(path: Path, dry: bool):
    raw = path.read_text(encoding="utf-8", errors="ignore")
    html = raw
    changes = 0
    for old, new in REPLACEMENTS:
        if old in html:
            changes += html.count(old)
            html = html.replace(old, new)
    if html != raw:
        if not dry:
            path.write_text(html, encoding="utf-8")
        return changes
    return 0


def main():
    dry = "--dry-run" in sys.argv
    touched = 0
    copy_hits = 0
    for path in html_files():
        notes = patch_html(path, dry)
        if notes:
            touched += 1
            copy_hits += sum(int(n.split("×")[1]) for n in notes if n.startswith("copy×"))
            print(f"{'would patch' if dry else 'patched'} {path.relative_to(ROOT)}: {', '.join(notes)}")
    for path in text_files():
        hits = patch_text(path, dry)
        if hits:
            copy_hits += hits
            print(f"{'would patch' if dry else 'patched'} {path.relative_to(ROOT)}: copy×{hits}")
    print(f"\n{touched} pages, {copy_hits} copy replacements")


if __name__ == "__main__":
    main()
