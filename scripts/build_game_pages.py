#!/usr/bin/env python3
"""Build the standalone game pages at /games/<slug>.html.

Each page is its own indexable URL with the shared arcade engine, how-to-play
copy, an FAQ and VideoGame structured data. Run after changing game copy:

  python3 scripts/build_game_pages.py
  python3 scripts/apply_site.py games/snake.html   # inject shared chrome
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "games"
SITE = "https://digitalinfohub.net"

GAMES = [
    {
        "slug": "snake", "name": "Snake", "cat": "Arcade", "icon": "🐍",
        "title": "Snake — Play the Classic Browser Game Free | Digital Infohub",
        "desc": "Play Snake in your browser: eat, grow and avoid your own tail. Arrow keys, WASD or swipe on mobile, with a saved high score. No download, no signup.",
        "tagline": "The one everybody knows, with a clean board and a saved high score.",
        "howto": ["Use the arrow keys or W A S D to steer.", "Eat the red dot to grow and add 10 points.", "The snake speeds up as you score — plan two moves ahead.", "Swipe on a phone; press Space to restart after a crash."],
        "faq": [("Why does it get faster?", "Each dot shortens the gap between moves, up to a floor of 65 ms. It keeps the last minute tense without becoming unplayable."), ("Is the high score saved?", "Yes, in your browser's local storage. Nothing is sent to a server.")],
        "best": "Score",
    },
    {
        "slug": "2048", "name": "2048", "cat": "Puzzle", "icon": "🔢",
        "title": "2048 — Play the Number Puzzle Online | Digital Infohub",
        "desc": "Play 2048 free in your browser. Slide tiles, merge matching numbers and chase the 2048 square. Works with keyboard or swipe, high score saved on your device.",
        "tagline": "Slide, merge, repeat. The puzzle that quietly eats ten minutes.",
        "howto": ["Slide all tiles with the arrow keys, W A S D or a swipe.", "Two equal tiles merge into one when they collide.", "Every move drops a new 2 or 4 on the board.", "The run ends when the board is full and nothing can merge."],
        "faq": [("What is a good score?", "Passing 10,000 is a solid run; reaching the 2048 tile usually needs 20,000 or more."), ("Any strategy?", "Keep your largest tile in one corner and build rows in a single direction.")],
        "best": "Score",
    },
    {
        "slug": "pong", "name": "Pong", "cat": "Arcade", "icon": "🏓",
        "title": "Pong — Play Against the Computer | Digital Infohub",
        "desc": "Play Pong free in your browser. Move your paddle with the mouse, touch or arrow keys and beat the computer to seven points. No download or signup.",
        "tagline": "First to seven. The computer does not get tired.",
        "howto": ["Move your paddle with the mouse, a finger or ↑ ↓.", "The ball speeds up slightly on every hit.", "First player to seven points wins the match.", "The computer follows the ball with a little wobble — aim for the edges."],
        "faq": [("Can I play on a phone?", "Yes. Drag a finger on the board to move the paddle."), ("Why does the ball curve?", "Hitting the ball away from the paddle centre adds angle, exactly like the original.")],
        "best": "Wins",
    },
    {
        "slug": "memory", "name": "Memory", "cat": "Puzzle", "icon": "🧠",
        "title": "Memory Match — Free Card Matching Game | Digital Infohub",
        "desc": "Flip cards and match eight pairs in as few moves as possible. A calm memory game for a two-minute break, playable on desktop and mobile.",
        "tagline": "Eight pairs, sixteen cards, one short-term memory.",
        "howto": ["Click or tap a card to flip it.", "Flip a second card — a match stays open, a miss flips back.", "Clear all eight pairs to finish.", "Fewer moves is better than faster clicks."],
        "faq": [("Is there a time limit?", "No. The move counter is the score, so take your time."), ("Does it work offline?", "Once the page has loaded, yes — the game runs entirely in the browser.")],
        "best": "Moves",
    },
    {
        "slug": "mole", "name": "Whack-a-mole", "cat": "Reflex", "icon": "🐹",
        "title": "Whack-a-Mole — 30-Second Reflex Game | Digital Infohub",
        "desc": "Thirty seconds, nine holes, one very fast mole. Tap or click as many as you can before the timer runs out. Free, no signup, works on touch.",
        "tagline": "Thirty seconds. It speeds up. Good luck.",
        "howto": ["Tap a hole when the mole appears.", "Each hit is one point.", "The mole speeds up as the clock runs down.", "The game ends after thirty seconds."],
        "faq": [("Does a miss cost points?", "No, but the mole moves on, so a slow tap is a lost opportunity."), ("Can I pause?", "No — the thirty seconds run continuously. Restart to try again.")],
        "best": "Score",
    },
    {
        "slug": "reaction", "name": "Reaction test", "cat": "Reflex", "icon": "⚡",
        "title": "Reaction Time Test — Measure Your Reflexes | Digital Infohub",
        "desc": "Measure your reaction time in milliseconds over five tries. Click when the pad turns green — the average and your best are shown at the end.",
        "tagline": "How fast are you, honestly? Five tries, one average.",
        "howto": ["Click the pad to arm the test.", "Wait for it to turn green — clicking early counts as a miss.", "Click as soon as it changes.", "Five tries produce your average and best time."],
        "faq": [("What is a normal reaction time?", "Most adults land between 200 and 300 ms on a screen. Under 200 ms is quick."), ("Why was my first try slower?", "Anticipation helps. The delay is randomised so you cannot predict the green.")],
        "best": "Best",
    },
    {
        "slug": "simon", "name": "Simon", "cat": "Memory", "icon": "🎵",
        "title": "Simon — Repeat the Sequence Game | Digital Infohub",
        "desc": "Watch the four pads light up, then repeat the pattern. Each round adds one step. A free memory and attention game with sound.",
        "tagline": "Four pads, one growing pattern. How long can you follow?",
        "howto": ["Press Restart and watch the first pad light up.", "Repeat the sequence by clicking the pads in order.", "Each successful round adds one more step.", "One wrong pad ends the run."],
        "faq": [("Is there sound?", "Yes, a soft tone per pad, controlled by the sound switch in the header (Shift+S)."), ("How is the best score kept?", "The furthest level is stored in your browser, not on a server.")],
        "best": "Level",
    },
    {
        "slug": "tictactoe", "name": "Tic-tac-toe", "cat": "Versus", "icon": "❌",
        "title": "Tic-tac-toe vs the Computer — Free Game | Digital Infohub",
        "desc": "Play tic-tac-toe against an unbeatable computer. You are X; the best you can get is a draw. A quick test of opening moves and forks.",
        "tagline": "You are X. The machine does not lose. A draw is a win.",
        "howto": ["You play X and move first.", "The computer answers instantly with a perfect move.", "Three in a row wins; a full board is a draw.", "Start in a corner to make the machine work."],
        "faq": [("Can I win?", "Not against perfect play. A draw is the best possible result, which is the point of the puzzle."), ("Why does it take the centre?", "The centre is part of more winning lines than any other square.")],
        "best": "Wins",
    },
    {
        "slug": "typing", "name": "Typing rush", "cat": "Skill", "icon": "⌨️",
        "title": "Typing Speed Test — 60 Seconds, WPM & Accuracy | Digital Infohub",
        "desc": "Test your typing speed in a 60-second run. See words per minute update live, track accuracy and compare runs. Free, no signup, keyboard only.",
        "tagline": "Sixty seconds of honest WPM, with accuracy attached.",
        "howto": ["Click the box and start typing the passage.", "The timer begins on your first keystroke.", "Green is correct, red is a typo — accuracy matters as much as speed.", "Your WPM and accuracy appear when the minute ends."],
        "faq": [("How is WPM calculated?", "Characters typed divided by five, then scaled to a minute — the standard word length."), ("Are mistakes penalised?", "They are counted in the accuracy figure. Keep it above 95% before chasing speed.")],
        "best": "WPM",
    },
]

HEAD = """<!DOCTYPE html>
<html lang="en" data-theme="dark" data-dih="">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5443646750699471" crossorigin="anonymous"></script>
<link rel="stylesheet" href="/assets/hub.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body data-page="games">

