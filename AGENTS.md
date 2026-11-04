# Blog workflow
Static trilingual blog (EN/JA/ZH). Posts live in /post as self-contained HTML.
Never hand-edit files in /post — always regenerate from the template.

To create a new post:
1. Write `_posts/<slug>.json` (see existing examples for the schema). Use [[n]] markers for inline citations in the body HTML — do NOT hand-write reference anchors.
2. Run `python3 scripts/build_post.py <slug>` (stdlib only — no installs needed). Use `--all` to rebuild every post.
3. Verify post/<slug>.html renders correctly, then commit and publish.

# Tech Topics

The Tech Topics guides at the site root (`/artificialintelligence`, `/robotics`, ...)
and `techtopics.html` are generated. Never hand-edit them.

1. Edit the topic content in `scripts/topics_part1.py` … `topics_part4.py` (one entry per
topic: slug, title, meta description, sections, facts, FAQ, related slugs).
2. Run `python3 scripts/build_topics.py` (stdlib only). Use `python3 scripts/build_topics.py <slug>`
   to rebuild a single guide.
3. The build also refreshes `techtopics.html`, `sitemap.xml` and `robots.txt`.
4. Preview with `python3 scripts/preview_server.py 3000`, which resolves `/slug` to `slug.html`.
