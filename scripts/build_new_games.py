#!/usr/bin/env python3
"""Publish the three standalone arcade games exactly as designed.

Each game lives in _arcade/<slug>.full.html as a complete, self-contained
document (own fonts, canvas/Three.js, audio, HUD and controls). This script only
swaps in the site's titles and invisible SEO tags, adds the AdSense loader and
two ad units (start screen and end screen), then writes games/<slug>.html.
No site chrome or stylesheet is injected, so the game layout is untouched.

The end-screen unit is created lazily the first time the game-over or victory
screen appears: AdSense will not render an <ins> that was hidden at load, and
mounting on demand also guarantees one impression per finished run.
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
        "ad_anchor": '<button class="primary-btn" id="startBtn">INITIALIZE SYSTEM</button>',
        "ad_css": "@media (max-height:900px){#mainOverlay{justify-content:flex-start;overflow-y:auto}}",
        "ad_light": False,
        "end_mounts": [{"id": "dihEndAd", "after_start_ad": True}],
        "end_hooks": [("mainOverlay.classList.remove('hidden');", 2, "dihEndAd")],
    },
    {
        "slug": "neon-horizon",
        "name": "Neon Horizon",
        "title": "Neon Horizon: 3D Highway Racer | Digital Infohub",
        "desc": "Play Neon Horizon free: a 3D neon highway racer built with Three.js. Weave through traffic, grab fuel cans and chase a high score across the synthwave horizon.",
        "genre": "Racing",
        "keywords": "neon horizon, highway racer, 3d driving game, browser racing game, endless racer",
        "ad_anchor": "Start Engine\n            </button>",
        "ad_css": "#start-screen>div{max-height:calc(100dvh - 2rem);overflow-y:auto}#gameover-screen>.hud-glass{max-height:calc(100dvh - 2rem);overflow-y:auto}",
        "ad_light": False,
        "end_mounts": [{"id": "dihEndAd", "before": '<button id="btn-restart"'}],
        "end_hooks": [("dom.gameoverScreen.classList.add('flex');", 1, "dihEndAd")],
    },
    {
        "slug": "perfect-pour",
        "name": "Perfect Pour",
        "title": "Perfect Pour — Make Coffee Perfectly | Digital Infohub",
        "desc": "Play Perfect Pour free: hold to pour espresso into five cups, stop inside the green target zone and chase three stars without spilling a drop.",
        "genre": "Skill",
        "keywords": "perfect pour, coffee game, pouring game, browser skill game, free online game",
        "ad_anchor": '<button class="btn-primary" id="btn-start-game">Start Brewing</button>',
        "ad_css": "#start-overlay .modal-card,#result-overlay .modal-card,#victory-overlay .modal-card{max-height:calc(100dvh - 2rem);overflow-y:auto}",
        "ad_light": True,
        "end_mounts": [
            {"id": "dihEndAd", "before": '<button class="btn-primary mint" id="btn-result-action">'},
            {"id": "dihEndAdWin", "before": '<button class="btn-primary" id="btn-play-again">'},
        ],
        "end_hooks": [
            ("resultOverlay.classList.add('visible');", 1, "dihEndAd"),
            ("victoryOverlay.classList.add('visible');", 1, "dihEndAdWin"),
        ],
    },
]

SITE = "https://digitalinfohub.net"

ADSENSE_LOADER = (
    '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
    '?client=ca-pub-5443646750699471" crossorigin="anonymous"></script>'
)

AD_CSS = (
    ".dih-ad{box-sizing:border-box;width:100%;max-width:520px;margin:18px auto 0;"
    "padding:8px 10px 10px;border-radius:14px;background:rgba(255,255,255,.06);"
    "border:1px solid rgba(255,255,255,.16);overflow:hidden;text-align:left;color:inherit}"
    ".dih-ad small{display:block;font:600 9px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace;"
    "letter-spacing:.18em;text-transform:uppercase;opacity:.55;margin-bottom:4px}"
    ".dih-ad-light{background:rgba(74,44,30,.05);border-color:rgba(74,44,30,.18);color:#4a2c1e}"
    ".dih-end-ad{margin:12px auto 14px;max-width:520px}"
    ".dih-end-ad:empty{display:none}"
)

AD_HTML = (
    '<div class="dih-ad%s" id="dihStartAd" role="complementary" aria-label="Advertisement" style="margin-bottom:14px">'
    '<small>Advertisement</small>'
    '<ins class="adsbygoogle" style="display:inline-block;width:300px;height:250px"'
    ' data-ad-client="ca-pub-5443646750699471" data-ad-slot="8451723433"></ins>'
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>'
    '</div>'
)

# One helper, defined once per game. It hides the start-screen unit, mounts the
# end-screen unit and asks AdSense to fill it. Guarded so repeated game-over
# screens reuse the same unit instead of stacking new ones.
END_HELPER = """<script>
window.dihEndScreen = function (boxId) {
  var start = document.getElementById('dihStartAd');
  if (start) start.style.display = 'none';
  var box = document.getElementById(boxId || 'dihEndAd');
  if (!box || box.dataset.mounted) return;
  box.dataset.mounted = '1';
  var ad = document.createElement('div');
  ad.className = 'dih-ad%s';
  ad.setAttribute('role', 'complementary');
  ad.setAttribute('aria-label', 'Advertisement');
  ad.innerHTML = '<small>Advertisement</small><ins class="adsbygoogle" style="display:inline-block;width:300px;height:250px" data-ad-client="ca-pub-5443646750699471" data-ad-slot="8451723433"></ins>';
  box.appendChild(ad);
  try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
};
</script>
"""

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

    # AdSense: loader in the head, one unit on the start screen.
    head_extra = "%s\n<style id=\"dih-ad-style\">%s\n%s</style>\n</head>" % (
        ADSENSE_LOADER, AD_CSS, game["ad_css"])
    doc, n_head = re.subn(r"</head>", lambda m: head_extra, doc, count=1, flags=re.I)
    if n_head != 1:
        raise SystemExit(f"{slug}: no </head> found")

    anchor = game["ad_anchor"]
    if doc.count(anchor) != 1:
        raise SystemExit(f"{slug}: ad anchor matched {doc.count(anchor)} times")
    ad = AD_HTML % (" dih-ad-light" if game["ad_light"] else "")
    doc = doc.replace(anchor, anchor + "\n" + ad, 1)

    # End-screen mount points (one per visible end screen, unique ids).
    for mount in game["end_mounts"]:
        marker = '<div class="dih-end-ad" id="%s"></div>' % mount["id"]
        if mount.get("after_start_ad"):
            doc = doc.replace(ad, ad + "\n" + marker, 1)
            continue
        needle = mount["before"]
        if doc.count(needle) != 1:
            raise SystemExit(f"{slug}: end mount anchor matched {doc.count(needle)} times: {needle}")
        doc = doc.replace(needle, marker + "\n" + needle, 1)

    # Call the mount from each game-over / victory handler.
    for needle, expected, box_id in game["end_hooks"]:
        found = doc.count(needle)
        if found != expected:
            raise SystemExit(f"{slug}: end hook {needle!r} matched {found}, expected {expected}")
        doc = doc.replace(needle, needle + " dihEndScreen('%s');" % box_id)

    # Define the helper just before the closing body tag.
    helper = END_HELPER % (" dih-ad-light" if game["ad_light"] else "")
    if doc.count("</body>") != 1:
        raise SystemExit(f"{slug}: expected one </body>")
    doc = doc.replace("</body>", helper + "</body>", 1)

    out = ROOT / "games" / (slug + ".html")
    out.write_text(doc, encoding="utf-8")
    print("wrote", out.relative_to(ROOT), len(doc), "bytes")


if __name__ == "__main__":
    for game in GAMES:
        build(game)
