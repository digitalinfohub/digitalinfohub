#!/usr/bin/env python3
"""Generate the Tech Topic guide pages, the /techtopics index and sitemap.xml.

Usage:
  python3 scripts/build_topics.py            # rebuild every topic page + index + sitemap
  python3 scripts/build_topics.py robotics   # rebuild one topic page only

Content lives in scripts/topics_part*.py. Do not hand-edit the generated
<slug>.html files or techtopics.html; edit the data and rerun this script.
"""
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from topics_part1 import TOPICS as PART1  # noqa: E402
from topics_part2 import TOPICS as PART2  # noqa: E402
from topics_part3 import TOPICS as PART3  # noqa: E402
from topics_part4 import TOPICS as PART4  # noqa: E402
from topics_part5 import TOPICS as PART5  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://digitalinfohub.net"
SITE_NAME = "Digital Infohub"
LOGO = "https://static.wixstatic.com/media/94ccfe_dec2763dd58148e78d3d8aaef72cf2fe~mv2.png"
ADSENSE = "ca-pub-5443646750699471"
AD_SLOT = "8451723433"
UPDATED = "2026-11-04"
TODAY = date.today().isoformat()

from apply_site import process as apply_site_process  # noqa: E402
from images import TOPIC_IMAGES, share_url  # noqa: E402

ALL = PART1 + PART2 + PART3 + PART4 + PART5
TOPICS = {t["slug"]: t for t in ALL}

# Display order used on /techtopics (matches the original page order).
ORDER = [
    "artificialintelligence", "machinelearning", "blockchain", "cloudcomputing",
    "cybersecurity", "internetofthings", "quantumcomputing", "bigdata",
    "virtualreality", "5gnetworks", "apis", "devops", "opensource", "robotics",
    "edgecomputing", "web3", "semiconductors", "3dprinting", "biotechnology",
    "greentechnology", "digitaltwins", "zerotrustsecurity", "serverlesscomputing",
    "neuromorphiccomputing",
    "augmentedreality", "drones", "nanotechnology", "spacetechnology",
    "wearabletechnology", "smartcities",
]

CATEGORIES = ["Foundations", "Infrastructure", "Engineering", "Security", "Web3", "Hardware", "Emerging"]

BRIEF = {
    "artificialintelligence": "What AI is, how modern models learn, and where it already runs your day.",
    "machinelearning": "Learning from data: the three main approaches and why models fail.",
    "blockchain": "Shared ledgers, consensus and smart contracts, minus the marketing.",
    "cloudcomputing": "Renting compute, the three service models and the real cost drivers.",
    "cybersecurity": "The threats that matter and the controls that actually reduce risk.",
    "internetofthings": "Sensors, gateways and the security questions every device raises.",
    "quantumcomputing": "Qubits, error correction and the encryption migration you should plan.",
    "bigdata": "The five Vs, modern data pipelines and how raw volume becomes decisions.",
    "virtualreality": "VR, AR and mixed reality: what works today and what still holds it back.",
    "5gnetworks": "Speed, latency and density, plus the spectrum physics behind coverage maps.",
    "apis": "How software talks to software, and how to design contracts that last.",
    "devops": "CI/CD, infrastructure as code and the habits that make releases boring.",
    "opensource": "Licences, communities, contribution and the risk hiding in dependencies.",
    "robotics": "Sense, plan, act: how robots work and where autonomy still struggles.",
    "edgecomputing": "Why processing near the data wins on latency, bandwidth and privacy.",
    "web3": "Wallets, contracts and dApps, and which parts are real today.",
    "semiconductors": "How chips are fabricated and why the supply chain became strategic.",
    "3dprinting": "FDM, resin and metal printing, and when additive beats traditional.",
    "biotechnology": "Gene editing, biomanufacturing and the questions that come with them.",
    "greentechnology": "Clean generation, storage and efficiency, including the honest trade-offs.",
    "digitaltwins": "Live virtual models that predict and optimise physical systems.",
    "zerotrustsecurity": "Verify every request instead of trusting the network perimeter.",
    "serverlesscomputing": "Event-driven execution, per-request billing and the trade-offs.",
    "neuromorphiccomputing": "Brain-inspired chips that spend almost no power when idle.",
    "augmentedreality": "How AR overlays the real world, and where it is already useful.",
    "drones": "Flight, inspection and the rules that decide where UAVs can go.",
    "nanotechnology": "Engineering at the atomic scale, from chips to medicine.",
    "spacetechnology": "Cheaper launch, smarter satellites and the new space economy.",
    "wearabletechnology": "Health sensors, smart rings and ambient computing on the body.",
    "smartcities": "Urban sensors, digital twins and the trust problem.",
}

