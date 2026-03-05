import requests
import config


def send_slack_message(message):

    payload = {
        "text": message
    }

    requests.post(config.SLACK_WEBHOOK, json=payload)