<main class="hub-app">
  <header class="hub-app-head">
    <span class="dih-eyebrow">Pixel Palace · {cat}</span>
    <h1>{name}</h1>
    <p>{tagline}</p>
  </header>

  <section class="hub-card" aria-label="{name} game">
    <div id="game" data-arcade="{slug}">
      <noscript><p>This game needs JavaScript. The rest of the page still works without it.</p></noscript>
    </div>
  </section>

  <div class="hub-grid" style="margin-top:14px">
    <section class="hub-card" aria-labelledby="howTitle">
      <h2 id="howTitle">How to play</h2>
      <ol style="margin:0;padding-left:18px;font-size:12.5px;line-height:1.7;color:var(--dih-text-sub)">
{howto}
      </ol>
      <p class="hub-note" style="margin-top:10px">All games run locally: no account, no downloads, nothing uploaded. Scores are saved in this browser only.</p>
    </section>
    <aside class="hub-card" aria-labelledby="moreTitle">
      <h2 id="moreTitle">More from the arcade</h2>
      <div style="display:grid;gap:6px">
{more}
      </div>
      <a class="hub-btn is-ghost" href="/games" style="margin-top:10px">All nine games →</a>
    </aside>
  </div>

  <section class="hub-card" style="margin-top:14px" aria-labelledby="faqTitle">
    <h2 id="faqTitle">Questions</h2>
    <div class="hub-faq">
{faq}
    </div>
  </section>

  <div class="hub-ad" aria-label="Advertisement">
    <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-5443646750699471" data-ad-slot="8451723433" data-ad-format="auto" data-full-width-responsive="true"></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
  </div>

  <p class="hub-note">Related: <a href="/software">Free browser tools</a> · <a href="/terminal">Terminal mode</a> · <a href="/blog">Tech blog</a></p>