CSS = """
:root {
  --font: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease: cubic-bezier(0.22, 0.61, 0.36, 1);
  --radius: 12px;
  --radius-sm: 8px;
}

[data-theme="dark"] {
  --bg: #0a0a0a;
  --surface: #111111;
  --surface-2: #161616;
  --surface-3: #1a1a1a;
  --border: rgba(255,255,255,0.06);
  --border-strong: rgba(255,255,255,0.1);
  --text: #f5f5f5;
  --text-sub: #a1a1aa;
  --text-muted: #71717a;
  --accent: #6366f1;
  --accent-soft: rgba(99,102,241,0.1);
  --shadow: 0 4px 24px -6px rgba(0,0,0,0.4);
}

[data-theme="light"] {
  --bg: #fafafa;
  --surface: #ffffff;
  --surface-2: #f4f4f5;
  --surface-3: #e4e4e7;
  --border: rgba(0,0,0,0.06);
  --border-strong: rgba(0,0,0,0.12);
  --text: #0a0a0a;
  --text-sub: #52525b;
  --text-muted: #a1a1aa;
  --accent: #4f46e5;
  --accent-soft: rgba(79,70,229,0.08);
  --shadow: 0 4px 24px -6px rgba(0,0,0,0.08);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  transition: background 0.3s ease, color 0.3s ease;
}

.shell { max-width: 820px; margin: 0 auto; padding: 32px 24px 80px; }

/* NAVIGATION */
.nav-shell {
  position: sticky; top: 0; z-index: 100;
  background: var(--bg); border-bottom: 1px solid var(--border);
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
  margin: -32px -24px 32px; padding: 0 24px;
}
.nav-bar {
  max-width: 820px; margin: 0 auto;
  display: flex; align-items: center; justify-content: space-between;
  padding: 12px 0; gap: 16px;
}
.nav-links { display: flex; gap: 4px; align-items: center; overflow-x: auto; scrollbar-width: none; }
.nav-links::-webkit-scrollbar { display: none; }
.nav-link {
  padding: 8px 14px; background: none; border: 1px solid transparent;
  color: var(--text-sub); border-radius: 8px; cursor: pointer;
  font-size: 13px; font-weight: 500; text-decoration: none;
  transition: all 0.2s var(--ease); white-space: nowrap;
  font-family: inherit; display: flex; align-items: center; gap: 6px;
}
.nav-link:hover { color: var(--text); background: var(--surface-2); border-color: var(--border); }
.nav-link.active { color: var(--accent); background: var(--accent-soft); border-color: var(--accent); }
.nav-link:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }

.hamburger {
  display: none; width: 36px; height: 36px;
  border: 1px solid var(--border); background: var(--surface); color: var(--text-sub);
  border-radius: var(--radius-sm); cursor: pointer;
  align-items: center; justify-content: center;
  font-size: 18px; transition: all 0.2s var(--ease); flex-shrink: 0;
}
.hamburger:hover { color: var(--text); background: var(--surface-2); border-color: var(--border-strong); }

.mobile-menu {
  display: none; position: absolute; top: 100%; left: 0; right: 0;
  background: var(--surface); border-bottom: 1px solid var(--border);
  padding: 8px 16px 16px; flex-direction: column; gap: 4px;
  box-shadow: var(--shadow); animation: slideDown 0.2s var(--ease);
}
.mobile-menu.active { display: flex; }
.mobile-menu .nav-link { width: 100%; justify-content: flex-start; padding: 12px 14px; font-size: 14px; }
@keyframes slideDown { from { opacity: 0; transform: translateY(-8px); } to { opacity: 1; transform: translateY(0); } }

/* TOP BAR */
.topbar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 40px; }
.brand {
  display: flex; align-items: center; gap: 10px;
  font-weight: 700; font-size: 15px; letter-spacing: -0.01em;
  text-decoration: none; color: var(--text);
}
.brand-logo {
  width: 28px; height: 28px; border-radius: 8px;
  background: var(--surface-2); border: 1px solid var(--border);
  display: flex; align-items: center; justify-content: center; overflow: hidden;
}
.brand-logo img { width: 100%; height: 100%; object-fit: cover; display: block; }
.topbar-actions { display: flex; gap: 6px; align-items: center; }
.icon-btn {
  width: 36px; height: 36px; border: 1px solid var(--border);
  background: var(--surface); color: var(--text-sub);
  border-radius: var(--radius-sm); cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: all 0.2s var(--ease);
}
.icon-btn:hover { color: var(--text); border-color: var(--border-strong); background: var(--surface-2); }
.icon-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }

/* INDEX HEADER */
.page-header { margin-bottom: 32px; }
.page-title { font-size: 32px; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 12px; }
.page-desc { color: var(--text-sub); font-size: 16px; max-width: 620px; }
.page-desc a, .article a.inline { color: var(--accent); text-decoration: none; font-weight: 500; }
.page-desc a:hover, .article a.inline:hover { text-decoration: underline; }

.topic-jump { display: flex; flex-wrap: wrap; gap: 8px; margin: 24px 0 8px; }
.topic-jump a {
  font-size: 12px; font-weight: 600; color: var(--text-sub);
  border: 1px solid var(--border); background: var(--surface);
  border-radius: 99px; padding: 6px 12px; text-decoration: none;
  transition: all 0.2s var(--ease);
}
.topic-jump a:hover { color: var(--text); border-color: var(--accent); }

.topic-group { margin-top: 40px; }
.group-head {
  display: flex; align-items: baseline; justify-content: space-between;
  gap: 12px; padding-bottom: 12px; margin-bottom: 16px;
  border-bottom: 1px solid var(--border);
  scroll-margin-top: 90px;
}
.group-head h2 { font-size: 20px; font-weight: 700; letter-spacing: -0.01em; }
.group-count { font-family: var(--mono); font-size: 11px; color: var(--text-muted); }

/* TOPIC CARDS */
.topics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 16px;
}
.topic-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 24px;
  transition: all 0.25s var(--ease);
  display: flex; flex-direction: column; gap: 10px;
  position: relative; overflow: hidden;
  text-align: left; color: inherit; font-family: inherit; width: 100%;
  text-decoration: none;
}
.topic-card:hover {
  transform: translateY(-4px); border-color: var(--accent);
  box-shadow: var(--shadow);
}
.topic-card:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; transform: translateY(-4px); }
.topic-icon {
  width: 48px; height: 48px; border-radius: 12px;
  background: var(--surface-2); display: flex; align-items: center; justify-content: center;
  font-size: 24px; margin-bottom: 2px;
}
.topic-name { font-size: 18px; font-weight: 700; color: var(--text); }
.topic-brief { font-size: 13px; color: var(--text-muted); line-height: 1.5; }
.topic-more {
  font-size: 12px; font-weight: 600; color: var(--accent);
  margin-top: auto; padding-top: 6px;
}
.topic-arrow {
  position: absolute; top: 24px; right: 24px;
  color: var(--text-muted); opacity: 0; transition: opacity 0.2s; font-size: 18px;
}
.topic-card:hover .topic-arrow, .topic-card:focus-visible .topic-arrow { opacity: 1; color: var(--accent); }

/* ARTICLE */
.breadcrumb {
  display: flex; flex-wrap: wrap; align-items: center; gap: 8px;
  font-size: 12px; color: var(--text-muted); margin-bottom: 24px;
}
.breadcrumb a { color: var(--text-sub); text-decoration: none; }
.breadcrumb a:hover { color: var(--accent); }
.breadcrumb [aria-current] { color: var(--text); }

.article { max-width: 720px; margin: 0 auto; }
.article-head { margin-bottom: 28px; }
.topic-chip {
  display: inline-flex; align-items: center; gap: 8px;
  font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--accent); background: var(--accent-soft);
  border: 1px solid var(--border); border-radius: 99px;
  padding: 6px 12px; margin-bottom: 16px;
}
.article h1 {
  font-size: clamp(30px, 5vw, 40px); font-weight: 800;
  letter-spacing: -0.03em; line-height: 1.15; margin-bottom: 14px;
}
.article .lede { font-size: 17px; color: var(--text-sub); line-height: 1.65; margin-bottom: 18px; }
.article-meta {
  display: flex; flex-wrap: wrap; gap: 8px; align-items: center;
  font-family: var(--mono); font-size: 11px; color: var(--text-muted);
}
.article-meta .dot { opacity: 0.5; }

.toc {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 20px 24px; margin: 32px 0;
}
.toc h2 {
  font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em;
  color: var(--text-muted); margin-bottom: 12px; font-weight: 700;
}
.toc ol { margin: 0; padding-left: 20px; }
.toc li { margin-bottom: 6px; font-size: 14px; }
.toc a { color: var(--text-sub); text-decoration: none; }
.toc a:hover { color: var(--accent); text-decoration: underline; }

.article h2 {
  font-size: 24px; font-weight: 700; letter-spacing: -0.01em;
  margin: 40px 0 14px; scroll-margin-top: 90px;
}
.article h3 { font-size: 17px; font-weight: 700; margin: 0 0 8px; }
.article p { color: var(--text-sub); margin-bottom: 16px; font-size: 16px; line-height: 1.75; }
.article p strong { color: var(--text); font-weight: 600; }
.article ul, .article ol { margin: 0 0 20px 22px; color: var(--text-sub); font-size: 15px; }
.article li { margin-bottom: 8px; line-height: 1.6; }

.callout {
  border-left: 3px solid var(--accent);
  background: var(--accent-soft);
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  padding: 16px 20px; margin: 24px 0;
  color: var(--text); font-size: 15px; line-height: 1.65;
}

.facts {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px; margin: 20px 0 8px;
}
.fact {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius-sm); padding: 16px;
  font-size: 14px; color: var(--text-sub); line-height: 1.55;
}

.faq-item {
  border: 1px solid var(--border); background: var(--surface);
  border-radius: var(--radius-sm); padding: 18px 20px; margin-bottom: 12px;
}
.faq-item p { margin: 0; font-size: 15px; }

.prevnext { display: flex; gap: 12px; margin: 40px 0; }
.prevnext a {
  flex: 1; display: flex; flex-direction: column; gap: 4px;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 16px 18px;
  text-decoration: none; transition: all 0.2s var(--ease);
}
.prevnext a:hover { border-color: var(--accent); transform: translateY(-2px); }
.prevnext .pn-label { font-family: var(--mono); font-size: 10px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.08em; }
.prevnext .pn-name { font-size: 14px; font-weight: 600; color: var(--text); }
.prevnext a.next { text-align: right; align-items: flex-end; }

.article .related { margin-top: 40px; }
.article .related .topics-grid { grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); }
.article .related .topic-card { padding: 18px; gap: 8px; }
.article .related .topic-icon { width: 36px; height: 36px; font-size: 18px; border-radius: 9px; }
.article .related .topic-name { font-size: 15px; }

.source {
  margin-top: 32px; padding-top: 20px; border-top: 1px solid var(--border);
  font-size: 13px; color: var(--text-muted);
}
.source a { color: var(--accent); text-decoration: none; }
.source a:hover { text-decoration: underline; }

.explore { margin-top: 40px; }
.explore-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 10px; }
.explore-grid a {
  display: flex; align-items: center; gap: 10px;
  border: 1px solid var(--border); background: var(--surface);
  border-radius: var(--radius-sm); padding: 12px 14px;
  text-decoration: none; color: var(--text-sub); font-size: 13px; font-weight: 500;
  transition: all 0.2s var(--ease);
}
.explore-grid a:hover { border-color: var(--accent); color: var(--text); }

/* ADS */
.ad-box, .ad-box-inline {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 20px;
  display: flex; align-items: center; justify-content: center;
  overflow: hidden; margin: 32px 0; min-height: 120px;
}
.ad-box-inline { min-height: 140px; }
.ad-label {
  font-family: var(--mono); font-size: 10px; text-transform: uppercase;
  letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 8px; text-align: center;
}
.ad-box-ins { width: 100%; display: block; min-height: 100px; }

/* FOOTER */
.site-footer {
  margin-top: 56px; padding-top: 28px; border-top: 1px solid var(--border);
  display: flex; flex-wrap: wrap; gap: 12px 20px; align-items: center;
  justify-content: space-between; font-size: 13px; color: var(--text-muted);
}
.site-footer nav { display: flex; flex-wrap: wrap; gap: 14px; }
.site-footer a { color: var(--text-sub); text-decoration: none; }
.site-footer a:hover { color: var(--accent); }

@media (max-width: 640px) {
  .shell { padding: 20px 16px 60px; }
  .nav-shell { margin: -20px -16px 32px; padding: 0 16px; }
  .nav-links { display: none; }
  .hamburger { display: flex; }
  .page-title { font-size: 26px; }
  .topics-grid { grid-template-columns: 1fr 1fr; gap: 12px; }
  .topic-card { padding: 18px; }
  .topic-name { font-size: 15px; }
  .topic-icon { width: 40px; height: 40px; font-size: 20px; }
  .article h2 { font-size: 21px; margin-top: 32px; }
  .article p { font-size: 15.5px; }
  .prevnext { flex-direction: column; }
  .prevnext a.next { text-align: left; align-items: flex-start; }
}

@media (max-width: 380px) {
  .topics-grid { grid-template-columns: 1fr; }
}
"""

