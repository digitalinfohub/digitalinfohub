#!/usr/bin/env python3
"""Usage: python3 scripts/build_post.py <slug> | --all"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "scripts" / "template.html"
POSTS_DIR = ROOT / "_posts"
OUT_DIR = ROOT / "post"
LANGS = ["en", "ja", "zh"]
SUFFIX = {"en": "", "ja": "-ja", "zh": "-zh"}
SRC_HEAD = {"en": "Sources", "ja": "情報源", "zh": "参考来源"}

def body_html(body, lang):
    return re.sub(r"\[\[(\d+)\]\]",
                  lambda m: f'<a href="#src-{m.group(1)}{SUFFIX[lang]}" class="ref">[{m.group(1)}]</a>',
                  body)

def sources_html(sources, lang):
    out = []
    for i, s in enumerate(sources, 1):
        out.append(f'          <li id="src-{i}{SUFFIX[lang]}">\n'
                   f'            <span class="src-title">{s["title"]}</span>\n'
                   f'            <a class="src-url" href="{s["url"]}" target="_blank" rel="noopener">{s["display"]}</a>\n'
                   f'          </li>')
    return "\n".join(out)

def build(slug):
    data = json.loads((POSTS_DIR / f"{slug}.json").read_text(encoding="utf-8"))
    html = TEMPLATE.read_text(encoding="utf-8")
    reps = {
        "{{TITLE_TAG}}": data["title"]["en"],
        "{{META_DESC}}": data["meta_description"],
        "{{OG_DESC}}": data["og_description"],
        "{{OG_IMAGE}}": data["og_image"],
        "{{JS_TITLES}}": ",\n    ".join(f"{l}: {json.dumps(data['title'][l], ensure_ascii=False)}" for l in LANGS),
        "{{TAGS}}": "\n        ".join(f'<a class="tag" href="#">{t}</a>' for t in data["tags"]),
    }
    for l in LANGS:
        reps[f"{{{{META_{l}}}}}"] = data["read_time"][l]
        reps[f"{{{{TITLE_{l}}}}}"] = data["title"][l]
        reps[f"{{{{SUBTITLE_{l}}}}}"] = data["subtitle"][l]
        reps[f"{{{{BODY_{l}}}}}"] = body_html(data["body"][l], l)
    for k, v in reps.items():
        html = html.replace(k, v)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / f"{slug}.html").write_text(html, encoding="utf-8")
    print(f"built post/{slug}.html")

if __name__ == "__main__":
    if sys.argv[1:] == ["--all"]:
        for p in sorted(POSTS_DIR.glob("*.json")): build(p.stem)
    elif len(sys.argv) == 2: build(sys.argv[1])
    else: sys.exit(__doc__)
