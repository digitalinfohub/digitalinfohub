#!/usr/bin/env python3
"""Generate a unique 1200x630 social card for every page on the site.

Every page gets its own artwork, derived from its slug and title, so a shared
link never shows the same thumbnail as another page. The design is deterministic:
the same slug always produces the same card, so regeneration is safe.

    python3 scripts/og_images.py            # build missing cards and rewire meta
    python3 scripts/og_images.py --force    # rebuild all artwork
    python3 scripts/og_images.py --only software/calculator.html

Cards are written to assets/og/<slug>.jpg and every page's og:image,
og:image:secure_url, twitter:image and schema primaryImageOfPage are pointed at
them.
"""
from __future__ import annotations

import colorsys
import hashlib
import math
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "og"
SITE = "https://digitalinfohub.net"
W, H = 1200, 630

SKIP = {"404.html"}

SECTIONS = [
    ("software/", "Creative Studio"),
    ("games/", "Pixel Palace Arcade"),
    ("vrgames/", "VR Arcade"),
    ("vrexperiences/", "VR Experiences"),
    ("post/", "Field Notes"),
]


def pages() -> list[Path]:
    found: list[Path] = []
    for pattern in ("*.html", "software/*.html", "games/*.html", "vrgames/*.html", "vrexperiences/*.html", "post/*.html"):
        found += sorted(ROOT.glob(pattern))
    return [p for p in found if p.name not in SKIP]


def slug_for(rel: str) -> str:
    s = rel.replace("\\", "/")
    if s.endswith(".html"):
        s = s[:-5]
    if s in ("", "index"):
        return "home"
    return s.strip("/").replace("/", "-").lower()


PUNCT = {
    "\u2014": "-", "\u2013": "-", "\u2012": "-", "\u2212": "-",
    "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
    "\u00b7": "\u00b7", "\u00d7": "\u00d7", "\u2192": "\u2192",
}


def card_text(s: str) -> str:
    """The bundled card font has no typographic dashes or quotes."""
    out = []
    for ch in s:
        if ch in PUNCT:
            out.append(PUNCT[ch])
        elif ord(ch) < 128 or ch in "\u00b7\u00d7\u2192":
            out.append(ch)
        else:
            out.append("")
    return re.sub(r"\s+", " ", "".join(out)).strip()


def title_of(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, re.S | re.I)
    if not m:
        return "Digital Infohub"
    t = re.sub(r"\s+", " ", m.group(1)).strip()
    t = t.replace("&amp;", "&").replace("&#x27;", "'").replace("&quot;", '"')
    # Drop the trailing brand so the card can carry it as a footer instead.
    t = re.split(r"\s+[|\u2014\u2013]\s+Digital Infohub", t)[0]
    return card_text(t.strip(" |\u2014\u2013"))


def section_of(rel: str) -> str:
    rel = rel.replace("\\", "/")
    for prefix, label in SECTIONS:
        if rel.startswith(prefix):
            return label
    if rel in ("blog.html", "news.html") or rel.startswith("post/"):
        return "Field Notes"
    if rel in ("software.html",):
        return "Creative Studio"
    if rel in ("games.html",):
        return "Pixel Palace Arcade"
    if rel in ("vrexperiences.html",):
        return "VR Experiences"
    if rel in ("vr.html",):
        return "VR Hub"
    if rel in ("techtopics.html",) or rel in TOPIC_SLUGS:
        return "Tech Topics"
    if rel in ("coincompass.html",):
        return "Markets"
    return "Digital Infohub"


TOPIC_SLUGS = {
    "3dprinting.html", "5gnetworks.html", "advertisingtech.html", "apis.html",
    "artificialintelligence.html", "augmentedreality.html", "automation.html",
    "autonomousvehicles.html", "bigdata.html", "biotechnology.html",
    "blockchain.html", "cloudcomputing.html", "cybersecurity.html",
    "datacenters.html", "digitaltwins.html", "drones.html", "edtech.html",
    "edgecomputing.html", "fintech.html", "greenenergy.html", "healthtech.html",
    "iot.html", "machinelearning.html", "nanotechnology.html", "nfts.html",
    "quantumcomputing.html", "robotics.html", "saas.html", "serverlesscomputing.html",
    "smartcities.html", "spaceindustry.html", "supplychaintech.html",
    "virtualreality.html", "wearables.html", "web3.html",
}


