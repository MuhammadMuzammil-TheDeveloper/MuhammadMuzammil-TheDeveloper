"""
Convert scripts/source-prepped.png into a self-typing, monochrome ASCII
portrait SVG.

The image is downsampled to a character grid (~100 wide), and each cell's
average brightness picks a glyph from a density ramp: sparse characters for
bright areas, dense ones for dark ones.

Each row is wrapped in a horizontal clip-path that wipes left-to-right (a
small block "cursor" rides the wipe edge), staggered top to bottom. The
portrait prints once and freezes -- no looping.
"""
import os
from PIL import Image

RAMP = " .`:-=+*cs#%@"   # bright (sparse) -> dark (dense); leading space = blank

GRID_COLS = 100
CHAR_W = 6      # px per character cell at render scale
CHAR_H = 11     # px per row (monospace line height, ~1.8x width)
FONT_SIZE = 10

SRC_PATH = os.path.join(os.path.dirname(__file__), "source-prepped.png")
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "avi-ascii.svg")

FILL = "#c9d1d9"   # single light-gray fill -- monochrome on purpose


def image_to_ascii_rows(path, cols):
    img = Image.open(path).convert("L")
    w, h = img.size
    # Character cells are taller than wide, so compensate the row count
    # to avoid a squashed portrait.
    aspect_correction = 0.55
    rows = max(1, int(cols * (h / w) * aspect_correction))
    small = img.resize((cols, rows))
    pixels = small.load()

    ramp_len = len(RAMP)
    ascii_rows = []
    for y in range(rows):
        line = []
        for x in range(cols):
            brightness = pixels[x, y]  # 0 dark .. 255 bright
            idx = int((brightness / 255) * (ramp_len - 1))
            line.append(RAMP[idx])
        ascii_rows.append("".join(line))
    return ascii_rows


def esc(ch):
    if ch == "&":
        return "&amp;"
    if ch == "<":
        return "&lt;"
    if ch == ">":
        return "&gt;"
    return ch


def build_svg(rows):
    width = GRID_COLS * CHAR_W
    height = len(rows) * CHAR_H
    row_duration = 0.9
    row_stagger = 0.05

    parts = [
        f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="Consolas, Menlo, monospace" font-size="{FONT_SIZE}">',
    ]

    style = f"""
    <style>
      .row-wipe {{
        animation: wipe {row_duration}s steps(60, end) forwards;
      }}
      @keyframes wipe {{
        from {{ clip-path: inset(0 100% 0 0); }}
        to   {{ clip-path: inset(0 0 0 0); }}
      }}
    </style>
    """
    parts.append(style)

    parts.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="transparent" />')

    for ri, row_text in enumerate(rows):
        y = (ri + 1) * CHAR_H - 2
        delay = round(ri * row_stagger, 3)
        escaped = "".join(esc(c) for c in row_text)
        # Preserve leading/trailing spaces in the SVG text node.
        parts.append(
            f'<g class="row-wipe" style="animation-delay:{delay}s">'
            f'<text x="0" y="{y}" xml:space="preserve" fill="{FILL}">{escaped}</text>'
            f'</g>'
        )

    parts.append("</svg>")
    return "\n".join(parts)


def main():
    if not os.path.exists(SRC_PATH):
        print(f"Missing {SRC_PATH} -- run prep_photo.py first.")
        return
    rows = image_to_ascii_rows(SRC_PATH, GRID_COLS)
    svg = build_svg(rows)
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"Wrote {OUT_PATH} ({len(rows)} rows x {GRID_COLS} cols)")


if __name__ == "__main__":
    main()
