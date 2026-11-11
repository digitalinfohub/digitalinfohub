#!/usr/bin/env python3
"""Curated Unsplash imagery for Digital Infohub.

One registry powers:
  * social share images (og:image / twitter:image) on every page
  * the "Technology, in focus" clickable cards injected across the site
  * the subtle ambient background behind each page

All URLs point at real Unsplash photos (validated with HTTP 200 image/jpeg).
Do not hand-write image URLs elsewhere — add them here.
"""
from html import escape

SHARE_W, SHARE_H = 1200, 630
CARD_W, CARD_H = 800, 500
AMBIENT_W, AMBIENT_H = 1600, 900


def _photo_url(photo_id: str, w: int, h: int, q: int = 80) -> str:
    return (
        f"https://images.unsplash.com/{photo_id}"
        f"?w={w}&h={h}&fit=crop&auto=format&q={q}"
    )


IMAGES = [
    {
        "id": "dots",
        "photo": "photo-1758073519996-6d3c63b4922c",
        "tag": "IoT",
        "title": "Connected by default",
        "blurb": "A modern factory floor now runs more connected sensors than laptops. The value is in the data, but every new endpoint is also a new door to defend.",
        "href": "/internetofthings",
        "cta": "Read the IoT guide",
        "alt": "Abstract blue field of glowing technology dots representing a connected network",
    },
    {
        "id": "network",
        "photo": "photo-1644088379091-d574269d422f",
        "tag": "5G & edge",
        "title": "Networks that think",
        "blurb": "Modern networks do not just move packets; they schedule workloads, slice bandwidth and push compute closer to users. That is what makes low-latency apps feel instant.",
        "href": "/5gnetworks",
        "cta": "Explore 5G networks",
        "alt": "Glowing blue network lines and nodes forming a digital mesh",
    },
    {
        "id": "earth",
        "photo": "photo-1451187580459-43490279c0fa",
        "tag": "Cloud",
        "title": "A planetary-scale cloud",
        "blurb": "Cloud regions are physical campuses full of power, cooling and fibre. That geography explains latency, cost and most data-sovereignty rules.",
        "href": "/cloudcomputing",
        "cta": "Read the cloud guide",
        "alt": "Illuminated planet Earth seen from space with blue technology overlays",
    },
    {
        "id": "laptop",
        "photo": "photo-1531297484001-80022131f5a1",
        "tag": "Hardware",
        "title": "The laptop still runs the world",
        "blurb": "Desktops and laptops remain where deep work happens. The buying decision now centres on battery efficiency, memory bandwidth and how well the machine handles AI-assisted software.",
        "href": "/techproducts",
        "cta": "Tech buying guides",
        "alt": "Slim laptop on a desk lit with cool blue light",
    },
    {
        "id": "circuit",
        "photo": "photo-1782155789465-9bae14cbfba5",
        "tag": "Semiconductors",
        "title": "Inside the silicon bottleneck",
        "blurb": "A leading-edge chip can take months to fabricate and thousands of steps to test. That complexity is why semiconductor capacity became a strategic asset.",
        "href": "/semiconductors",
        "cta": "Read the semiconductor guide",
        "alt": "Macro photograph of a dense electronic circuit board",
    },
    {
        "id": "security",
        "photo": "photo-1550751827-4bd374c3f58b",
        "tag": "Cybersecurity",
        "title": "Security is an identity problem",
        "blurb": "Most breaches start with a stolen session or a weak credential, not a broken firewall. Strong identity checks and short-lived access do more than another perimeter tool.",
        "href": "/cybersecurity",
        "cta": "Read the security guide",
        "alt": "Cybersecurity concept with a glowing padlock over code",
    },
    {
        "id": "blue-dots",
        "photo": "photo-1644325349124-d1756b79dd42",
        "tag": "Data",
        "title": "Finding signal in the noise",
        "blurb": "Data teams spend more time cleaning and labelling than modelling. The quality of that groundwork decides whether a dashboard is trusted or ignored.",
        "href": "/bigdata",
        "cta": "Read the big data guide",
        "alt": "Blue abstract background with fine lines and dots",
    },
    {
        "id": "laptop-open",
        "photo": "photo-1548092372-0d1bd40894a3",
        "tag": "AI hardware",
        "title": "Where AI actually lands",
        "blurb": "AI is moving from cloud data centres onto phones, laptops and wearables. On-device inference cuts latency and keeps sensitive data local, at the cost of model size.",
        "href": "/post/ai-hardware-race-sept-2026",
        "cta": "Read the AI hardware analysis",
        "alt": "Hands opening a blue and white laptop computer",
    },
    {
        "id": "blue-abstract",
        "photo": "photo-1727434032773-af3cd98375ba",
        "tag": "Machine learning",
        "title": "The shape of a model",
        "blurb": "A model is a structure plus millions of tuned numbers. Change the structure, the data or the evaluation and you get a different product — not just a different score.",
        "href": "/machinelearning",
        "cta": "Read the machine learning guide",
        "alt": "Deep blue abstract digital waves and particles",
    },
    {
        "id": "cubes-a",
        "photo": "photo-1639322537228-f710d846310a",
        "tag": "Blockchain",
        "title": "Blocks, ledgers and trust",
        "blurb": "A blockchain is a shared record that no single party can quietly rewrite. That property is useful for settlement and provenance, and overkill for most databases.",
        "href": "/blockchain",
        "cta": "Read the blockchain guide",
        "alt": "Glowing translucent cubes arranged in a chain",
    },
    {
        "id": "abstract",
        "photo": "photo-1620641788421-7a1c342ea42e",
        "tag": "Digital culture",
        "title": "Where code meets culture",
        "blurb": "Product decisions are cultural decisions. The interfaces people trust tend to be the ones that explain themselves and fail gracefully.",
        "href": "/blog",
        "cta": "Read the latest analysis",
        "alt": "Colourful abstract 3D shapes representing digital creativity",
    },
    {
        "id": "brain",
        "photo": "photo-1677442135703-1787eea5ce01",
        "tag": "Artificial intelligence",
        "title": "Inside the AI brain",
        "blurb": "Large models learn statistical patterns from enormous text corpora. They can draft, summarise and reason usefully, but they still need verification where mistakes are expensive.",
        "href": "/artificialintelligence",
        "cta": "Read the AI guide",
        "alt": "Glowing digital brain made of blue and violet neural connections",
    },
    {
        "id": "abstract-2",
        "photo": "photo-1663895064411-fff0ab8a9797",
        "tag": "Edge computing",
        "title": "Designed for the edge",
        "blurb": "Processing data near the device cuts round trips and bandwidth bills. It also creates a fleet of small systems that must be updated and secured remotely.",
        "href": "/edgecomputing",
        "cta": "Read the edge guide",
        "alt": "Blue and violet abstract technology shapes with depth",
    },
    {
        "id": "desktop",
        "photo": "photo-1614624532983-4ce03382d63d",
        "tag": "Productivity",
        "title": "The productive desk",
        "blurb": "A good desk setup removes friction: one cable, one screen, one place for everything. The same principle applies to the software you use every day.",
        "href": "/techproducts",
        "cta": "Build a better setup",
        "alt": "Clean desktop workspace with monitor, keyboard and warm lighting",
    },
    {
        "id": "cubes-b",
        "photo": "photo-1639322537138-5e513100b36e",
        "tag": "Web3",
        "title": "Smart contracts, plainly",
        "blurb": "A smart contract is code that executes on a shared ledger. It is fast and transparent, but bugs are public, permanent and expensive.",
        "href": "/web3",
        "cta": "Read the Web3 guide",
        "alt": "Abstract glowing cubes connected by thin lines",
    },
    {
        "id": "cubes-c",
        "photo": "photo-1639762681057-408e52192e55",
        "tag": "Markets",
        "title": "Tokenised everything",
        "blurb": "Tokenisation promises faster settlement and fractional ownership. The technology works; the regulatory and custody questions are what slow adoption.",
        "href": "/blockchain",
        "cta": "Read the blockchain guide",
        "alt": "Floating translucent cubes in a dark blue space",
    },
    {
        "id": "waves",
        "photo": "photo-1590859808308-3d2d9c515b1a",
        "tag": "Markets",
        "title": "Riding the market cycle",
        "blurb": "Tech stocks and crypto move on the same liquidity tide more often than investors admit. Watching rates, earnings and risk appetite together beats chasing headlines.",
        "href": "/coincompass",
        "cta": "Open CoinCompass",
        "alt": "Abstract blue data waves resembling a market chart",
    },
    {
        "id": "bulb",
        "photo": "photo-1649406458887-2b6561c36a4d",
        "tag": "3D printing",
        "title": "From idea to prototype",
        "blurb": "Additive manufacturing turns a CAD file into a physical part in hours. It is best for complex geometry, small batches and parts that would be costly to machine.",
        "href": "/3dprinting",
        "cta": "Read the 3D printing guide",
        "alt": "Wireframe lightbulb glowing against a dark background",
    },
    {
        "id": "domore",
        "photo": "photo-1483058712412-4245e9b90334",
        "tag": "Software",
        "title": "Tools for deep work",
        "blurb": "The best productivity tools disappear into a routine. Pick a small set, learn their shortcuts and stop rebuilding your system every month.",
        "href": "/software",
        "cta": "Browse free tools",
        "alt": "Mac computer on a desk with the words Do More on screen",
    },
    {
        "id": "vr",
        "photo": "photo-1593508512255-86ab42a8e620",
        "tag": "VR & AR",
        "title": "The next interface",
        "blurb": "VR and AR are finding real work in training, design review and simulation. The hardware is improving faster than the comfort and content problems.",
        "href": "/virtualreality",
        "cta": "Read the VR guide",
        "alt": "Person wearing a virtual reality headset in blue light",
    },
]

