from app.db import cursor, conn
from datetime import datetime, timedelta


def create_lead(name, interest):
    cursor.execute(
        "INSERT INTO leads (name, interest, status) VALUES (?, ?, ?)",
        (name, interest, "new")
    )
    conn.commit()
    return f"Lead created for {name}"


def update_status(name, status):
    cursor.execute(
        "UPDATE leads SET status=? WHERE name=?",
        (status, name)
    )
    conn.commit()
    return f"Updated {name} status to {status}"


def schedule_followup_seconds(name, seconds):
    seconds = int(seconds)
    follow_time = datetime.now() + timedelta(seconds=seconds)

    cursor.execute(
        "UPDATE leads SET follow_up_date=? WHERE name=?",
        (follow_time.strftime("%Y-%m-%d %H:%M:%S"), name)
    )
    conn.commit()

    return f"Reminder set for {name} in {seconds} seconds"