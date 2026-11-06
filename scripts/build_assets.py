#!/usr/bin/env python3
"""Generate the favicon / app-icon / social-card set from DigitalInfohubLogo.png.

Run from the repo root:  python3 scripts/build_assets.py

Outputs (all committed, no network needed):
  assets/logo.png              256px nav + chat avatar
  assets/favicon-32.png        32px favicon
  assets/favicon-16.png        16px favicon
  assets/favicon.ico           multi-size icon
  assets/apple-touch-icon.png  180px iOS home-screen icon
  assets/icon-192.png          PWA icon
  assets/icon-512.png          PWA icon
  assets/og-cover.png          1200x630 social share card
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "DigitalInfohubLogo.png"
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)

logo = Image.open(SRC).convert("RGBA")


def square(size: int, pad_ratio: float = 0.0) -> Image.Image:
    """Logo centred on a square opaque canvas."""
    canvas = Image.new("RGBA", (size, size), (7, 7, 12, 255))
    inner = int(size * (1 - pad_ratio * 2))
    img = logo.resize((inner, inner), Image.LANCZOS)
    canvas.alpha_composite(img, ((size - inner) // 2, (size - inner) // 2))
    return canvas


square(256, 0.02).save(OUT / "logo.png", optimize=True)
square(32, 0.02).save(OUT / "favicon-32.png", optimize=True)
square(16, 0.02).save(OUT / "favicon-16.png", optimize=True)
square(180, 0.02).save(OUT / "apple-touch-icon.png", optimize=True)
square(192, 0.02).save(OUT / "icon-192.png", optimize=True)
square(512, 0.02).save(OUT / "icon-512.png", optimize=True)

square(64, 0.02).save(
    OUT / "favicon.ico",
    sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64)],
)

# ---------------------------------------------------------------- OG card
W, H = 1200, 630
og = Image.new("RGB", (W, H), (7, 7, 12))
px = og.load()

# Diagonal blue/violet gradient wash.
for y in range(H):
    for x in range(0, W, 4):
        t = (x / W) * 0.55 + (y / H) * 0.45
        r = int(7 + 38 * t)
        g = int(7 + 26 * t)
        b = int(12 + 70 * t)
        for k in range(4):
            if x + k < W:
                px[x + k, y] = (r, g, b)

draw = ImageDraw.Draw(og, "RGBA")

# Grid.
for x in range(0, W, 60):
    draw.line([(x, 0), (x, H)], fill=(255, 255, 255, 8), width=1)
for y in range(0, H, 60):
    draw.line([(0, y), (W, y)], fill=(255, 255, 255, 8), width=1)

# Glows.
draw.ellipse([-260, -300, 520, 330], fill=(76, 141, 255, 40))
draw.ellipse([760, 300, 1420, 900], fill=(139, 92, 246, 34))

icon = logo.resize((168, 168), Image.LANCZOS)
og.paste(icon, (96, 96), icon)

font_paths = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
]
regular_paths = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
]


def load_font(paths, size):
    for p in paths:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


bold = load_font(font_paths, 62)
bold_small = load_font(font_paths, 30)
body = load_font(regular_paths, 30)
tag = load_font(font_paths, 22)

draw.text((300, 120), "Digital", font=bold, fill=(245, 247, 250))
draw.text((300, 190), "Infohub", font=bold, fill=(122, 176, 255))

draw.text((100, 330), "Tech intelligence for people who", font=bold_small, fill=(245, 247, 250))
draw.text((100, 374), "build, buy and invest in technology.", font=bold_small, fill=(245, 247, 250))

draw.text((100, 450), "AI  ·  Markets  ·  Software  ·  Tech Topics  ·  Games", font=body, fill=(168, 174, 190))

draw.rounded_rectangle([100, 522, 392, 574], radius=26, fill=(76, 141, 255, 235))
draw.text((126, 534), "digitalinfohub.net", font=tag, fill=(255, 255, 255))

og.save(OUT / "og-cover.png", optimize=True, quality=88)

print("assets built:", ", ".join(sorted(p.name for p in OUT.glob("*") if p.is_file())))
