from services.jira_service import get_sprints_ending_today
from services.summary_service import generate_summary
from services.email_service import send_email


def run():

    print("Checking for sprint completion...")

    sprints = get_sprints_ending_today()

    if not sprints:
        print("No sprint ended today")
        return

    for sprint in sprints:

        print("Sprint ended:", sprint["sprint_name"])

        summary = generate_summary(sprint)

        send_email(summary)

        print("Email sent successfully")


if __name__ == "__main__":
    run()