def palette(seed: str) -> tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]:
    h = int(hashlib.sha256(seed.encode()).hexdigest()[:8], 16)
    hue = (h % 360) / 360
    hue2 = ((h >> 9) % 40 + 150) / 360  # a second, cooler hue
    c1 = colorsys.hsv_to_rgb(hue, 0.55, 0.14)
    c2 = colorsys.hsv_to_rgb(hue2, 0.62, 0.34)
    accent = colorsys.hsv_to_rgb(hue, 0.62, 1.0)
    to255 = lambda c: tuple(int(v * 255) for v in c)  # noqa: E731
    return to255(c1), to255(c2), to255(accent)


def hexa(c: tuple[int, int, int]) -> str:
    return "#%02x%02x%02x" % c


def gradient(size, c1, c2, angle=70):
    w, h = size
    base = Image.new("RGB", (w, h), c1)
    top = Image.new("RGB", (w, h), c2)
    mask = Image.new("L", (w, h))
    px = mask.load()
    rad = math.radians(angle)
    dx, dy = math.cos(rad), math.sin(rad)
    scale = abs(dx) * w + abs(dy) * h
    for y in range(h):
        for x in range(0, w, 1):
            v = (x * dx + y * dy) / scale
            px[x, y] = int(max(0, min(1, v)) * 255)
    base.paste(top, (0, 0), mask)
    return base


def font(size: int):
    return ImageFont.load_default(size=size)


def tracked(draw, xy, text, fnt, fill, extra=3):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + extra
    return x


