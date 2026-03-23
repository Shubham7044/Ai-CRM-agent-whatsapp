from app.tools import create_lead, update_status, schedule_followup_seconds
from app.memory import get_history, save_message


def extract_name(text):
    words = text.split()
    for i, word in enumerate(words):
        if word.lower() == "with":
            return words[i + 1].capitalize()
    return None


def run_agent(user_input: str, user_id: str):
    try:
        text = user_input.lower()

        # 🧠 MEMORY
        if "my name is" in text:
            name = user_input.split("is")[-1].strip().capitalize()
            save_message(user_id, "name", name)
            return f"Nice to meet you, {name}!"

        if "what is my name" in text:
            history = get_history(user_id)
            for msg in reversed(history):
                if msg.get("role") == "name":
                    return f"Your name is {msg.get('content')}"
            return "I don't know your name yet."

        # 🤖 CREATE LEAD
        if "create" in text:
            name = user_input.split("for")[1].split()[0]
            interest = user_input.split()[-1]
            return create_lead(name, interest)

        # 🤖 UPDATE STATUS
        if "update" in text:
            name = user_input.split()[1]
            status = user_input.split()[-1]
            return update_status(name, status)

        # ⏰ REMINDER (SECONDS)
        if "seconds" in text:
            seconds = [w for w in text.split() if w.isdigit()][0]
            name = extract_name(user_input)
            return schedule_followup_seconds(name, seconds)

        return "I can help with CRM + reminders."

    except Exception as e:
        print("AGENT ERROR:", e)
        return "Something went wrong"