BY_ID = {image["id"]: image for image in IMAGES}


def share_url(image_id: str) -> str:
    # Force JPEG so every social crawler gets a predictable 1200x630 card.
    return _photo_url(BY_ID[image_id]["photo"], SHARE_W, SHARE_H, 80) + "&fm=jpg"


def card_url(image_id: str) -> str:
    return _photo_url(BY_ID[image_id]["photo"], CARD_W, CARD_H, 72)


def ambient_url(image_id: str) -> str:
    return _photo_url(BY_ID[image_id]["photo"], AMBIENT_W, AMBIENT_H, 45)


def image_alt(image_id: str) -> str:
    return BY_ID[image_id]["alt"]


# Social card for the main hand-authored pages.
PAGE_IMAGES = {
    "index.html": "dots",
    "blog.html": "network",
    "techtopics.html": "circuit",
    "software.html": "domore",
    "techproducts.html": "laptop",
    "games.html": "vr",
    "subscribe.html": "earth",
    "about.html": "abstract-2",
    "services.html": "bulb",
    "advertise.html": "desktop",
    "news.html": "network",
    "quiz.html": "brain",
    "coincompass.html": "waves",
    "privacy-policy.html": "security",
    "expense-tracker.html": "blue-dots",
    "pomodoro.html": "desktop",
}

