#!/usr/bin/env python3
"""Assemble /games from the shared site chrome and _arcade/games-body.html.

Digital Infohub games come first and every cabinet links to its own page in a
new tab; Random Ryan Digital sits last with the "another way to play" context.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURRENT = (ROOT / "games.html").read_text(encoding="utf-8")
HEADER = CURRENT[CURRENT.index("<!-- DIH:HEADER -->"): CURRENT.index("<!-- /DIH:HEADER -->") + len("<!-- /DIH:HEADER -->")]
FOOTER = CURRENT[CURRENT.index("<!-- DIH:FOOTER -->"): CURRENT.index("<!-- /DIH:FOOTER -->") + len("<!-- /DIH:FOOTER -->")]
BODY = (ROOT / "_arcade" / "games-body.html").read_text(encoding="utf-8")

TITLE = "Free Browser Games — Pixel Palace Arcade | Digital Infohub"
DESC = ("Twelve free browser games from Digital Infohub: Block Defender, Neon Horizon, Perfect Pour, Snake, 2048 and more. "
        "Each opens on its own page.")
URL = "https://digitalinfohub.net/games"

head = f"""<!DOCTYPE html>
<html lang="en" data-dih="">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<meta name="keywords" content="free browser games, online arcade, block defender, neon horizon, perfect pour, snake, 2048, digital infohub">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5443646750699471" crossorigin="anonymous"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="/assets/hub.css?v=20261202">
<link rel="canonical" href="{URL}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Digital Infohub">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="https://images.unsplash.com/photo-1511512578047-dfb367046420?w=1200&amp;h=630&amp;fit=crop&amp;auto=format&amp;q=80&amp;fm=jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{TITLE}">
<meta name="twitter:description" content="{DESC}">
<meta name="theme-color" content="#07060f">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon-16.png">
<link rel="icon" href="/assets/favicon.ico" sizes="any">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<script>try{{var t=localStorage.getItem('dih_theme')||'dark';document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
</head>
<body>
"""

page = (
    head
    + HEADER
    + '\n<div class="dih-ambient" aria-hidden="true"><i></i><i></i><i></i></div>\n'
    + BODY
    + '\n'
    + FOOTER
    + '\n<script src="/assets/site.js" defer></script>\n</body>\n</html>\n'
)
(ROOT / "games.html").write_text(page, encoding="utf-8")
print("wrote games.html", len(page), "bytes")
