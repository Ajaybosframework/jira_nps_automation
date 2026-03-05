import json
from datetime import datetime


def get_sprints_ending_today():

    with open("data/fake_jira_data.json") as file:
        sprints = json.load(file)

    today = datetime.today().strftime("%Y-%m-%d")

    ending_sprints = []

    for sprint in sprints:

        if sprint["end_date"] == today:
            ending_sprints.append(sprint)

    return ending_sprints