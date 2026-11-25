#!/usr/bin/env python3
"""Publish the three standalone arcade games exactly as designed.

Each game lives in _arcade/<slug>.full.html as a complete, self-contained
document (own fonts, canvas/Three.js, audio, HUD and controls). This script only
swaps in the site's titles and invisible SEO tags, then writes games/<slug>.html.
No site chrome or stylesheet is injected, so the game layout is untouched.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

GAMES = [
    {
        "slug": "block-defender",
        "name": "Block Defender",
        "title": "Block Defender — Cyber Block Defense | Digital Infohub",
        "desc": "Play Block Defender free: a five-sector neon block defense game with glitch bugs, saboteur drones, power cells and laser, EMP, freeze and purify upgrades.",
        "genre": "Puzzle",
        "keywords": "block defender, falling blocks game, browser puzzle game, neon arcade, free online game",
    },
    {
        "slug": "neon-horizon",
        "name": "Neon Horizon",
        "title": "Neon Horizon: 3D Highway Racer | Digital Infohub",
        "desc": "Play Neon Horizon free: a 3D neon highway racer built with Three.js. Weave through traffic, grab fuel cans and chase a high score across the synthwave horizon.",
        "genre": "Racing",
        "keywords": "neon horizon, highway racer, 3d driving game, browser racing game, endless racer",
    },
    {
        "slug": "perfect-pour",
        "name": "Perfect Pour",
        "title": "Perfect Pour — Make Coffee Perfectly | Digital Infohub",
        "desc": "Play Perfect Pour free: hold to pour espresso into five cups, stop inside the green target zone and chase three stars without spilling a drop.",
        "genre": "Skill",
        "keywords": "perfect pour, coffee game, pouring game, browser skill game, free online game",
    },
]

SITE = "https://digitalinfohub.net"
OG_IMAGE = "https://images.unsplash.com/photo-1644088379091-d574269d422f?w=1200&h=630&fit=crop&auto=format&q=80&fm=jpg"

LD = (
    '{"@context":"https://schema.org","@type":"VideoGame","name":"%s",'
    '"url":"%s/games/%s","description":"%s",'
    '"genre":"%s","gamePlatform":"Web browser","playMode":"SinglePlayer",'
    '"applicationCategory":"Game","operatingSystem":"Any",'
    '"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"inLanguage":"en",'
    '"publisher":{"@type":"Organization","name":"Digital Infohub","url":"%s"},'
    '"isPartOf":{"@type":"WebSite","name":"Digital Infohub","url":"%s"}}'
)


def build(game):
    slug = game["slug"]
    url = f"{SITE}/games/{slug}"
    doc = (ROOT / "_arcade" / (slug + ".full.html")).read_text(encoding="utf-8")

    # Replace the game's own <title> with the site title.
    doc, n = re.subn(r"<title>.*?</title>", lambda m: "<title>%s</title>" % game["title"], doc, count=1, flags=re.S | re.I)
    if n != 1:
        raise SystemExit(f"{slug}: no <title> found")

    meta = [
        '<meta name="description" content="%s">' % game["desc"],
        '<meta name="keywords" content="%s">' % game["keywords"],
        '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">',
        '<link rel="canonical" href="%s">' % url,
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Digital Infohub">',
        '<meta property="og:title" content="%s">' % game["title"],
        '<meta property="og:description" content="%s">' % game["desc"],
        '<meta property="og:url" content="%s">' % url,
        '<meta property="og:image" content="%s">' % OG_IMAGE,
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:title" content="%s">' % game["title"],
        '<meta name="twitter:description" content="%s">' % game["desc"],
        '<meta name="twitter:image" content="%s">' % OG_IMAGE,
        '<script type="application/ld+json">%s</script>'
        % (LD % (game["name"], SITE, slug, game["desc"], game["genre"], SITE, SITE)),
    ]

    doc = doc.replace("</title>", "</title>\n" + "\n".join(meta), 1)

    out = ROOT / "games" / (slug + ".html")
    out.write_text(doc, encoding="utf-8")
    print("wrote", out.relative_to(ROOT), len(doc), "bytes")


if __name__ == "__main__":
    for game in GAMES:
        build(game)
