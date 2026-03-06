import os
from dotenv import load_dotenv

load_dotenv()

# Jira Config
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")

# Email Config
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Slack Config
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")