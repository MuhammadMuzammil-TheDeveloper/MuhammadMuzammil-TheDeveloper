"""
Render data/contributions.json as a 53-week x 7-day GitHub-style heatmap SVG.

The grid reveals itself once with a diagonal, line-after-line slide-down
(pure CSS keyframes embedded in the SVG's <style>, no external CSS, no JS),
then freezes. A Less -> More legend and a stats line sit below the grid.
"""
import json
import os
from datetime import datetime

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]
# index 0 = no contributions ... index 5 = a neon top end above GitHub's own level 4

BOX = 11          # box size in px
GAP = 3           # gap between boxes
COLS = 53         # weeks
ROWS = 7          # days
LEFT_PAD = 28     # room for day labels
TOP_PAD = 20       # room for month labels
LEGEND_H = 26
FOOTER_H = 22

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "contributions.json")
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "contrib-heatmap.svg")

MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def load_data():
    with open(DATA_PATH) as f:
        return json.load(f)


def bucket_level(count, max_count):
    """Map a raw count onto our 0-5 palette, independent of GitHub's own level."""
    if count <= 0 or max_count <= 0:
        return 0
    ratio = count / max_count
    if ratio <= 0.15:
        return 1
    if ratio <= 0.35:
        return 2
    if ratio <= 0.6:
        return 3
    if ratio <= 0.85:
        return 4
    return 5


def build_weeks(days):
    """Group flat day list into weeks (columns), aligned to Sunday-start rows."""
    if not days:
        return []
    parsed = [
        {**d, "dt": datetime.strptime(d["date"], "%Y-%m-%d")}
        for d in days
    ]
    parsed.sort(key=lambda d: d["dt"])

    weeks = []
    current_week = [None] * 7
    week_start_dow = parsed[0]["dt"].weekday()  # Mon=0 .. Sun=6
    # Convert to Sun=0..Sat=6 indexing to match GitHub's calendar
    first_dow = (week_start_dow + 1) % 7
    for i in range(first_dow):
        current_week[i] = None

    for d in parsed:
        dow = (d["dt"].weekday() + 1) % 7  # Sun=0
        if dow == 0 and any(x is not None for x in current_week):
            weeks.append(current_week)
            current_week = [None] * 7
        current_week[dow] = d

    if any(x is not None for x in current_week):
        weeks.append(current_week)

    return weeks


def month_labels(weeks):
    """Return {week_index: 'Jan'} for the first week each month appears in."""
    labels = {}
    seen_months = set()
    for wi, week in enumerate(weeks):
        for day in week:
            if day is None:
                continue
            key = day["dt"].strftime("%Y-%m")
            if key not in seen_months:
                seen_months.add(key)
                labels[wi] = MONTH_NAMES[day["dt"].month - 1]
            break
    return labels


def render(payload):
    days = payload.get("days", [])
    stats = payload.get("stats", {})
    username = payload.get("username", "")

    weeks = build_weeks(days)
    max_count = max((d["count"] for d in days if d), default=0) or 1
    labels = month_labels(weeks)

    grid_w = len(weeks) * (BOX + GAP)
    grid_h = ROWS * (BOX + GAP)
    width = LEFT_PAD + grid_w + 20
    height = TOP_PAD + grid_h + LEGEND_H + FOOTER_H + 10

    svg_parts = []
    svg_parts.append(
        f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="Consolas, Menlo, monospace">'
    )

    svg_parts.append(f"""
    <style>
      .cell {{
        opacity: 0;
        animation: revealCell 0.4s ease-out forwards;
      }}
      @keyframes revealCell {{
        0%   {{ opacity: 0; transform: translateY(-6px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
      }}
      .meta {{ fill: #8b949e; font-size: 9px; }}
      .footer {{ fill: #c9d1d9; font-size: 11px; }}
    </style>
    """)

    # Month labels
    for wi, name in labels.items():
        x = LEFT_PAD + wi * (BOX + GAP)
        svg_parts.append(f'<text x="{x}" y="{TOP_PAD - 8}" class="meta">{name}</text>')

    # Day-of-week labels (Mon, Wed, Fri only, like GitHub)
    dow_label_rows = {1: "Mon", 3: "Wed", 5: "Fri"}
    for row, name in dow_label_rows.items():
        y = TOP_PAD + row * (BOX + GAP) + BOX - 2
        svg_parts.append(f'<text x="0" y="{y}" class="meta">{name}</text>')

    # Grid cells, staggered diagonally: delay depends on (week + day) index
    max_delay_steps = len(weeks) + ROWS
    for wi, week in enumerate(weeks):
        for di, day in enumerate(week):
            x = LEFT_PAD + wi * (BOX + GAP)
            y = TOP_PAD + di * (BOX + GAP)
            if day is None:
                color = PALETTE[0]
                delay_steps = wi + di
            else:
                level = bucket_level(day["count"], max_count)
                color = PALETTE[level]
                delay_steps = wi + di
            delay = round(0.012 * delay_steps, 3)
            title = ""
            if day is not None:
                title = f'<title>{day["count"]} contributions on {day["date"]}</title>'
            svg_parts.append(
                f'<rect class="cell" x="{x}" y="{y}" width="{BOX}" height="{BOX}" '
                f'rx="2" ry="2" fill="{color}" '
                f'style="animation-delay:{delay}s">{title}</rect>'
            )

    # Legend: Less -> More
    legend_y = TOP_PAD + grid_h + 16
    svg_parts.append(f'<text x="{LEFT_PAD}" y="{legend_y + 8}" class="meta">Less</text>')
    lx = LEFT_PAD + 32
    for i, color in enumerate(PALETTE):
        svg_parts.append(
            f'<rect x="{lx + i * (BOX + GAP)}" y="{legend_y}" width="{BOX}" height="{BOX}" '
            f'rx="2" ry="2" fill="{color}" />'
        )
    svg_parts.append(
        f'<text x="{lx + len(PALETTE) * (BOX + GAP) + 6}" y="{legend_y + 8}" class="meta">More</text>'
    )

    # Footer stats line
    total = stats.get("total", 0)
    streak = stats.get("longest_streak", 0)
    footer_y = legend_y + LEGEND_H
    svg_parts.append(
        f'<text x="{LEFT_PAD}" y="{footer_y}" class="footer">'
        f'{total} contributions in the last year &#183; longest streak {streak} days'
        f'</text>'
    )

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def main():
    payload = load_data()
    svg = render(payload)
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
