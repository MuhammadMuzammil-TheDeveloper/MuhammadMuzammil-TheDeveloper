"""
Fetch a public GitHub contribution calendar without any token.

GitHub serves the calendar fragment your profile page itself uses at:
    https://github.com/users/<username>/contributions

We parse the day cells with BeautifulSoup and write data/contributions.json
containing the raw days plus a few derived stats (current streak, longest
streak, best day, total).
"""
import json
import os
import sys
from datetime import date, datetime, timezone

import requests
from bs4 import BeautifulSoup

USERNAME = os.environ.get("GH_USERNAME", "MuhammadMuzammil-TheDeveloper")
URL = f"https://github.com/users/{USERNAME}/contributions"
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "contributions.json")


def fetch_days():
    headers = {"User-Agent": "Mozilla/5.0 (profile-readme-script)"}
    resp = requests.get(URL, headers=headers, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    days = []
    # Each day is a <td class="ContributionCalendar-day" data-date=... data-level=...>.
    # The actual count isn't an attribute — it's in a sibling <tool-tip for="...">
    # element reading e.g. "5 contributions on January 3rd." or
    # "No contributions on July 20th."
    cells = soup.select("td.ContributionCalendar-day")
    for cell in cells:
        d = cell.get("data-date")
        if not d:
            continue
        try:
            level = int(cell.get("data-level", 0))
        except (TypeError, ValueError):
            level = 0

        count = 0
        cell_id = cell.get("id")
        tip = soup.find("tool-tip", attrs={"for": cell_id}) if cell_id else None
        if tip and tip.text:
            text = tip.text.strip()
            if text.lower().startswith("no contributions"):
                count = 0
            else:
                first_token = text.split(" ", 1)[0]
                try:
                    count = int(first_token)
                except ValueError:
                    count = 0

        days.append({"date": d, "count": count, "level": level})

    days.sort(key=lambda x: x["date"])
    return days


def derive_stats(days):
    if not days:
        return {}

    total = sum(d["count"] for d in days)
    best = max(days, key=lambda d: d["count"]) if days else None

    # Current streak: walk backward from the most recent day.
    current_streak = 0
    for d in reversed(days):
        if d["count"] > 0:
            current_streak += 1
        else:
            break

    # Longest streak across the whole window.
    longest_streak = 0
    running = 0
    for d in days:
        if d["count"] > 0:
            running += 1
            longest_streak = max(longest_streak, running)
        else:
            running = 0

    # Rough monthly totals for the trailing 12 months.
    monthly = {}
    for d in days:
        month_key = d["date"][:7]  # YYYY-MM
        monthly[month_key] = monthly.get(month_key, 0) + d["count"]

    return {
        "total": total,
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "best_day": {"date": best["date"], "count": best["count"]} if best else None,
        "monthly": monthly,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def main():
    days = fetch_days()
    if not days:
        print("Warning: no contribution cells parsed — GitHub's markup may have "
              "changed, or the profile has no public contribution data.", file=sys.stderr)
    stats = derive_stats(days)
    payload = {"username": USERNAME, "days": days, "stats": stats}

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(payload, f, indent=2)
    print(f"Wrote {len(days)} days -> {OUT_PATH}")
    print(f"Stats: {stats}")


if __name__ == "__main__":
    main()
