from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.db import cursor, conn
from app.whatsapp import send_whatsapp_message

scheduler = BackgroundScheduler()

def check_followups():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "SELECT name FROM leads WHERE follow_up_date IS NOT NULL AND follow_up_date <= ?",
        (now,)
    )
    leads = cursor.fetchall()

    for lead in leads:
        name = lead[0]

        send_whatsapp_message(
            "whatsapp:+918670288623",  # replace with your number
            f"⏰ Reminder: Meeting with {name} now!"
        )

        cursor.execute(
            "UPDATE leads SET follow_up_date=NULL WHERE name=?",
            (name,)
        )
        conn.commit()


scheduler.add_job(check_followups, "interval", seconds=5)
scheduler.start()