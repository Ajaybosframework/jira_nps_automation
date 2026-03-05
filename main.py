import json
import os

from services.jira_service import get_sprints_ending_today
from services.summary_service import generate_summary
from services.email_service import send_email


TRACK_FILE = "sent_sprints.json"


def load_sent_sprints():

    if not os.path.exists(TRACK_FILE):
        return {}

    try:
        with open(TRACK_FILE, "r") as f:
            data = json.load(f)

        if isinstance(data, dict):
            return data

        return {}

    except json.JSONDecodeError:
        print("⚠️ Could not read sent_sprints.json. Starting fresh.")
        return {}


def save_sent_sprints(data):

    with open(TRACK_FILE, "w") as f:
        json.dump(data, f, indent=2)


def run():

    print("🔍 Checking for sprint completion...")

    sent_sprints = load_sent_sprints()

    sprints = get_sprints_ending_today()

    print("📊 Sprints found:", sprints)

    if not sprints:
        print("ℹ️ No sprint ended today")
        return

    for sprint in sprints:

        sprint_id = str(sprint.get("sprint_id") or sprint.get("sprint_name"))

        if not sprint_id:
            print("⚠️ Skipping sprint due to missing ID:", sprint)
            continue

        sprint_name = sprint.get("sprint_name", "Unknown Sprint")

        if sprint_id in sent_sprints:
            print(f"⏭ Email already sent for sprint: {sprint_name}")
            continue

        print(f"🏁 Sprint ended: {sprint_name}")

        try:
            summary = generate_summary(sprint)

            send_email(summary)

            print("✅ Email sent successfully")

            sent_sprints[sprint_id] = True

        except Exception as e:
            print(f"❌ Failed to send email for {sprint_name}: {e}")

    save_sent_sprints(sent_sprints)

    print("💾 Sprint tracking file updated")


if __name__ == "__main__":
    run()