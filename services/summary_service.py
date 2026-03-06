def generate_summary(sprint):

    summary = f"""
Sprint Completed

Project: {sprint['project_name']}
Sprint: {sprint['sprint_name']}

Results

Completed Issues: {sprint['completed_issues']}
Bugs Fixed: {sprint['bugs_fixed']}
Story Points Delivered: {sprint['story_points']}
"""

    return summary