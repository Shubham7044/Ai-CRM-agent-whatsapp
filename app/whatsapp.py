from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()  # 🔥 THIS WAS MISSING

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

print("SID:", account_sid)  # debug
print("TOKEN:", auth_token)

client = Client(account_sid, auth_token)


def send_whatsapp_message(to, message):
    client.messages.create(
        from_='whatsapp:+14155238886',
        body=message,
        to=to
    )