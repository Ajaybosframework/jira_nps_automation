from services.jira_service import get_sprints_ending_today
from services.summary_service import generate_summary
from services.email_service import send_email


def run():

    sprints = get_sprints_ending_today()

    for sprint in sprints:

        summary = generate_summary(sprint)

        send_email(summary)

        print("Email sent successfully")


if __name__ == "__main__":
    run()