def wrap(draw, text, fnt, max_w, max_lines=3):
    words = text.split()
    lines, line = [], ""
    for w in words:
        trial = (line + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            line = trial
        else:
            if line:
                lines.append(line)
            line = w
            if len(lines) == max_lines - 1:
                break
    if line and len(lines) < max_lines:
        lines.append(line)
    # Truncate anything that did not fit.
    consumed = " ".join(lines)
    if consumed and len(consumed) < len(text):
        last = lines[-1]
        while draw.textlength(last + "\u2026", font=fnt) > max_w and " " in last:
            last = last.rsplit(" ", 1)[0]
        lines[-1] = last + "\u2026"
    return lines


def motif(img, variant, accent, seed):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    a = tuple(list(accent) + [46])
    a2 = tuple(list(accent) + [22])
    h = int(hashlib.sha256((seed + "m").encode()).hexdigest()[:6], 16)
    if variant == 0:  # concentric arcs, bottom right
        cx, cy = W - 90, H + 40
        for i in range(9):
            r = 90 + i * 74
            d.arc([cx - r, cy - r, cx + r, cy + r], 180, 360, fill=a if i % 2 == 0 else a2, width=3)
    elif variant == 1:  # diagonal stripes
        for i in range(-H, W, 52):
            d.line([(i + (h % 25), H), (i + H + (h % 25), 0)], fill=a2, width=2)
    elif variant == 2:  # dot grid
        step = 38
        for y in range(60, H, step):
            for x in range(W - 560, W, step):
                r = 2.2 if (x // step + y // step) % 3 else 4
                d.ellipse([x - r, y - r, x + r, y + r], fill=a)
    elif variant == 3:  # vertical bars
        for i, x in enumerate(range(W - 520, W, 46)):
            top = 80 + ((i * 53 + h) % 300)
            d.rounded_rectangle([x, top, x + 18, H - 70], radius=9, fill=a2 if i % 2 else a)
    else:  # circuit traces
        for i in range(7):
            y = 90 + i * 72
            x0 = W - 470 + (h >> (i % 5)) % 90
            d.line([(x0, y), (x0 + 150, y)], fill=a, width=2)
            d.line([(x0 + 150, y), (x0 + 150, y + 44)], fill=a, width=2)
            d.ellipse([x0 - 5, y - 5, x0 + 5, y + 5], fill=a)
    img.alpha_composite(layer)


def build(slug: str, title: str, section: str, dest: Path) -> None:
    c1, c2, accent = palette(slug)
    seed = hashlib.sha256(slug.encode()).hexdigest()
    variant = int(seed[0], 16) % 5
    centred = int(seed[1], 16) % 6 == 0

    img = gradient((W, H), c1, c2, angle=90 + int(seed[2], 16) % 60).convert("RGBA")
    # soft glow behind the headline
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([-260, -180, 620, 480], fill=tuple(list(accent) + [26]))
    img.alpha_composite(glow)
    motif(img, variant, accent, slug)

    d = ImageDraw.Draw(img)
    # accent edge
    d.rectangle([0, 0, 7, H], fill=accent)

    pad = 84
    eyebrow_font = font(21)
    accent_txt = hexa(accent)
    tracked(d, (pad + 2, 96), section.upper(), eyebrow_font, accent_txt, extra=4.2)
    d.line([(pad + 2, 136), (pad + 74, 136)], fill=tuple(list(accent) + [190]), width=3)

    title_font = font(60 if len(title) < 52 else 52)
    lines = wrap(d, title, title_font, W - pad * 2 - 250, max_lines=3)
    y = 205 if len(lines) <= 2 else 180
    for line in lines:
        d.text((pad, y), card_text(line), font=title_font, fill=(255, 255, 255), stroke_width=0)
        y += int(title_font.size * 1.22)

    # footer
    fy = H - 96
    d.ellipse([pad + 2, fy + 6, pad + 18, fy + 22], fill=accent)
    d.text((pad + 30, fy), "digitalinfohub.net", font=font(24), fill=(226, 231, 240))
    d.text((W - pad - 220, fy), "Free \u00b7 no signup", font=font(22), fill=(150, 158, 175))

    img.convert("RGB").save(dest, "JPEG", quality=82, optimize=True, progressive=True)


def rewrite_meta(html: str, url: str, alt: str) -> str:
    def sub(pattern, repl, text):
        return re.sub(pattern, repl, text, count=1)

    html = sub(r'(<meta property="og:image" content=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), html)
    html = sub(r'(<meta property="og:image:secure_url" content=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), html)
    html = sub(r'(<meta property="og:image:alt" content=")[^"]*(")', lambda m: m.group(1) + alt + m.group(2), html)
    html = sub(r'(<meta name="twitter:image" content=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), html)
    html = sub(r'(<meta name="twitter:image:alt" content=")[^"]*(")', lambda m: m.group(1) + alt + m.group(2), html)
    # schema primaryImageOfPage
    html = re.sub(r'("primaryImageOfPage":\s*\{[^}]*?"url":\s*")[^"]*(")',
                  lambda m: m.group(1) + url + m.group(2), html, count=1)
    return html


def main() -> None:
    force = "--force" in sys.argv
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1]
    OUT.mkdir(parents=True, exist_ok=True)
    made = rewired = 0
    for path in pages():
        rel = str(path.relative_to(ROOT)).replace("\\", "/")
        if only and rel != only:
            continue
        slug = slug_for(rel)
        html = path.read_text(encoding="utf-8")
        title = title_of(html)
        dest = OUT / f"{slug}.jpg"
        if force or not dest.exists():
            build(slug, title, section_of(rel), dest)
            made += 1
        url = f"{SITE}/assets/og/{slug}.jpg"
        alt = f"{title} \u2014 Digital Infohub"
        new = rewrite_meta(html, url, alt.replace('"', "&quot;"))
        if new != html:
            path.write_text(new, encoding="utf-8")
            rewired += 1
    print(f"{made} image(s) built, {rewired} page(s) rewired, {len(list(OUT.glob('*.jpg')))} cards on disk")


if __name__ == "__main__":
    main()