NAV_LINKS = [
    ("/", "🏠", "Home"),
    ("/blog", "📝", "Blog"),
    ("/techtopics", "💡", "Tech Topics"),
    ("/software", "💻", "Software"),
    ("/games", "🎮", "Games"),
    ("/subscribe", "✉️", "Subscribe"),
]

THEME_JS = """
(function() {
  'use strict';
  var sunSvg = '<circle cx="12" cy="12" r="4"></circle><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"></path>';
  var moonSvg = '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>';

  var theme = 'dark';
  try { theme = localStorage.getItem('dih_theme') || 'dark'; } catch (e) {}
  document.documentElement.setAttribute('data-theme', theme);

  var themeIcon = document.getElementById('themeIcon');
  if (themeIcon) themeIcon.innerHTML = theme === 'dark' ? sunSvg : moonSvg;

  var themeToggle = document.getElementById('themeToggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', function() {
      theme = theme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', theme);
      try { localStorage.setItem('dih_theme', theme); } catch (e) {}
      if (themeIcon) themeIcon.innerHTML = theme === 'dark' ? sunSvg : moonSvg;
    });
  }

  var hamburger = document.getElementById('hamburger');
  var mobileMenu = document.getElementById('mobileMenu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', function() {
      var isOpen = mobileMenu.classList.toggle('active');
      hamburger.textContent = isOpen ? '\\u00d7' : '\\u2630';
      hamburger.setAttribute('aria-expanded', isOpen);
    });
  }
})();
"""


