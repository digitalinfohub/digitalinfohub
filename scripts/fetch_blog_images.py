#!/usr/bin/env python3
"""Download the images used by the blog index so thumbnails never break.

- Reads the POSTS array in blog.html.
- Downloads each remote image, normalises it to a 900px JPEG in assets/blog/.
- Rewrites the blog.html image field to the local path.
- Falls back to a generated brand image when a source is unavailable.
Run: python3 scripts/fetch_blog_images.py
"""
import io
import re
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
BLOG = ROOT / "blog.html"
OUT = ROOT / "assets" / "blog"
OUT.mkdir(parents=True, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (compatible; DigitalInfohub/1.0)"}


def fallback() -> Path:
    path = OUT / "fallback.jpg"
    if path.exists():
        return path
    logo = Image.open(ROOT / "DigitalInfohubLogo.png").convert("RGBA").resize((220, 220), Image.LANCZOS)
    img = Image.new("RGB", (900, 563), (10, 11, 20))
    draw = ImageDraw.Draw(img, "RGBA")
    for y in range(563):
        t = y / 563
        draw.line([(0, y), (900, y)], fill=(int(10 + 26 * t), int(11 + 20 * t), int(20 + 54 * t)))
    draw.ellipse([-180, -220, 520, 300], fill=(76, 141, 255, 46))
    draw.ellipse([520, 300, 1080, 760], fill=(139, 92, 246, 38))
    img.paste(logo, ((900 - 220) // 2, (563 - 220) // 2 - 10), logo)
    img.save(path, quality=82, optimize=True)
    return path


def normalise(raw: bytes, dest: Path) -> bool:
    try:
        im = Image.open(io.BytesIO(raw))
        im.load()
        im = im.convert("RGB")
        w, h = im.size
        target_w = 900
        if w > target_w:
            im = im.resize((target_w, int(h * target_w / w)), Image.LANCZOS)
        im.save(dest, "JPEG", quality=82, optimize=True, progressive=True)
        return True
    except Exception as exc:  # noqa: BLE001
        print("  ! could not decode:", exc)
        return False


def main() -> None:
    html = BLOG.read_text(encoding="utf-8")
    entries = 0
    downloaded = 0
    rewritten = 0

    def repl(match: re.Match) -> str:
        nonlocal entries, downloaded, rewritten
        line = match.group(0)
        link = re.search(r"link:\s*'([^']+)'", line)
        image = re.search(r"image:\s*'([^']+)'", line)
        if not link or not image:
            return line
        entries += 1
        url = image.group(1)
        slug_match = re.search(r"/post/([a-z0-9-]+)", link.group(1))
        slug = slug_match.group(1) if slug_match else re.sub(r"[^a-z0-9]+", "-", link.group(1))[-60:]
        dest = OUT / f"{slug}.jpg"
        if not dest.exists():
            try:
                req = urllib.request.Request(url, headers=UA)
                with urllib.request.urlopen(req, timeout=30) as resp:
                    raw = resp.read()
                if raw and normalise(raw, dest):
                    downloaded += 1
                    print("  ok", slug, f"{len(raw)//1024}kb")
                else:
                    raise ValueError("empty or invalid")
            except Exception as exc:  # noqa: BLE001
                print("  fallback", slug, "-", exc)
                dest.write_bytes(fallback().read_bytes())
        if url != f"/assets/blog/{slug}.jpg":
            rewritten += 1
        return line.replace(url, f"/assets/blog/{slug}.jpg")

    new_html = re.sub(r"\{ title:.*?\},?\n", repl, html)
    BLOG.write_text(new_html, encoding="utf-8")
    print(f"entries={entries} downloaded={downloaded} rewritten={rewritten}")


if __name__ == "__main__":
    main()
