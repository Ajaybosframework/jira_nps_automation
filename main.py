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
            else:
                return {}

    except:
        return {}


def save_sent_sprints(data):
    with open(TRACK_FILE, "w") as f:
        json.dump(data, f, indent=2)


def run():

    print("Checking for sprint completion...")

    sent_sprints = load_sent_sprints()

    sprints = get_sprints_ending_today()

    if not sprints:
        print("No sprint ended today")
        return

    for sprint in sprints:

        sprint_id = str(sprint["sprint_name"])

        if sprint_id in sent_sprints:
            print("Email already sent for:", sprint["sprint_name"])
            continue

        print("Sprint ended:", sprint["sprint_name"])

        summary = generate_summary(sprint)

        send_email(summary)

        print("Email sent successfully")

        # mark as sent
        sent_sprints[sprint_id] = True

    save_sent_sprints(sent_sprints)


if __name__ == "__main__":
    run()