def esc(value):
    return (value.replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def ad_block(label="Sponsored", inline=True):
    cls = "ad-box-inline" if inline else "ad-box"
    return (
        f'<div class="{cls}" role="complementary" aria-label="Advertisement">\n'
        f'  <div style="width:100%;">\n'
        f'    <div class="ad-label">{label}</div>\n'
        f'    <ins class="adsbygoogle ad-box-ins"\n'
        f'         style="display:block"\n'
        f'         data-ad-client="{ADSENSE}"\n'
        f'         data-ad-slot="{AD_SLOT}"\n'
        f'         data-ad-format="auto"\n'
        f'         data-full-width-responsive="true"></ins>\n'
        f'    <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>\n'
        f'  </div>\n'
        f'</div>'
    )


def nav_html(active_tech=True):
    items = []
    for href, icon, label in NAV_LINKS:
        cls = "nav-link active" if (active_tech and href == "/techtopics") else "nav-link"
        items.append(f'        <a href="{href}" class="{cls}">{icon} {label}</a>')
    links = "\n".join(items)
    return f'''  <nav class="nav-shell">
    <div class="nav-bar">
      <div class="nav-links">
{links}
      </div>
      <button class="hamburger" id="hamburger" aria-label="Menu" aria-expanded="false">☰</button>
    </div>
    <div class="mobile-menu" id="mobileMenu">
{links}
    </div>
  </nav>'''


def topbar_html():
    return f'''  <div class="topbar">
    <a href="/" class="brand" aria-label="{SITE_NAME} home">
      <span class="brand-logo">
        <img src="{LOGO}" alt="" loading="lazy" width="28" height="28">
      </span>
      <span>{SITE_NAME}</span>
    </a>
    <div class="topbar-actions">
      <button class="icon-btn" id="themeToggle" title="Toggle theme" aria-label="Toggle dark and light theme">
        <svg id="themeIcon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"></path></svg>
      </button>
    </div>
  </div>'''


def footer_html():
    return f'''  <footer class="site-footer">
    <span>&copy; {date.today().year} {SITE_NAME}. All rights reserved.</span>
    <nav aria-label="Site links">
      <a href="/">Home</a>
      <a href="/techtopics">Tech Topics</a>
      <a href="/blog">Blog</a>
      <a href="/about">About</a>
      <a href="/advertise">Advertise</a>
      <a href="/privacy-policy">Privacy</a>
      <a href="https://digitalinfohub.net/">Main site</a>
    </nav>
  </footer>'''


def head_html(title, description, url, image, keywords=None, og_type="article", extra_ld=None):
    ld_blocks = ""
    if extra_ld:
        for block in extra_ld:
            ld_blocks += ('<script type="application/ld+json">\n'
                          + json.dumps(block, ensure_ascii=False, indent=2)
                          + "\n</script>\n")
    kw = ""
    if keywords:
        kw = f'<meta name="keywords" content="{esc(", ".join(keywords))}">\n'
    full_title = f"{title} | {SITE_NAME}" if SITE_NAME not in title else title
    return f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">
{kw}<meta name="author" content="{SITE_NAME}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#0a0a0a">
<meta name="color-scheme" content="dark light">
<link rel="canonical" href="{url}">

<!-- Open Graph -->
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(title)}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(full_title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{image}">

<link rel="icon" type="image/png" href="{LOGO}">
<link rel="apple-touch-icon" href="{LOGO}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://pagead2.googlesyndication.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

<!-- AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE}" crossorigin="anonymous"></script>

