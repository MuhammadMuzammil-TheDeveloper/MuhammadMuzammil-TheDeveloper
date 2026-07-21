"""
Hand-author a neofetch-style info card SVG: a title bar, then colored
key/value rows that fade + slide in on a short stagger, like the panel
is printing next to the ASCII portrait.

Set STATIC=1 to emit a frozen (no-animation) frame for local Quick Look
previews.
"""
import os

STATIC = os.environ.get("STATIC") == "1"
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "info-card.svg")

# ---- Edit this block to update the card's content ----
TITLE_USER = "muzammil@github"
TITLE_PATH = "~"
NOW_ROLE = "Full Stack Developer"
PREV = "BSCS student, KIET (Karachi) - grad 2027"
STACK = "JS (ES6+), React, Tailwind, Firebase, Supabase, PostgreSQL, MySQL, WordPress"
HIGHLIGHTS = [
    "1st place - CODE JUNG 2025 (Web Dev)",
    "Top 5 - SMIT Hackathon 2025",
]
# --------------------------------------------------------

ACCENT = "#39d353"   # key color
FG = "#c9d1d9"       # value color
DIM = "#8b949e"      # separators / secondary text
BG = "transparent"

WIDTH = 490
LINE_H = 22
TOP_PAD = 42
LEFT_PAD = 18


def esc(s):
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def row(label, value, y, delay):
    style = "" if STATIC else f' style="animation-delay:{delay}s"'
    cls = "" if STATIC else ' class="line"'
    return (
        f'<g{cls}{style}>'
        f'<text x="{LEFT_PAD}" y="{y}" fill="{ACCENT}" font-weight="600">{esc(label)}</text>'
        f'<text x="{LEFT_PAD + 90}" y="{y}" fill="{FG}">{esc(value)}</text>'
        f'</g>'
    )


def build():
    lines = []
    y = TOP_PAD
    delay_step = 0.18
    delay = 0.0

    lines.append(row("Now", NOW_ROLE, y, delay)); y += LINE_H; delay += delay_step
    lines.append(row("Prev", PREV, y, delay)); y += LINE_H; delay += delay_step
    lines.append(row("Stack", STACK[:0], y, delay))  # placeholder replaced below

    # Stack tends to be long; wrap it manually across up to 2 lines.
    max_chars = 46
    stack_lines = []
    words = STACK.split(", ")
    cur = ""
    for w in words:
        candidate = (cur + ", " + w) if cur else w
        if len(candidate) > max_chars and cur:
            stack_lines.append(cur)
            cur = w
        else:
            cur = candidate
    if cur:
        stack_lines.append(cur)

    lines[-1] = row("Stack", stack_lines[0], y, delay)
    y += LINE_H
    delay += delay_step
    for extra in stack_lines[1:]:
        lines.append(row("", extra, y, delay))
        y += LINE_H
        delay += delay_step

    lines.append(row("Highlights", HIGHLIGHTS[0] if HIGHLIGHTS else "", y, delay))
    y += LINE_H
    delay += delay_step
    for extra in HIGHLIGHTS[1:]:
        lines.append(row("", extra, y, delay))
        y += LINE_H
        delay += delay_step

    height = y + 18

    style_block = "" if STATIC else """
    <style>
      .line { opacity: 0; transform: translateX(-8px); animation: fadeSlide 0.5s ease-out forwards; }
      @keyframes fadeSlide {
        0%   { opacity: 0; transform: translateX(-8px); }
        100% { opacity: 1; transform: translateX(0); }
      }
    </style>
    """

    header = (
        f'<rect x="0" y="0" width="{WIDTH}" height="26" rx="6" ry="6" fill="#161b22" />'
        f'<circle cx="14" cy="13" r="4" fill="#ff5f56" />'
        f'<circle cx="28" cy="13" r="4" fill="#ffbd2e" />'
        f'<circle cx="42" cy="13" r="4" fill="#27c93f" />'
        f'<text x="{WIDTH/2}" y="17" fill="{DIM}" font-size="11" text-anchor="middle">'
        f'{esc(TITLE_USER)}: {esc(TITLE_PATH)}$ neofetch</text>'
    )

    svg = (
        f'<svg viewBox="0 0 {WIDTH} {height}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="Consolas, Menlo, monospace" font-size="13">'
        f'{style_block}'
        f'{header}'
        + "".join(lines) +
        '</svg>'
    )
    return svg


def main():
    svg = build()
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
