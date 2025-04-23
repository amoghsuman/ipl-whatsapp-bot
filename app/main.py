from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from app.scheduler import get_today_matches

app = FastAPI()

@app.post("/bot")
async def whatsapp_webhook(request: Request):
    form_data = await request.form()
    message_body = form_data.get("Body", "").lower()

    if "today" in message_body:
        response_text = get_today_matches()
    else:
        response_text = "Hi! Ask me: What's the IPL schedule today?"

    return PlainTextResponse(response_text)