{ld_blocks}<style>{CSS}</style>
</head>'''


def article_ld(t, url):
    return {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": t["title"],
        "description": t["meta"],
        "image": [share_url(TOPIC_IMAGES.get(t["slug"], "network"))],
        "url": url,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "datePublished": UPDATED,
        "dateModified": UPDATED,
        "inLanguage": "en",
        "isAccessibleForFree": True,
        "articleSection": t["category"],
        "keywords": ", ".join(t["keywords"]),
        "wordCount": word_count(t),
        "author": {"@type": "Organization", "name": SITE_NAME, "url": SITE + "/"},
        "publisher": {
            "@type": "Organization",
            "name": SITE_NAME,
            "url": SITE + "/",
            "logo": {"@type": "ImageObject", "url": LOGO},
        },
    }


def breadcrumb_ld(name, url):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Tech Topics", "item": SITE + "/techtopics"},
            {"@type": "ListItem", "position": 3, "name": name, "item": url},
        ],
    }


def faq_ld(t):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": item["q"],
                "acceptedAnswer": {"@type": "Answer", "text": item["a"]},
            }
            for item in t["faq"]
        ],
    }


def word_count(t):
    text = " ".join(t["intro"])
    for s in t["sections"]:
        text += " " + " ".join(s["p"]) + " " + " ".join(s.get("list", [])) + " " + s.get("callout", "")
    text += " " + " ".join(t["facts"])
    text += " " + " ".join(f['q'] + " " + f['a'] for f in t["faq"])
    return len(text.split())


def related_card(slug):
    r = TOPICS[slug]
    return f'''        <a class="topic-card" href="/{r["slug"]}">
          <div class="topic-icon" aria-hidden="true">{r["icon"]}</div>
          <div class="topic-name">{esc(r["name"])}</div>
          <div class="topic-brief">{esc(BRIEF[r["slug"]])}</div>
          <div class="topic-more">Read the guide &rarr;</div>
        </a>'''


def render_topic(t):
    url = f"{SITE}/{t['slug']}"
    share_image = share_url(TOPIC_IMAGES.get(t["slug"], "network"))
    read_mins = max(4, round(word_count(t) / 220))

    toc_items = "\n".join(
        f'      <li><a href="#{s["id"]}">{esc(s["h"])}</a></li>' for s in t["sections"]
    )

    body = []
    for i, s in enumerate(t["sections"]):
        body.append(f'    <h2 id="{s["id"]}">{esc(s["h"])}</h2>')
        for para in s["p"]:
            body.append(f'    <p>{esc(para)}</p>')
        if s.get("list"):
            body.append("    <ul>")
            for item in s["list"]:
                body.append(f"      <li>{esc(item)}</li>")
            body.append("    </ul>")
        if s.get("callout"):
            body.append(f'    <div class="callout">{esc(s["callout"])}</div>')
        if i == 1:
            body.append("    " + ad_block().replace("\n", "\n    "))
    body_html = "\n".join(body)

    facts = "\n".join(f'      <div class="fact">{esc(f)}</div>' for f in t["facts"])
    faq = "\n".join(
        f'      <div class="faq-item">\n        <h3>{esc(item["q"])}</h3>\n        <p>{esc(item["a"])}</p>\n      </div>'
        for item in t["faq"]
    )

    idx = ORDER.index(t["slug"])
    prev_slug = ORDER[idx - 1] if idx > 0 else None
    next_slug = ORDER[idx + 1] if idx < len(ORDER) - 1 else None
    pn = []
    if prev_slug:
        pn.append(f'    <a class="prev" href="/{prev_slug}">\n      <span class="pn-label">&larr; Previous topic</span>\n      <span class="pn-name">{esc(TOPICS[prev_slug]["name"])}</span>\n    </a>')
    if next_slug:
        pn.append(f'    <a class="next" href="/{next_slug}">\n      <span class="pn-label">Next topic &rarr;</span>\n      <span class="pn-name">{esc(TOPICS[next_slug]["name"])}</span>\n    </a>')
    prevnext = ""
    if pn:
        prevnext = '  <nav class="prevnext" aria-label="More tech topics">\n' + "\n".join(pn) + "\n  </nav>"

    related = "\n".join(related_card(s) for s in t["related"])

    return f'''{head_html(t["title"], t["meta"], url, share_image, t["keywords"],
                           extra_ld=[article_ld(t, url), breadcrumb_ld(t["name"], url), faq_ld(t)])}
