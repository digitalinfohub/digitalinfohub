#!/usr/bin/env python3
"""Build the public staging directory used by Freebuff Sites.

The Publish button's previous output copied source files and produced a manifest
with an extra field. This script creates only public files, a clean manifest and
the Workers entrypoint. Run it after apply_site.py / build_topics.py.

Usage: python3 scripts/build_sites.py
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "freebuff-sites-build"
PUBLIC = OUT / "assets"

PUBLIC_ROOT_FILES = [
    "ads.txt", "favicon.ico", "robots.txt", "site.webmanifest", "sitemap.xml",
]
SKIP_PARTS = {"__pycache__", ".git", ".wrangler", "node_modules", "scripts", "_posts"}


def copy_public_tree():
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir(parents=True)

    for path in sorted(ROOT.glob("*.html")):
        shutil.copy2(path, PUBLIC / path.name)

    for folder in ("post", "software"):
        source = ROOT / folder
        target = PUBLIC / folder
        target.mkdir()
        for path in sorted(source.glob("*.html")):
            shutil.copy2(path, target / path.name)

    for name in PUBLIC_ROOT_FILES:
        source = ROOT / name
        if source.exists():
            shutil.copy2(source, PUBLIC / name)

    source_assets = ROOT / "assets"
    target_assets = PUBLIC / "assets"
    target_assets.mkdir()
    for path in source_assets.rglob("*"):
        if path.is_dir() or SKIP_PARTS.intersection(path.parts):
            continue
        relative = path.relative_to(source_assets)
        destination = target_assets / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)


def write_worker():
    source = ROOT / "scripts" / "sites_worker.js"
    shutil.copy2(source, OUT / "worker.js")
    manifest = {
        "entrypoint": "worker.js",
        "compatibilityDate": "2026-11-01",
        "modules": [
            {"name": "worker.js", "type": "esm", "path": "./worker.js"}
        ],
        "assetsDirectory": "./assets",
        "spa": False,
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    copy_public_tree()
    write_worker()

    files = [p for p in PUBLIC.rglob("*") if p.is_file()]
    size = sum(p.stat().st_size for p in files)
    print(f"built {OUT.relative_to(ROOT)}: {len(files)} public files, {size / 1024 / 1024:.2f} MiB")

    required = ["index.html", "news.html", "quiz.html", "techtopics.html", "software.html",
                "assets/site.css", "assets/site.js", "assets/digi.js", "assets/digi.png",
                "assets/news.js", "assets/quiz.js", "assets/chat-markdown.js",
                "api/news does not need a file"]
    missing = [name for name in required if not name.startswith("api/") and not (PUBLIC / name).exists()]
    if missing:
        raise SystemExit("missing public files: " + ", ".join(missing))
    print("required public files present")


if __name__ == "__main__":
    main()
