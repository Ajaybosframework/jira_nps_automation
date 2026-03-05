import json
from datetime import date

def get_sprints():

    with open("data/fake_jira_data.json") as f:
        data = json.load(f)

    return data


def get_sprints_ending_today():

    today = str(date.today())

    sprints = get_sprints()

    result = []

    for sprint in sprints:

        if sprint["end_date"] == today:
            result.append(sprint)

    return result