<body>

<div class="shell">
{nav_html()}

{topbar_html()}

  <nav class="breadcrumb" aria-label="Breadcrumb">
    <a href="/">Home</a>
    <span aria-hidden="true">/</span>
    <a href="/techtopics">Tech Topics</a>
    <span aria-hidden="true">/</span>
    <span aria-current="page">{esc(t["name"])}</span>
  </nav>

  <article class="article">
    <header class="article-head">
      <span class="topic-chip"><span aria-hidden="true">{t["icon"]}</span> {esc(t["category"])} &middot; Tech Topics</span>
      <h1>{esc(t["title"])}</h1>
      <p class="lede">{esc(t["lede"])}</p>
      <div class="article-meta">
        <span>Updated {datetime.strptime(UPDATED, "%Y-%m-%d").strftime("%B %Y")}</span>
        <span class="dot">&middot;</span>
        <span>{read_mins} min read</span>
        <span class="dot">&middot;</span>
        <span>{SITE_NAME}</span>
      </div>
    </header>

    {ad_block()}

    <div class="toc">
      <h2>In this guide</h2>
      <ol>
{toc_items}
      </ol>
    </div>

{chr(10).join(f"    <p>{esc(p)}</p>" for p in t["intro"])}

{body_html}

    <h2 id="key-facts">Key facts at a glance</h2>
    <div class="facts">
{facts}
    </div>

    <h2 id="faq">Frequently asked questions</h2>
{faq}

    <div class="source">
      Further reading: <a href="{t["wiki"]}" target="_blank" rel="noopener noreferrer">Wikipedia &mdash; {esc(t["name"])}</a>
    </div>

