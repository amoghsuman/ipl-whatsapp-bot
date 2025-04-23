import json
from datetime import datetime
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "ipl_schedule_2025_clean.json")

def get_today_matches():
    today = datetime.today().strftime("%Y-%m-%d")

    with open(DATA_PATH, "r") as f:
        schedule = json.load(f)

    today_matches = [match for match in schedule if match["date"] == today]

    if not today_matches:
        return "No IPL matches scheduled today."

    response = "🏏 Today's IPL Matches:\n\n"
    for match in today_matches:
        response += f"{match['teams']} at {match['venue']} — {match['time']}\n"
    return response.strip()
