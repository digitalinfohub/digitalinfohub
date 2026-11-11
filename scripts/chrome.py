#!/usr/bin/env python3
"""Shared site chrome (header, footer, explore block) for Digital Infohub.

Imported by apply_site.py, build_topics.py and build_post.py so every page
family renders exactly the same navigation, footer and design assets.
"""
from html import escape

SITE = "https://digitalinfohub.net"

NAV = [
    ("/", "Home"),
    ("/digi", "Digi"),
    ("/blog", "Blog"),
    ("/techtopics", "Tech Topics"),
    ("/software", "Software"),
    ("/techproducts", "Tech Products"),
    ("/games", "Games"),
    ("/coincompass", "Markets"),
]

TARGETS = {
    "/": ("🏠", "Homepage", "Today's tech briefing, tools and market pulse."),
    "/digi": ("✨", "Digi AI guide", "Ask anything — tech, markets, design or everyday life."),
    "/blog": ("📝", "Blog & analysis", "Deep dives on AI, hardware, markets and digital culture."),
    "/techtopics": ("🔬", "Tech Topics", "Plain-language guides to the technology shaping business."),
    "/software": ("🛠️", "Software & tools", "Free AI assistants and browser utilities that run locally."),
    "/techproducts": ("💻", "Tech Products", "Hands-on buying guidance for work, creativity and play."),
    "/games": ("🎮", "Pixel Palace", "Free arcade games, playable on desktop and mobile."),
    "/coincompass": ("🧭", "CoinCompass", "Track crypto and market context in one place."),
    "/news": ("📰", "Tech News", "Live headlines from the industry, updated through the day."),
    "/quiz": ("🎯", "Tech Quiz", "Six quick quizzes with a grade for every topic."),
    "/subscribe": ("✉️", "Subscribe", "Weekly tech intelligence in your inbox, free."),
    "/about": ("ℹ️", "About", "Who builds Digital Infohub and why."),
    "/services": ("🧰", "Services", "Automation, AI integration and custom builds."),
    "/advertise": ("📣", "Advertise", "Reach an audience of tech professionals and founders."),
    "/privacy-policy": ("🔒", "Privacy", "How Digital Infohub handles your data."),
    "/contact": ("✉️", "Contact", "Questions about services, advertising or the site? Send a message."),
}

EXPLORE = {
    "blog": ["/techtopics", "/software", "/coincompass", "/subscribe"],
    "techtopics": ["/blog", "/software", "/techproducts", "/subscribe", "/quiz", "/news"],
    "software": ["/blog", "/techtopics", "/coincompass", "/games"],
    "software-detail": ["/software", "/blog", "/techtopics", "/games"],
    "techproducts": ["/blog", "/software", "/techtopics", "/games"],
    "games": ["/software", "/blog", "/coincompass", "/techtopics"],
    "about": ["/services", "/blog", "/advertise", "/subscribe"],
    "services": ["/about", "/software", "/advertise", "/subscribe"],
    "advertise": ["/services", "/about", "/subscribe", "/blog"],
    "subscribe": ["/blog", "/techtopics", "/software", "/games"],
    "coincompass": ["/blog", "/techtopics", "/software", "/subscribe"],
    "news": ["/quiz", "/blog", "/techtopics", "/subscribe"],
    "quiz": ["/techtopics", "/news", "/blog", "/software"],
    "privacy": ["/about", "/subscribe", "/blog", "/services"],
    "tool": ["/software", "/blog", "/techtopics", "/coincompass"],
    "post": ["/blog", "/techtopics", "/software", "/subscribe"],
}

_HEADINGS = {
    "blog": "Keep reading, keep building",
    "techtopics": "Go deeper on the tech that matters",
    "software": "Put these tools to work",
    "software-detail": "More from the software suite",
    "techproducts": "Research before you buy",
    "games": "Take a five-minute break",
    "about": "Get to know the hub",
    "services": "Build something with us",
    "advertise": "Grow with Digital Infohub",
    "subscribe": "Never miss a signal",
    "coincompass": "Follow the money",
    "privacy": "Explore the hub",
    "tool": "More free tools",
    "post": "Keep the momentum",
    "news": "Turn headlines into understanding",
    "quiz": "Find your next rabbit hole",
}

_SUBS = {
    "blog": "One more article, guide or tool before you go.",
    "techtopics": "Guides that make you the most informed person in the room.",
    "software": "Free tools with no signup, no install and no tracking.",
    "software-detail": "Every tool in the suite is free and runs in your browser.",
    "techproducts": "Product guides, industry analysis and tools worth your time.",
    "games": "Fresh guides and tools while you recharge.",
    "about": "The rest of the hub, in one click.",
    "services": "See how we work, who we work with and what we build.",
    "advertise": "Audience, formats and the stories that perform.",
    "subscribe": "Start with today's briefing, then pick your rabbit hole.",
    "coincompass": "Market context plus the analysis behind the moves.",
    "privacy": "Everything else Digital Infohub publishes.",
    "tool": "Ten more browser tools are waiting in the suite.",
    "post": "Related guides, tools and analysis from the hub.",
    "news": "The story behind the headline is usually a guide away.",
    "quiz": "A score is useful. Knowing what to read next is better.",
}


