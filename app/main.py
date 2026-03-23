from fastapi import FastAPI, Request
from fastapi.responses import Response
from twilio.twiml.messaging_response import MessagingResponse

from app.agent import run_agent
from app.scheduler import scheduler  # start scheduler

app = FastAPI()


@app.post("/whatsapp")
async def whatsapp(request: Request):
    form = await request.form()

    user_msg = form.get("Body", "")
    user_id = form.get("From", "")

    reply = run_agent(user_msg, user_id)

    resp = MessagingResponse()
    resp.message(reply)

    return Response(content=str(resp), media_type="text/xml")