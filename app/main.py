from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from app.scheduler import get_today_matches

app = FastAPI()

from app.scheduler import get_today_matches, get_next_match_for_team, get_matches_by_date, get_matches_by_city

TEAM_ALIASES = {
    "csk": "Chennai Super Kings",
    "rcb": "Royal Challengers Bengaluru",
    "mi": "Mumbai Indians",
    "kkr": "Kolkata Knight Riders",
    "rr": "Rajasthan Royals",
    "dc": "Delhi Capitals",
    "gt": "Gujarat Titans",
    "pbks": "Punjab Kings",
    "lsg": "Lucknow Super Giants",
    "srh": "Sunrisers Hyderabad"
}

@app.post("/bot")
async def whatsapp_webhook(request: Request):
    form_data = await request.form()
    message_body = form_data.get("Body", "").lower()
    print(f"📩 Received: {message_body}")

    try:
        if "today" in message_body:
            response = get_today_matches()

        elif "next" in message_body and "match" in message_body:
            for short, full in TEAM_ALIASES.items():
                if short in message_body:
                    response = get_next_match_for_team(full)
                    break
            else:
                response = "❓ Please specify a team (e.g., next CSK match)."

        elif "on" in message_body:
            import re
            match = re.search(r"\d{4}-\d{2}-\d{2}", message_body)
            if match:
                response = get_matches_by_date(match.group())
            else:
                response = "⚠️ Please provide a date in YYYY-MM-DD format."

        elif "in" in message_body or "at" in message_body:
            for keyword in ["in", "at"]:
                if keyword in message_body:
                    city = message_body.split(keyword)[-1].strip()
                    response = get_matches_by_city(city)
                    break

        else:
            response = (
                "👋 Try:\n"
                "• What's the IPL schedule today?\n"
                "• Next CSK match?\n"
                "• Match on 2025-04-10\n"
                "• Matches in Chennai"
            )

    except Exception as e:
        response = f"⚠️ Internal Error: {str(e)}"

    return PlainTextResponse(response)