TOOL_IMAGES = {
    "tool-calendar.html": "dots",
    "tool-expense-tracker.html": "waves",
    "tool-json-formatter.html": "circuit",
    "tool-markdown-editor.html": "abstract",
    "tool-password-generator.html": "security",
    "tool-pomodoro.html": "desktop",
    "tool-qr-generator.html": "cubes-a",
    "tool-quick-notes.html": "laptop",
    "tool-task-manager.html": "domore",
    "tool-unit-converter.html": "blue-abstract",
}

SOFTWARE_IMAGES = {
    "software/infohubgpt.html": "brain",
    "software/marketlens.html": "waves",
    "software/calculator.html": "blue-dots",
    "software/converter.html": "cubes-c",
    "software/cookinstep.html": "bulb",
    "software/json.html": "circuit",
    "software/kayakmeocean.html": "earth",
    "software/markdown.html": "abstract",
    "software/password.html": "security",
    "software/savesmart.html": "cubes-a",
    "software/taskygpt.html": "domore",
    "software/buildengine.html": "laptop-open",
}

TOPIC_IMAGES = {
    "artificialintelligence": "brain",
    "machinelearning": "blue-abstract",
    "blockchain": "cubes-a",
    "cloudcomputing": "earth",
    "cybersecurity": "security",
    "internetofthings": "dots",
    "quantumcomputing": "cubes-b",
    "bigdata": "blue-dots",
    "virtualreality": "vr",
    "5gnetworks": "network",
    "apis": "circuit",
    "devops": "laptop-open",
    "opensource": "abstract",
    "robotics": "cubes-c",
    "edgecomputing": "abstract-2",
    "web3": "cubes-b",
    "semiconductors": "circuit",
    "3dprinting": "bulb",
    "biotechnology": "blue-abstract",
    "greentechnology": "earth",
    "digitaltwins": "desktop",
    "zerotrustsecurity": "security",
    "serverlesscomputing": "network",
    "neuromorphiccomputing": "brain",
    "augmentedreality": "vr",
    "drones": "network",
    "nanotechnology": "circuit",
    "spacetechnology": "earth",
    "wearabletechnology": "vr",
    "smartcities": "dots",
}

