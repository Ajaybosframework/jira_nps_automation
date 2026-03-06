import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
from config import JIRA_EMAIL, JIRA_API_TOKEN, JIRA_BASE_URL


auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

headers = {
    "Accept": "application/json"
}


def get_sprints_ending_today():

    results = []

    boards = requests.get(
        f"{JIRA_BASE_URL}/rest/agile/1.0/board",
        headers=headers,
        auth=auth
    ).json()["values"]

    for board in boards:

        board_id = board["id"]
        board_name = board["name"]

        sprints = requests.get(
            f"{JIRA_BASE_URL}/rest/agile/1.0/board/{board_id}/sprint",
            headers=headers,
            auth=auth
        ).json()["values"]

        for sprint in sprints:

            end_date = sprint.get("endDate")

            if not end_date:
                continue

            end = datetime.fromisoformat(end_date.replace("Z", "+00:00")).date()
            today = datetime.utcnow().date()

            if end != today:
                continue

            sprint_id = sprint["id"]
            sprint_name = sprint["name"]

            issues = requests.get(
                f"{JIRA_BASE_URL}/rest/agile/1.0/sprint/{sprint_id}/issue",
                headers=headers,
                auth=auth
            ).json()["issues"]

            total = len(issues)
            done = 0
            bugs = 0
            story_points = 0

            for issue in issues:

                status = issue["fields"]["status"]["name"].lower()
                issue_type = issue["fields"]["issuetype"]["name"].lower()

                sp = issue["fields"].get("customfield_10016")

                if sp:
                    story_points += sp

                if "done" in status:
                    done += 1

                if issue_type == "bug":
                    bugs += 1

            results.append({
                "project_name": board_name,
                "sprint_name": sprint_name,
                "sprint_id": sprint_id,
                "completed_issues": done,
                "bugs_fixed": bugs,
                "story_points": story_points
            })

    return results