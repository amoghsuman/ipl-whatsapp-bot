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

def get_matches_by_date(date_str: str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        query_date = date_obj.strftime("%Y-%m-%d")
    except ValueError:
        return "⚠️ Please use the format YYYY-MM-DD (e.g., 2025-04-10)."

    with open("app/data/ipl_schedule.json", "r") as f:
        schedule = json.load(f)

    matches = [m for m in schedule if m["date"] == query_date]

    if not matches:
        return f"🟡 No matches scheduled on {query_date}."

    response = f"📅 *Matches on {query_date}:*\n\n"
    for m in matches:
        response += f"🔸 {m['teams']} at {m['venue']} — {m['time']}\n"
    return response.strip()

def get_matches_by_city(city_name: str):
    with open("app/data/ipl_schedule.json", "r") as f:
        schedule = json.load(f)

    city_matches = [
        m for m in schedule if city_name.lower() in m["venue"].lower()
    ]

    if not city_matches:
        return f"⚠️ No matches found in *{city_name.title()}*."

    response = f"🏟️ *Matches in {city_name.title()}:*\n\n"
    for m in city_matches:
        response += f"{m['teams']} on {m['day']}, {m['date']} — {m['time']}\n"
    return response.strip()

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
