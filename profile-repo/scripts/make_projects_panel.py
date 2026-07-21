"""
Featured projects panel, styled like `ls -la ~/projects` with a one-line
description under each entry. SVGs embedded via <img> can't carry real
links (GitHub strips interactivity from <img>-rendered SVG), so the
README places the actual clickable links in plain markdown just below
this panel -- this is the visual index, the markdown links are the
functional one.
"""
import os

STATIC = os.environ.get("STATIC") == "1"
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "projects.svg")

TITLE_USER = "muzammil@github"
TITLE_PATH = "~/projects"

# ---- Edit this block to update the project list ----
PROJECTS = [
    ("NoteStack", "Supabase-powered sticky notes SaaS - glassmorphism auth, pastel dashboard"),
    ("Asset Maintenance System", "QR-based asset tracking - Admin/Technician/Public roles on Supabase"),
    ("AI Quiz Platform", "JS quiz app wired to the Open Trivia DB API"),
    ("WorldAtlas", "Country/geo data explorer built with vanilla JS"),
    ("Hospital Management System", "Patient, staff, and records management system"),
    ("SMIT UI Clone", "Pixel-level clone of the SMIT website UI"),
]
# ------------------------------------------------------

ACCENT = "#39d353"
FG = "#c9d1d9"
DIM = "#8b949e"

WIDTH = 860
LEFT_PAD = 20
TOP_PAD = 46
ROW_H = 40


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build():
    y = TOP_PAD
    parts = []
    delay = 0.0
    for name, desc in PROJECTS:
        style = "" if STATIC else f' style="animation-delay:{delay}s"'
        cls = "" if STATIC else ' class="line"'
        parts.append(
            f'<g{cls}{style}>'
            f'<text x="{LEFT_PAD}" y="{y}" fill="{ACCENT}">drwxr-xr-x</text>'
            f'<text x="{LEFT_PAD + 105}" y="{y}" fill="{FG}" font-weight="600">{esc(name)}</text>'
            f'<text x="{LEFT_PAD + 16}" y="{y + 18}" fill="{DIM}" font-size="12">{esc(desc)}</text>'
            f'</g>'
        )
        y += ROW_H
        delay += 0.12

    height = y + 6

    style_block = "" if STATIC else """
    <style>
      .line { opacity: 0; transform: translateX(-6px); animation: fadeSlide 0.4s ease-out forwards; }
      @keyframes fadeSlide {
        0%   { opacity: 0; transform: translateX(-6px); }
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
        f'{esc(TITLE_USER)}: {esc(TITLE_PATH)}$ ls -la</text>'
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
