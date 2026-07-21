"""
Neofetch-style card sitting beside the ASCII portrait: name, current +
previous roles, education, location, and contact links. Tech stack and
achievements live in their own wider panel below (see make_skills_card.py).
"""
import os

STATIC = os.environ.get("STATIC") == "1"
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "details-card.svg")

# ---- Edit this block to update the card's content ----
TITLE_USER = "muzammil@github"
TITLE_PATH = "~"

FIELDS = [
    ("Name", "Muhammad Muzammil"),
    ("Now", "Full Stack Dev Intern @ NexSoft Solutions"),
    ("Prev", "WordPress Blog Dev @ Webera Solution"),
    ("Edu", "BSCS, KIET Karachi - grad 2027"),
    ("Location", "Karachi, Pakistan"),
    ("GitHub", "MuhammadMuzammil-TheDeveloper"),
    ("LinkedIn", "muhammad-muzammil-7562bb316"),
]
# --------------------------------------------------------

ACCENT = "#39d353"
FG = "#c9d1d9"
DIM = "#8b949e"

WIDTH = 370
LINE_H = 20
TOP_PAD = 44
LEFT_PAD = 18
LABEL_COL_W = 70
VALUE_FONT_SIZE = 11.5
MAX_VALUE_CHARS = 30  # wrap point for the value column at VALUE_FONT_SIZE


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def wrap_value(value, max_chars):
    words = value.split(" ")
    lines, cur = [], ""
    for w in words:
        candidate = (cur + " " + w) if cur else w
        if len(candidate) > max_chars and cur:
            lines.append(cur)
            cur = w
        else:
            cur = candidate
    if cur:
        lines.append(cur)
    return lines


def row(label, value, y, delay):
    """Returns (svg_fragment, new_y) — value may wrap onto extra lines."""
    style = "" if STATIC else f' style="animation-delay:{delay}s"'
    cls = "" if STATIC else ' class="line"'
    value_lines = wrap_value(value, MAX_VALUE_CHARS)

    parts = [f'<g{cls}{style}>']
    parts.append(f'<text x="{LEFT_PAD}" y="{y}" fill="{ACCENT}" font-weight="600">{esc(label)}</text>')
    for i, vline in enumerate(value_lines):
        parts.append(
            f'<text x="{LEFT_PAD + LABEL_COL_W}" y="{y + i * (LINE_H - 4)}" '
            f'fill="{FG}" font-size="{VALUE_FONT_SIZE}">{esc(vline)}</text>'
        )
    parts.append('</g>')
    new_y = y + max(1, len(value_lines)) * (LINE_H - 4) + 6
    return "".join(parts), new_y


def build():
    y = TOP_PAD
    delay_step = 0.14
    lines = []
    for i, (label, value) in enumerate(FIELDS):
        frag, y = row(label, value, y, round(i * delay_step, 3))
        lines.append(frag)
    height = y + 12

    style_block = "" if STATIC else """
    <style>
      .line { opacity: 0; transform: translateX(-8px); animation: fadeSlide 0.45s ease-out forwards; }
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
