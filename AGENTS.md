# Blog workflow
Static trilingual blog (EN/JA/ZH). Posts live in /post as self-contained HTML.
Never hand-edit files in /post — always regenerate from the template.

To create a new post:
1. Write `_posts/<slug>.json` (see existing examples for the schema). Use [[n]] markers for inline citations in the body HTML — do NOT hand-write reference anchors.
2. Run `python3 scripts/build_post.py <slug>` (stdlib only — no installs needed). Use `--all` to rebuild every post.
3. Verify post/<slug>.html renders correctly, then commit and publish.
