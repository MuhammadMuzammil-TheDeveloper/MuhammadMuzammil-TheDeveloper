"""
Wide terminal-style panel meant to sit BELOW the portrait+details row,
listing the full tech stack and achievements/highlights.
"""
import os

STATIC = os.environ.get("STATIC") == "1"
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "skills-achievements.svg")

# ---- Edit this block to update the card's content ----
TITLE_USER = "muzammil@github"
TITLE_PATH = "~"
STACK_GROUPS = [
    ("Languages & Frameworks", [
        "JavaScript (ES6+)", "Node.js", "Express.js", "MongoDB",
        "Python", "C++", "HTML5", "CSS3", "React.js",
    ]),
    ("Styling & Backend Services", [
        "Tailwind CSS", "Bootstrap", "REST APIs", "Firebase", "Supabase", "MySQL",
    ]),
    ("Tools & Platforms", [
        "Git", "GitHub", "Postman", "VS Code", "Netlify", "Vercel", "XAMPP",
    ]),
    ("CMS & Design", [
        "WordPress", "Elementor", "Responsive Design", "UI/UX Basics",
    ]),
]
ACHIEVEMENTS = [
    "1st place - CODE JUNG 2025 (Web Development)",
    "Top 5 - SMIT Hackathon 2025",
    "Cisco Networking Basics certification",
]
# --------------------------------------------------------

ACCENT = "#39d353"
FG = "#c9d1d9"
DIM = "#8b949e"
CHIP_BG = "#161b22"
CHIP_BORDER = "#30363d"

WIDTH = 860
LEFT_PAD = 20
TOP_PAD = 46
LINE_H = 24
CHIP_H = 24
CHIP_GAP = 8
CHIP_PAD_X = 10


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text_width(s, size=12.3):
    # Rough monospace width estimate (Consolas ~0.6em per char)
    return len(s) * size * 0.6


def build_chips(items, y0, delay_start, delay_step):
    parts = []
    x = LEFT_PAD
    y = y0
    row_h = CHIP_H + CHIP_GAP
    delay = delay_start
    for item in items:
        w = text_width(item) + CHIP_PAD_X * 2
        if x + w > WIDTH - LEFT_PAD:
            x = LEFT_PAD
            y += row_h
        style = "" if STATIC else f' style="animation-delay:{delay}s"'
        cls = "" if STATIC else ' class="chip"'
        parts.append(
            f'<g{cls}{style}>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{CHIP_H}" rx="6" ry="6" '
            f'fill="{CHIP_BG}" stroke="{CHIP_BORDER}" />'
            f'<text x="{x + CHIP_PAD_X}" y="{y + CHIP_H - 7}" fill="{FG}" font-size="12.3">'
            f'{esc(item)}</text>'
            f'</g>'
        )
        x += w + CHIP_GAP
        delay += delay_step
    return "".join(parts), y + row_h


def build_list(items, y0, delay_start, delay_step):
    parts = []
    y = y0
    delay = delay_start
    for item in items:
        style = "" if STATIC else f' style="animation-delay:{delay}s"'
        cls = "" if STATIC else ' class="line"'
        parts.append(
            f'<g{cls}{style}>'
            f'<text x="{LEFT_PAD}" y="{y}" fill="{ACCENT}">&gt;</text>'
            f'<text x="{LEFT_PAD + 16}" y="{y}" fill="{FG}">{esc(item)}</text>'
            f'</g>'
        )
        y += LINE_H
        delay += delay_step
    return "".join(parts), y


def build():
    y = TOP_PAD
    parts = []

    parts.append(
        f'<text x="{LEFT_PAD}" y="{y}" fill="{ACCENT}" font-weight="600">Tech Stack</text>'
    )
    y += 22

    delay = 0.0
    for group_name, items in STACK_GROUPS:
        parts.append(
            f'<text x="{LEFT_PAD}" y="{y}" fill="{DIM}" font-size="11.5">{esc(group_name)}</text>'
        )
        y += 14
        chips_svg, y = build_chips(items, y, delay, 0.05)
        parts.append(chips_svg)
        y += 8
        delay += 0.2

    y += 6
    parts.append(
        f'<text x="{LEFT_PAD}" y="{y}" fill="{ACCENT}" font-weight="600">Achievements</text>'
    )
    y += 16
    list_svg, y = build_list(ACHIEVEMENTS, y, delay, 0.15)
    parts.append(list_svg)

    height = y + 10

    style_block = "" if STATIC else """
    <style>
      .chip { opacity: 0; transform: translateY(-4px); animation: popIn 0.35s ease-out forwards; }
      .line { opacity: 0; transform: translateX(-8px); animation: fadeSlide 0.4s ease-out forwards; }
      @keyframes popIn {
        0%   { opacity: 0; transform: translateY(-4px); }
        100% { opacity: 1; transform: translateY(0); }
      }
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
        f'{esc(TITLE_USER)}: {esc(TITLE_PATH)}$ cat skills.txt</text>'
    )

    svg = (
        f'<svg viewBox="0 0 {WIDTH} {height}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="Consolas, Menlo, monospace" font-size="13">'
        f'{style_block}{header}' + "".join(parts) + '</svg>'
    )
    return svg


def main():
    with open(OUT_PATH, "w") as f:
        f.write(build())
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