def header_html(prefix: str = "") -> str:
    """Shared sticky header. `prefix` is kept for future relative-path use."""
    nav = "\n".join(
        f'      <a class="dih-link" href="{href}">{escape(label)}</a>'
        for href, label in NAV
    )
    drawer = "\n".join(
        f'      <a class="dih-drawer-link" href="{href}">{escape(label)}</a>'
        for href, label in NAV
    )
    return f"""<!-- DIH:HEADER -->
<header class="dih-header">
  <div class="dih-header-inner">
    <a class="dih-brand" href="/" aria-label="Digital Infohub home">
      <img src="/assets/logo.png" alt="Digital Infohub logo" width="36" height="36">
      <span class="dih-brand-text">Digital <b>Infohub</b></span>
    </a>
    <nav class="dih-nav" data-dih-nav aria-label="Primary navigation">
{nav}
    </nav>
    <div class="dih-actions">
      <a class="dih-tools" href="/software#tools" title="Free browser tools" aria-label="Free browser tools">⚡<span>Tools</span></a>
      <button class="dih-icon" type="button" data-dih-theme aria-label="Switch theme" title="Switch theme">☀</button>
      <a class="dih-cta" href="/subscribe">Subscribe</a>
      <button class="dih-burger" id="dihBurger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="dihDrawer"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="dih-drawer" id="dihDrawer" aria-label="Site menu">
  <div class="dih-drawer-panel">
    <div class="dih-drawer-grid">
{drawer}
    </div>
    <div class="dih-drawer-sub">
      <a class="dih-drawer-link" href="/news">📰 Tech News</a>
      <a class="dih-drawer-link" href="/quiz">🎯 Tech Quiz</a>
      <a class="dih-drawer-link" href="/software#tools">⚡ Tools</a>
      <a class="dih-drawer-link" href="/services">🧰 Services</a>
      <a class="dih-drawer-link" href="/contact">✉️ Contact</a>
    </div>
    <a class="dih-drawer-cta" href="/subscribe">✉️ Subscribe — weekly tech intel</a>
    <p class="dih-drawer-note">Digital Infohub · Tech for everyone, with a guide for every question.</p>
  </div>
</div>
<!-- /DIH:HEADER -->"""


def explore_html(kind: str = "blog") -> str:
    keys = EXPLORE.get(kind, EXPLORE["blog"])
    title = _HEADINGS.get(kind, "Keep exploring")
    sub = _SUBS.get(kind, "More from Digital Infohub.")
    cards = []
    for href in keys:
        icon, label, desc = TARGETS[href]
        cards.append(
            f'      <a class="dih-explore-card" href="{href}">\n'
            f'        <span class="dih-explore-icon" aria-hidden="true">{icon}</span>\n'
            f'        <strong>{escape(label)}</strong>\n'
            f'        <span>{escape(desc)}</span>\n'
            f'        <em>Explore →</em>\n'
            f'      </a>'
        )
    return f"""<!-- DIH:EXPLORE -->
<section class="dih-explore" aria-labelledby="dihExploreTitle">
  <div class="dih-explore-head">
    <h2 id="dihExploreTitle">{escape(title)}</h2>
    <p>{escape(sub)}</p>
  </div>
  <div class="dih-explore-grid">
{chr(10).join(cards)}
  </div>
</section>
<!-- /DIH:EXPLORE -->"""


def footer_html() -> str:
    return """<!-- DIH:FOOTER -->
<footer class="dih-footer">
  <div class="dih-footer-inner">
    <div class="dih-footer-brand">
      <a class="dih-brand" href="/" aria-label="Digital Infohub home">
        <img src="/assets/logo.png" alt="Digital Infohub logo" width="40" height="40">
        <span class="dih-brand-text">Digital <b>Infohub</b></span>
      </a>
      <p>The independent tech hub for everyone: AI research, market moves, practical guides, free tools and Digi, your AI guide.</p>
      <span class="dih-pill"><span class="dih-dot"></span> Updated daily</span>
    </div>
    <div class="dih-footer-col">
      <h3>Explore</h3>
      <a href="/blog">Blog &amp; analysis</a>
      <a href="/techtopics">Tech Topics</a>
      <a href="/software">Software &amp; tools</a>
      <a href="/techproducts">Tech Products</a>
      <a href="/games">Pixel Palace</a>
      <a href="/digi">Digi AI guide</a>
      <a href="/news">Live tech news</a>
      <a href="/quiz">Tech quiz</a>
    </div>
    <div class="dih-footer-col">
      <h3>Company</h3>
      <a href="/about">About</a>
      <a href="/services">Services</a>
      <a href="/advertise">Advertise</a>
      <a href="/coincompass">CoinCompass</a>
      <a href="/privacy-policy">Privacy</a>
    </div>
    <div class="dih-footer-col dih-footer-cta">
      <h3>Stay ahead</h3>
      <p>One email a week: the AI, market and software stories that actually matter.</p>
      <a class="dih-btn dih-btn-primary" href="/subscribe">Subscribe free</a>
    </div>
  </div>
  <div class="dih-footer-bottom">
    <span>© 2026 Digital Infohub · Independent technology publication</span>
    <nav aria-label="Footer links">
      <a href="/blog">Blog</a>
      <a href="/techtopics">Guides</a>
      <a href="/software">Tools</a>
      <a href="/contact">Contact</a>
      <a href="/sitemap.xml">Sitemap</a>
    </nav>
  </div>
</footer>
<!-- /DIH:FOOTER -->"""


def script_tag() -> str:
    return '<script src="/assets/site.js" defer></script>'
