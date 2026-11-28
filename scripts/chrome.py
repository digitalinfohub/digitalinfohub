#!/usr/bin/env python3
"""Shared site chrome (header, footer, explore block) for Digital Infohub.

Imported by apply_site.py, build_topics.py and build_post.py so every page
family renders exactly the same navigation, footer and design assets.
"""
from html import escape

SITE = "https://digitalinfohub.net"

NAV = [
    ("/", "Home"),
    ("/blog", "Blog"),
    ("/techtopics", "Tech Topics"),
    ("/software", "Software"),
    ("/games", "Games"),
    ("/vr", "VR"),
    ("/coincompass", "Markets"),
    ("/app", "More"),
]

DRAWER = [
    ("/", "Home"),
    ("/digi", "Digi"),
    ("/blog", "Blog"),
    ("/techtopics", "Tech Topics"),
    ("/software", "Software"),
    ("/techproducts", "Tech Products"),
    ("/games", "Games"),
    ("/vr", "VR"),
    ("/coincompass", "Markets"),
    ("/app", "More"),
]

TARGETS = {
    "/": ("🏠", "Homepage", "Today's tech briefing, tools and market pulse."),
    "/digi": ("✨", "Digi AI guide", "Ask anything — tech, markets, design or everyday life."),
    "/blog": ("📝", "Blog & analysis", "Deep dives on AI, hardware, markets and digital culture."),
    "/techtopics": ("🔬", "Tech Topics", "Clear guides to the technology shaping business."),
    "/terminal": ("⌨️", "Terminal mode", "Browse the whole hub as a Linux-like shell."),
    "/software/tedori": ("🇯🇵", "手取り計算", "給与の手取りをブラウザで概算。"),
    "/software/furusato": ("🎁", "ふるさと納税", "寄付の限度額をシミュレーション。"),
    "/software/rirekisho": ("📄", "履歴書メーカー", "JIS様式の履歴書を作成・印刷。"),
    "/software/seikyusho": ("🧾", "請求書メーカー", "インボイス対応の請求書を作成。"),
    "/software/kakutei": ("🗂️", "確定申告チェック", "必要書類と期限を診断。"),
    "/software/invoice": ("💵", "Invoice generator", "Freelance invoices with tax and PDF export."),
    "/software/loan": ("🏦", "Loan calculator", "Repayments, interest and an amortisation table."),
    "/software/timezone": ("🌍", "Meeting planner", "Find an hour that works across time zones."),
    "/software/resume": ("📑", "Résumé builder", "An ATS-friendly CV you can print or export."),
    "/software/seo-preview": ("🔎", "SEO preview", "Check titles, descriptions and social cards."),
    "/games/snake": ("🐍", "Snake", "The classic, on its own page."),
    "/games/2048": ("🔢", "2048", "Merge the tiles on a dedicated page."),
    "/software": ("🛠️", "Software & tools", "Free AI assistants and browser utilities that run locally."),
    "/techproducts": ("💻", "Tech Products", "Hands-on buying guidance for work, creativity and play."),
    "/games": ("🎮", "Pixel Palace", "Free arcade games, playable on desktop and mobile."),
    "/vr": ("🥽", "VR hub", "Every VR game and walk-in experience in one place."),
    "/vrgames": ("🎯", "VR games", "Three WebXR games for a headset, desktop or phone."),
    "/vrexperiences": ("🖼️", "VR experiences", "Walk-in 3D places, starting with Artify Space."),
    "/coincompass": ("🧭", "CoinCompass", "Track crypto and market context in one place."),
    "/news": ("📰", "Tech News", "Live headlines from the industry, updated through the day."),
    "/quiz": ("🎯", "Tech Quiz", "Six quick quizzes with a grade for every topic."),
    "/app": ("📲", "Install the app", "Home-screen app, offline pages and the QR code."),
    "/extension": ("🧩", "Chrome extension", "News, markets and weather from your toolbar."),
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
    "app": ["/extension", "/software", "/techtopics", "/subscribe"],
    "extension": ["/app", "/news", "/coincompass", "/software"],
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
    "app": "Install it once, keep the hub close",
    "extension": "The hub, one click from any tab",
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
    "app": "Home screen, offline pages, no app store.",
    "extension": "News, markets and weather without leaving your work.",
}


def header_html(prefix: str = "") -> str:
    """Shared sticky header. `prefix` is kept for future relative-path use."""
    nav = "\n".join(
        f'      <a class="dih-link" href="{href}">{escape(label)}</a>'
        for href, label in NAV
    )
    drawer = "\n".join(
        f'      <a class="dih-drawer-link" href="{href}">{escape(label)}</a>'
        for href, label in DRAWER
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
      <a class="dih-icon dih-tools" href="/software#tools" title="Free browser tools" aria-label="Free browser tools">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2 5 14h5l-1 8 8-12h-5l1-8Z"/></svg>
      </a>
      <a class="dih-icon dih-term" href="/terminal" title="Terminal mode — browse like a shell" aria-label="Open terminal mode">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="3"/><path d="m7 9 3 3-3 3"/><path d="M13 15h4"/></svg>
      </a>
      <button class="dih-icon dih-sound" type="button" data-dih-sound aria-label="Sound on — tap to mute" aria-pressed="true" title="Sound on — tap to mute (Shift+S)">
        <svg class="on" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4Z"/><path d="M16.5 8.5a5 5 0 0 1 0 7"/><path d="M19 6a8.5 8.5 0 0 1 0 12"/></svg>
        <svg class="off" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4Z"/><path d="m16 9 5 6"/><path d="m21 9-5 6"/></svg>
      </button>
      <button class="dih-icon dih-share" type="button" data-dih-share aria-label="Share this page" title="Share this page">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12v7a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-7"/><path d="M12 3v13"/><path d="m7 8 5-5 5 5"/></svg>
      </button>
      <button class="dih-icon dih-theme" type="button" data-dih-theme aria-label="Switch theme" title="Switch theme">
        <svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
        <svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A8.5 8.5 0 1 1 11.2 3a6.6 6.6 0 0 0 9.8 9.8Z"/></svg>
      </button>
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
      <a class="dih-drawer-link" href="/vr">🥽 VR hub</a>
      <a class="dih-drawer-link" href="/vrgames">🎯 VR games</a>
      <a class="dih-drawer-link" href="/vrexperiences">🖼️ VR experiences</a>
      <a class="dih-drawer-link" href="/services">🧰 Services</a>
      <a class="dih-drawer-link" href="/terminal">⌨️ Terminal mode</a>
      <a class="dih-drawer-link" href="/terminal#interest">📊 Most opened pages</a>
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
      <a href="/terminal">Terminal mode</a>
      <a href="/techproducts">Tech Products</a>
      <a href="/games">Pixel Palace</a>
      <a href="/vr">VR &amp; AR</a>
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
      <a href="/terminal">Terminal</a>
      <a href="/vr">VR</a>
      <a href="/sitemap.xml">Sitemap</a>
    </nav>
  </div>
</footer>
<!-- /DIH:FOOTER -->"""


def script_tag() -> str:
    return '<script src="/assets/site.js" defer></script>'
