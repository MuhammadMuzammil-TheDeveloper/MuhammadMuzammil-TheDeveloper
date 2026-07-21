"""
Small neofetch-style card: just the "Now" / "Prev" lines, meant to sit
beside the ASCII portrait. Tech stack and achievements live in their own
wider panel below (see make_skills_card.py) so this stays compact.
"""
import os

STATIC = os.environ.get("STATIC") == "1"
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "details-card.svg")

# ---- Edit this block to update the card's content ----
TITLE_USER = "muzammil@github"
TITLE_PATH = "~"
NOW_ROLE = "Full Stack Developer"
PREV = "BSCS student, KIET (Karachi) - grad 2027"
# --------------------------------------------------------

ACCENT = "#39d353"
FG = "#c9d1d9"
DIM = "#8b949e"

WIDTH = 370
LINE_H = 24
TOP_PAD = 44
LEFT_PAD = 18


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def row(label, value, y, delay):
    style = "" if STATIC else f' style="animation-delay:{delay}s"'
    cls = "" if STATIC else ' class="line"'
    return (
        f'<g{cls}{style}>'
        f'<text x="{LEFT_PAD}" y="{y}" fill="{ACCENT}" font-weight="600">{esc(label)}</text>'
        f'<text x="{LEFT_PAD + 60}" y="{y}" fill="{FG}">{esc(value)}</text>'
        f'</g>'
    )


def build():
    y = TOP_PAD
    delay_step = 0.18
    lines = []
    lines.append(row("Now", NOW_ROLE, y, 0.0)); y += LINE_H
    lines.append(row("Prev", PREV, y, delay_step)); y += LINE_H
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
        f'{esc(TITLE_USER)}: {esc(TITLE_PATH)}$ whoami</text>'
    )

    svg = (
        f'<svg viewBox="0 0 {WIDTH} {height}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="Consolas, Menlo, monospace" font-size="13">'
        f'{style_block}{header}' + "".join(lines) + '</svg>'
    )
    return svg


def main():
    with open(OUT_PATH, "w") as f:
        f.write(build())
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
