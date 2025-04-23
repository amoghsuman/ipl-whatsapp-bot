import json
from datetime import datetime

def get_next_match_for_team(team_name: str):
    with open("app/data/ipl_schedule.json", "r") as f:
        schedule = json.load(f)

    today = datetime.today().strftime("%Y-%m-%d")

    # Filter for matches after today that include the team name
    upcoming = [
        match for match in schedule
        if match["date"] >= today and team_name.lower() in match["teams"].lower()
    ]

    if not upcoming:
        return f"❌ No upcoming matches found for *{team_name}*."

    next_match = upcoming[0]
    return (
        f"🟢 *Next match for {team_name.title()}:*\n\n"
        f"{next_match['teams']} on {next_match['day']}, {next_match['date']} at {next_match['venue']} — {next_match['time']}"
    )

def get_today_matches():
    with open("app/data/ipl_schedule.json", "r") as f:
        schedule = json.load(f)

    today = datetime.today().strftime("%Y-%m-%d")
    today_matches = [match for match in schedule if match["date"] == today]

    if not today_matches:
        return "🟡 No IPL matches are scheduled today."

    response = "🏏 *Today's IPL Matches:*\n\n"
    for match in today_matches:
        response += f"🔸 {match['teams']} at {match['venue']} — {match['time']}\n"
    return response.strip()
