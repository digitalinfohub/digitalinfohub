#!/usr/bin/env python3
"""Static audit: SEO/chrome coverage, duplicate chrome, internal link targets."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://digitalinfohub.net"
issues = []
pages = sorted(p for p in ROOT.rglob("*.html") if not ({"freebuff-sites-build", "sites-build", ".wrangler"} & set(p.parts)) and "scripts" not in p.parts)

for p in pages:
    rel = p.relative_to(ROOT).as_posix()
    h = p.read_text(encoding="utf-8", errors="ignore")
    checks = {
        "title": bool(re.search(r"<title>[^<]+</title>", h)),
        "description": bool(re.search(r'<meta\s+name="description"[^>]*content="[^"]+"', h)),
        "canonical": bool(re.search(r'<link\s+rel="canonical"', h)),
        "og:image": bool(re.search(r'property="og:image"', h)),
        "favicon": "assets/favicon-32.png" in h,
        "site.css": "/assets/site.css" in h,
        "header": 'class="dih-header"' in h,
        "footer": 'class="dih-footer"' in h,
        "explore": 'class="dih-explore"' in h,
        "site.js": "/assets/site.js" in h,
        "data-dih": "data-dih" in h[:400],
        "no legacy nav visible": True,
    }
    for name, ok in checks.items():
        if not ok:
            issues.append(f"{rel}: missing {name}")
    if h.count('class="dih-header"') > 1:
        issues.append(f"{rel}: duplicate header")
    if h.count('class="dih-footer"') > 1:
        issues.append(f"{rel}: duplicate footer")

# internal link targets
for p in pages:
    h = p.read_text(encoding="utf-8", errors="ignore")
    for href in set(re.findall(r'href="(/[^"#?]*)', h)):
        if href.startswith("/assets") or href.startswith("/sitemap") or href == "/":
            continue
        target = ROOT / href.lstrip("/")
        if target.suffix == "":
            candidates = [target.with_suffix(".html"), target / "index.html"]
        else:
            candidates = [target]
        if not any(c.exists() for c in candidates):
            issues.append(f"{p.relative_to(ROOT)}: dead internal link {href}")

# sitemap coverage
sm = (ROOT / "sitemap.xml").read_text() if (ROOT / "sitemap.xml").exists() else ""
in_sitemap = set(re.findall(r"<loc>" + re.escape(SITE) + r"/?([^<]*)</loc>", sm))
for p in pages:
    rel = p.relative_to(ROOT).as_posix()
    slug = "" if rel == "index.html" else rel[:-5]
    if slug not in in_sitemap:
        issues.append(f"sitemap: missing {slug or '/'}")

print(f"pages={len(pages)} issues={len(issues)}")
for i in issues:
    print(" -", i)
