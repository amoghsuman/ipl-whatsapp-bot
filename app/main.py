from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from app.scheduler import get_today_matches

app = FastAPI()

@app.post("/bot")
async def whatsapp_webhook(request: Request):
    form_data = await request.form()
    message_body = form_data.get("Body", "").lower()
    print(f"📩 Incoming WhatsApp message: {message_body}")

    try:
        if "today" in message_body or "match" in message_body or "ipl" in message_body:
            response_text = get_today_matches()
        else:
            response_text = "👋 Hi! You can ask:\n• What's the IPL schedule today?\n• Today's matches?\n• Any match today?"

    except Exception as e:
        response_text = f"⚠️ Error processing request: {str(e)}"

    return PlainTextResponse(response_text)