POST_IMAGES = {
    "how-to-clear-cache-on-iphone": "laptop-open",
    "how-to-screen-record-on-iphone": "laptop",
    "why-is-my-face-id-not-working": "security",
    "why-is-my-phone-not-charging": "laptop-open",
    "how-to-stay-safe-online-2026": "security",
    "meet-miyabi-from-nomad-sculpt-to-blender": "abstract",
    "meet-teamtbm": "vr",
    "newest-airpods-2026": "desktop",
    "newest-apple-watch-2026": "blue-dots",
    "newest-ipad-2026": "domore",
    "newest-iphone-2026": "laptop",
    "newest-samsung-phone-2026": "blue-abstract",
    "quantum-computing-breakthroughs-2026": "cubes-b",
    "small-biz-philly-a-great-resource-for-local-entrepreneurs": "domore",
    "tech-market-sell-off-october-2026": "waves",
    "tech-trends-october-2026": "network",
    "top-tech-headlines-sept-2026": "abstract-2",
    "ai-agent-economy-october-catalysts": "brain",
    "ai-hardware-race-sept-2026": "circuit",
    "ai-math-robotics-security-sept-2026": "cubes-c",
    "ai-model-wars-august-2026": "blue-abstract",
    "ai-wearables-2026": "vr",
    "beating-syllabus-overload-with-smarter-medical-learning": "bulb",
    "could-babav-be-your-next-ai-social-media-assistant": "dots",
    "cybersecurity-ai-investment-2026": "security",
    "greygrid-studio-shows-that-great-design-doesn-t-need-to-be-loud": "abstract",
    "investment-ideas-2026": "waves",
    "what-will-tech-look-like-in-the-future": "earth",
    "what-does-tech-look-like-today": "circuit",
}


def image_key_for(rel_path: str) -> str:
    """Resolve a curated image id for a page path such as 'blog.html'."""
    path = rel_path.replace("\\", "/").lstrip("./")
    name = path.rsplit("/", 1)[-1]
    if path in PAGE_IMAGES:
        return PAGE_IMAGES[path]
    if name in PAGE_IMAGES:
        return PAGE_IMAGES[name]
    if path in SOFTWARE_IMAGES:
        return SOFTWARE_IMAGES[path]
    if name in TOOL_IMAGES:
        return TOOL_IMAGES[name]
    stem = name[:-5] if name.endswith(".html") else name
    if path.startswith("post/") and stem in POST_IMAGES:
        return POST_IMAGES[stem]
    if stem in TOPIC_IMAGES:
        return TOPIC_IMAGES[stem]
    if stem in POST_IMAGES:
        return POST_IMAGES[stem]
    return "network"


def _gallery_count(kind: str) -> int:
    return {
        "home": 8,
        "blog": 6,
        "techtopics": 6,
        "post": 3,
        "tool": 3,
        "software-detail": 3,
    }.get(kind, 4)


def gallery_html(page_key: str, kind: str = "blog") -> str:
    """Clickable image cards with fresh tech context, rotated per page."""
    count = min(_gallery_count(kind), len(IMAGES))
    offset = sum(ord(ch) for ch in page_key) % len(IMAGES)
    picked = [IMAGES[(offset + i) % len(IMAGES)] for i in range(count)]
    cards = []
    for img in picked:
        loading = "lazy"
        cards.append(
            f'      <a class="dih-gallery-card" href="{escape(img["href"])}">\n'
            f'        <span class="dih-gallery-media">\n'
            f'          <img src="{escape(card_url(img["id"]))}" alt="{escape(img["alt"])}" '
            f'width="{CARD_W}" height="{CARD_H}" loading="{loading}" decoding="async">\n'
            f'          <span class="dih-gallery-tag">{escape(img["tag"])}</span>\n'
            f'        </span>\n'
            f'        <span class="dih-gallery-body">\n'
            f'          <strong>{escape(img["title"])}</strong>\n'
            f'          <span>{escape(img["blurb"])}</span>\n'
            f'          <em>{escape(img["cta"])} &rarr;</em>\n'
            f'        </span>\n'
            f'      </a>'
        )
    return f"""<!-- DIH:GALLERY -->
<section class="dih-gallery" aria-labelledby="dihGalleryTitle">
  <div class="dih-gallery-head">
    <div>
      <span class="dih-gallery-eyebrow">Visual briefing</span>
      <h2 id="dihGalleryTitle">Technology, in focus</h2>
      <p>Fast context on the ideas shaping the industry, with a guide for every one.</p>
    </div>
    <a class="dih-gallery-all" href="/techtopics">All 30 tech guides <span aria-hidden="true">&rarr;</span></a>
  </div>
  <div class="dih-gallery-grid">
{chr(10).join(cards)}
  </div>
  <p class="dih-gallery-credit">Photography by Unsplash contributors. Cards link to related Digital Infohub guides.</p>
</section>
<!-- /DIH:GALLERY -->"""


def ambient_html(page_key: str) -> str:
    image_id = image_key_for(page_key)
    url = escape(ambient_url(image_id))
    return (
        '<!-- DIH:AMBIENT -->\n'
        f'<div class="dih-ambient" aria-hidden="true" style="--dih-ambient:url(\'{url}\')"></div>\n'
        '<!-- /DIH:AMBIENT -->'
    )
