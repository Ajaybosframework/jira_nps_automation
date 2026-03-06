import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
from config import JIRA_EMAIL, JIRA_API_TOKEN, JIRA_BASE_URL

auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

headers = {
    "Accept": "application/json"
}


def get_boards():

    url = f"{JIRA_BASE_URL}/rest/agile/1.0/board"

    response = requests.get(url, headers=headers, auth=auth)

    return response.json().get("values", [])


def get_sprints(board_id):

    url = f"{JIRA_BASE_URL}/rest/agile/1.0/board/{board_id}/sprint"

    response = requests.get(url, headers=headers, auth=auth)

    return response.json().get("values", [])


def get_issues(sprint_id):

    url = f"{JIRA_BASE_URL}/rest/agile/1.0/sprint/{sprint_id}/issue"

    response = requests.get(url, headers=headers, auth=auth)

    return response.json().get("issues", [])


def get_sprints_ending_today():

    results = []

    boards = get_boards()

    today = datetime.utcnow().date()

    for board in boards:

        board_id = board["id"]
        board_name = board["name"]

        sprints = get_sprints(board_id)

        for sprint in sprints:

            end_date = sprint.get("endDate")

            if not end_date:
                continue

            sprint_end = datetime.fromisoformat(end_date.replace("Z", "+00:00")).date()

            if sprint_end != today:
                continue

            sprint_id = sprint["id"]
            sprint_name = sprint["name"]

            issues = get_issues(sprint_id)

            total = len(issues)
            done = 0
            bugs = 0
            story_points = 0

            for issue in issues:

                fields = issue["fields"]

                status = fields["status"]["name"].lower()
                issue_type = fields["issuetype"]["name"].lower()

                sp = fields.get("customfield_10016")

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