{prevnext}

    <section class="related" aria-labelledby="related-heading">
      <h2 id="related-heading">Related tech topics</h2>
      <div class="topics-grid">
{related}
      </div>
    </section>

    <section class="explore" aria-labelledby="explore-heading">
      <h2 id="explore-heading">Keep exploring {SITE_NAME}</h2>
      <div class="explore-grid">
        <a href="/techtopics"><span aria-hidden="true">💡</span> All Tech Topics</a>
        <a href="/blog"><span aria-hidden="true">📝</span> Latest articles</a>
        <a href="/software"><span aria-hidden="true">💻</span> Free software</a>
        <a href="/games"><span aria-hidden="true">🎮</span> Play free games</a>
        <a href="/subscribe"><span aria-hidden="true">✉️</span> Newsletter</a>
      </div>
    </section>

    {ad_block()}
  </article>

{footer_html()}
</div>

<script>{THEME_JS}</script>
</body>
</html>
'''


def render_index():
    url = f"{SITE}/techtopics"
    title = "Tech Topics: Guides to AI, Cloud, Security and More"
    description = ("Explore plain-language guides to the technology shaping our world: AI, machine learning, "
                   "cloud, cybersecurity, quantum computing, robotics, blockchain and more.")
    groups = []
    jump = []
    for cat in CATEGORIES:
        members = [TOPICS[s] for s in ORDER if TOPICS[s]["category"] == cat]
        if not members:
            continue
        anchor = re.sub(r"[^a-z0-9]+", "-", cat.lower()).strip("-")
        jump.append(f'      <a href="#{anchor}">{cat}</a>')
        cards = "\n".join(
            f'''        <a class="topic-card" href="/{m["slug"]}" role="listitem">
          <div class="topic-icon" aria-hidden="true">{m["icon"]}</div>
          <div class="topic-name">{esc(m["name"])}</div>
          <div class="topic-brief">{esc(BRIEF[m["slug"]])}</div>
          <div class="topic-more">Read the guide &rarr;</div>
          <div class="topic-arrow" aria-hidden="true">&rarr;</div>
        </a>''' for m in members
        )
        groups.append(f'''    <section class="topic-group" aria-labelledby="{anchor}">
      <div class="group-head" id="{anchor}">
        <h2>{cat}</h2>
        <span class="group-count">{len(members)} guides</span>
      </div>
      <div class="topics-grid" role="list">
{cards}
      </div>
    </section>''')

    item_list = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Tech Topics guides",
        "url": url,
        "numberOfItems": len(ORDER),
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1,
             "name": TOPICS[s]["name"], "url": f"{SITE}/{s}"}
            for i, s in enumerate(ORDER)
        ],
    }
    collection = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": title,
        "description": description,
        "url": url,
        "isPartOf": {"@type": "WebSite", "name": SITE_NAME, "url": SITE + "/"},
        "publisher": {"@type": "Organization", "name": SITE_NAME, "url": SITE + "/"},
    }
    home_crumbs = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Tech Topics", "item": url},
        ],
    }

    return f'''{head_html(title, description, url,
                         share_url("circuit"),
                         keywords=["tech topics", "technology guides", "what is AI", "cloud computing",
                                   "cybersecurity", "quantum computing", "explained"],
                         og_type="website",
                         extra_ld=[collection, item_list, home_crumbs])}
