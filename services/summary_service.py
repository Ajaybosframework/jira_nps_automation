def generate_summary(sprint):

    summary = f"""
Sprint Name: {sprint['sprint_name']}
Project: {sprint['project_name']}

Sprint Results:

Completed Issues: {sprint['completed_issues']}
Bugs Fixed: {sprint['bugs_fixed']}
Story Points Delivered: {sprint['story_points']}

Sprint Duration:
{sprint['start_date']} → {sprint['end_date']}
"""

    return summary