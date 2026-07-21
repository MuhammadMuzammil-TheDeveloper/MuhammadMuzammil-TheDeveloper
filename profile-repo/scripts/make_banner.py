"""
Full-width typing-effect banner for the top of the profile README:
a terminal prompt that types out a greeting line, then a subtitle line,
then settles into a slow blinking cursor (the only looping element on
the whole profile -- everything else prints once and freezes).
"""
import os

STATIC = os.environ.get("STATIC") == "1"
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "banner.svg")

PROMPT = "muzammil@github ~ $"
LINE1 = "echo \"Hi, I'm Muzammil\""
LINE2_LABEL = "> "
LINE2 = "Full Stack Developer, building things that work end to end."

WIDTH = 860
HEIGHT = 118
FG = "#c9d1d9"
ACCENT = "#39d353"
DIM = "#8b949e"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def typed_text(text, x, y, start_delay, char_dur, fill, font_size=15, font_weight="400"):
    """Render text as a run of tspans, each appearing at a staggered delay
    via a fade-in (kept short so it reads as 'typing' rather than fading)."""
    parts = [f'<text x="{x}" y="{y}" font-size="{font_size}" font-weight="{font_weight}" fill="{fill}">']
    for i, ch in enumerate(text):
        delay = round(start_delay + i * char_dur, 3)
        cls = "" if STATIC else ' class="ch"'
        style = "" if STATIC else f' style="animation-delay:{delay}s"'
        parts.append(f'<tspan{cls}{style}>{esc(ch)}</tspan>')
    parts.append("</text>")
    return "".join(parts), start_delay + len(text) * char_dur


def build():
    header = (
        f'<rect x="0" y="0" width="{WIDTH}" height="26" rx="6" ry="6" fill="#161b22" />'
        f'<circle cx="14" cy="13" r="4" fill="#ff5f56" />'
        f'<circle cx="28" cy="13" r="4" fill="#ffbd2e" />'
        f'<circle cx="42" cy="13" r="4" fill="#27c93f" />'
    )

    prompt1 = f'<text x="20" y="54" font-size="15" fill="{ACCENT}" font-weight="600">{esc(PROMPT)}</text>'
    prompt_w = len(PROMPT) * 15 * 0.6 + 32

    line1_svg, end_delay = typed_text(LINE1, 20 + prompt_w, 54, 0.1, 0.035, FG, font_weight="600")

    line2_svg, end_delay2 = typed_text(
        LINE2_LABEL + LINE2, 20, 86, end_delay + 0.25, 0.018, DIM
    )

    cursor_x = 20 + (len(LINE2_LABEL + LINE2)) * 15 * 0.6 + 6
    cursor = "" if STATIC else (
        f'<rect class="cursor" x="{cursor_x}" y="74" width="9" height="16" fill="{ACCENT}" '
        f'style="animation-delay:{round(end_delay2 + 0.2, 3)}s" />'
    )

    style_block = "" if STATIC else f"""
    <style>
      .ch {{ opacity: 0; animation: appear 0.01s linear forwards; }}
      @keyframes appear {{
        to {{ opacity: 1; }}
      }}
      .cursor {{
        opacity: 0;
        animation: cursorIn 0.01s linear forwards, blink 1s step-end infinite;
      }}
      @keyframes cursorIn {{ to {{ opacity: 1; }} }}
      @keyframes blink {{ 50% {{ opacity: 0; }} }}
    </style>
    """

    svg = (
        f'<svg viewBox="0 0 {WIDTH} {HEIGHT}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="Consolas, Menlo, monospace">'
        f'{style_block}{header}{prompt1}{line1_svg}{line2_svg}{cursor}'
        f'</svg>'
    )
    return svg


def main():
    with open(OUT_PATH, "w") as f:
        f.write(build())
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