<body>

<div class="shell">
{nav_html()}

{topbar_html()}

  <header class="page-header">
    <h1 class="page-title">Tech Topics</h1>
    <p class="page-desc">Plain-language guides to the ideas shaping our digital world. Every topic below has an in-depth guide covering how it works, where it is used and what to watch for. Start anywhere, or browse our <a href="/blog">latest articles</a> and <a href="/software">free software</a>.</p>
    <nav class="topic-jump" aria-label="Jump to a category">
{chr(10).join(jump)}
    </nav>
    <div class="dih-guide-actions">
      <a class="dih-guide-action primary" href="/quiz"><span aria-hidden="true">🎯</span><strong>Test yourself</strong><span>Six quick tech quizzes with a grade for every topic.</span></a>
      <a class="dih-guide-action" href="/news"><span aria-hidden="true">📰</span><strong>Live tech news</strong><span>Fresh headlines even when the blog is quiet.</span></a>
    </div>
  </header>

  {ad_block()}

{chr(10).join(groups)}

  {ad_block("Sponsored", inline=False)}

{footer_html()}
</div>

<script>{THEME_JS}</script>
</body>
</html>
'''


def build_topic(slug):
    if slug not in TOPICS:
        raise SystemExit(f"Unknown topic: {slug}")
    out = ROOT / f"{slug}.html"
    out.write_text(render_topic(TOPICS[slug]), encoding="utf-8")
    apply_site_process(out)
    print(f"built {out.name}")


def build_index():
    out = ROOT / "techtopics.html"
    out.write_text(render_index(), encoding="utf-8")
    apply_site_process(out)
    print("built techtopics.html")


def build_sitemap():
    urls = []

    def add(path, priority, changefreq="monthly", lastmod=TODAY):
        loc = SITE + "/" + path if path else SITE + "/"
        urls.append((loc, lastmod, changefreq, priority))

    for slug in ORDER:
        add(slug, "0.8", "monthly", UPDATED)
    add("techtopics", "0.9", "weekly", UPDATED)
    add("", "1.0", "daily")
    for hub in ["blog", "software", "techtopics", "games", "subscribe", "about", "advertise", "services", "contact", "techproducts", "coincompass", "digi", "expense-tracker", "pomodoro", "privacy-policy", "news", "quiz"]:
        if (ROOT / f"{hub}.html").exists():
            add(hub, "0.7", "weekly")
    for sub in ["software", "post"]:
        folder = ROOT / sub
        if folder.is_dir():
            for f in sorted(folder.glob("*.html")):
                mtime = datetime.fromtimestamp(f.stat().st_mtime).date().isoformat()
                add(f"{sub}/{f.stem}", "0.6" if sub == "software" else "0.7", "monthly", mtime)
    for f in sorted(ROOT.glob("tool-*.html")):
        mtime = datetime.fromtimestamp(f.stat().st_mtime).date().isoformat()
        add(f.stem, "0.5", "monthly", mtime)

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod, changefreq, priority in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append(f"    <changefreq>{changefreq}</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"built sitemap.xml ({len(urls)} urls)")

    robots = ROOT / "robots.txt"
    robots.write_text(
        "User-agent: *\nAllow: /\n\n"
        f"Sitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print("built robots.txt")


if __name__ == "__main__":
    args = sys.argv[1:]
    missing = [s for s in ORDER if s not in TOPICS]
    if missing:
        raise SystemExit("Missing topic data for: " + ", ".join(missing))
    if args:
        for a in args:
            build_topic(a)
    else:
        for s in ORDER:
            build_topic(s)
        build_index()
        build_sitemap()
