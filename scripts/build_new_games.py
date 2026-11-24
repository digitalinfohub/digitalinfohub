#!/usr/bin/env python3
"""Build the three new Pixel Palace game pages from the shared site chrome.

The chrome (head, meta, header, footer) is taken from games/snake.html so the
new pages stay identical to the existing arcade pages; only the <main> body and
page meta are swapped in from _arcade/<slug>.html.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHROME = (ROOT / "games" / "snake.html").read_text(encoding="utf-8")

GAMES = [
    {
        "slug": "block-defender",
        "title": "Block Defender — Neon Falling Blocks Game | Digital Infohub",
        "desc": "Play Block Defender free in your browser: neon falling blocks, glitch bugs to crush and five sectors to clear. Power cells, row lasers and EMP blasts. No download.",
        "genre": "Puzzle",
    },
    {
        "slug": "neon-horizon",
        "title": "Neon Horizon — Endless Neon Highway Racer | Digital Infohub",
        "desc": "Play Neon Horizon free: an endless four-lane neon highway racer with traffic, fuel canisters and a score that climbs with every mile. Arrow keys or touch steering.",
        "genre": "Racing",
    },
    {
        "slug": "perfect-pour",
        "title": "Perfect Pour — Coffee Pouring Game | Digital Infohub",
        "desc": "Play Perfect Pour free: hold to pour coffee, stop inside the green target band and chase three stars across five cups. A calm, tactile browser skill game.",
        "genre": "Skill",
    },
]

HEAD_PREFIX = CHROME[: CHROME.index("<title>")]
HEAD_ASSETS = CHROME[CHROME.index('<link rel="stylesheet" href="/assets/hub.css'): CHROME.index("<!-- DIH:HEAD -->")]
HEAD_ASSETS = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', "", HEAD_ASSETS, flags=re.S)
HEAD_META = CHROME[CHROME.index("<!-- DIH:HEAD -->"): CHROME.index("<!-- /DIH:HEAD -->")]
HEADER = CHROME[CHROME.index("<!-- DIH:HEADER -->"): CHROME.index("<!-- /DIH:HEADER -->") + len("<!-- /DIH:HEADER -->")]
FOOTER = CHROME[CHROME.index("<!-- DIH:FOOTER -->"): CHROME.index("<!-- /DIH:FOOTER -->") + len("<!-- /DIH:FOOTER -->")]

LD = (
    '{"@context":"https://schema.org","@type":"VideoGame","name":"%s",'
    '"url":"https://digitalinfohub.net/games/%s","description":"%s",'
    '"genre":"%s","gamePlatform":"Web browser","playMode":"SinglePlayer",'
    '"applicationCategory":"Game","operatingSystem":"Any",'
    '"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"inLanguage":"en",'
    '"publisher":{"@type":"Organization","name":"Digital Infohub","url":"https://digitalinfohub.net"},'
    '"isPartOf":{"@type":"WebSite","name":"Digital Infohub","url":"https://digitalinfohub.net"}}'
)


def build(game):
    slug = game["slug"]
    name = game["title"].split(" — ")[0]
    url = "https://digitalinfohub.net/games/" + slug

    head = HEAD_PREFIX
    head += "<title>%s</title>\n" % game["title"]
    head += '<meta name="description" content="%s">\n' % game["desc"]
    head += '<script type="application/ld+json">\n' + (LD % (name, slug, game["desc"], game["genre"])) + "\n</script>\n"
    head += HEAD_ASSETS

    meta = HEAD_META
    meta = meta.replace("https://digitalinfohub.net/games/snake", url)
    meta = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + game["title"] + m.group(2), meta)
    meta = re.sub(r'(<meta name="twitter:title" content=")[^"]*(")', lambda m: m.group(1) + game["title"] + m.group(2), meta)
    meta = re.sub(r'(<meta property="og:description" content=")[^"]*(")', lambda m: m.group(1) + game["desc"] + m.group(2), meta)
    meta = re.sub(r'(<meta name="twitter:description" content=")[^"]*(")', lambda m: m.group(1) + game["desc"] + m.group(2), meta)

    body = (ROOT / "_arcade" / (slug + ".html")).read_text(encoding="utf-8")
    page = (
        head
        + meta
        + "\n<!-- /DIH:HEAD -->\n<!-- DIH:AMBIENT -->\n<div class=\"dih-ambient\" aria-hidden=\"true\"><i></i><i></i><i></i></div>\n<!-- /DIH:AMBIENT -->\n"
        + HEADER
        + "\n"
        + body
        + "\n\n"
        + FOOTER
        + "\n<script src=\"/assets/site.js\" defer></script>\n</body>\n</html>\n"
    )
    out = ROOT / "games" / (slug + ".html")
    out.write_text(page, encoding="utf-8")
    print("wrote", out.relative_to(ROOT), len(page), "bytes")


if __name__ == "__main__":
    for game in GAMES:
        build(game)
