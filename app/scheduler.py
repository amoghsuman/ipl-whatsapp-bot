import json
from datetime import datetime

def get_today_matches():
    with open("app/data/ipl_schedule.json", "r") as f:
        schedule = json.load(f)

    today = datetime.today().strftime("%Y-%m-%d")
    today_matches = [match for match in schedule if match["date"] == today]

    if not today_matches:
        return "No IPL matches scheduled today."

    response = "🏏 Today's IPL Matches:\n\n"
    for match in today_matches:
        response += f"{match['teams']} at {match['venue']} — {match['time']}\n"
    return response.strip()