</main>

<script src="/assets/arcade.js" defer></script>
<script>
document.addEventListener('DOMContentLoaded', function () {{
  var mount = document.querySelector('[data-arcade]');
  if (!mount || !window.Arcade) return;
  window.Arcade.mount(mount.getAttribute('data-arcade'), mount);
}});
</script>
</body>
</html>
"""


def build(game):
    others = [g for g in GAMES if g["slug"] != game["slug"]][:4]
    more = "\n".join(
        f'        <a class="interest-card" href="/games/{g["slug"]}"><span class="interest-rank">{g["icon"]}</span>'
        f'<span class="interest-copy"><strong>{g["name"]}</strong><span>{g["cat"]}</span></span>'
        f'<span class="interest-arrow">→</span></a>'
        for g in others
    )
    howto = "\n".join(f"        <li>{h}</li>" for h in game["howto"])
    faq = "\n".join(
        f"      <details><summary>{q}</summary><p>{a}</p></details>" for q, a in game["faq"]
    )
    ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "VideoGame",
        "name": game["name"],
        "url": f"{SITE}/games/{game['slug']}",
        "description": game["desc"],
        "genre": game["cat"],
        "gamePlatform": "Web browser",
        "playMode": "SinglePlayer",
        "applicationCategory": "Game",
        "operatingSystem": "Any",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "inLanguage": "en",
        "publisher": {"@type": "Organization", "name": "Digital Infohub", "url": SITE},
        "isPartOf": {"@type": "WebSite", "name": "Digital Infohub", "url": SITE},
    }, ensure_ascii=False, separators=(",", ":"))
    return HEAD.format(
        title=game["title"], desc=game["desc"], cat=game["cat"], name=game["name"],
        tagline=game["tagline"], howto=howto, more=more, faq=faq, ld=ld, slug=game["slug"],
    )


def main():
    OUT.mkdir(exist_ok=True)
    for game in GAMES:
        path = OUT / f"{game['slug']}.html"
        path.write_text(build(game), encoding="utf-8")
        print("wrote", path.relative_to(ROOT))
    print(f"{len(GAMES)} game pages")


if __name__ == "__main__":
    main()
