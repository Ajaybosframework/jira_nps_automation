import smtplib
from email.mime.text import MIMEText
import config


def send_email(summary):

    subject = "Sprint Completed – Feedback Request"

    body = f"""
Hello,

The sprint has been successfully completed.

Sprint Summary
----------------

{summary}

We would appreciate your feedback on this sprint.

Please complete the NPS survey below:

{config.NPS_FORM_LINK}

Thank you for your collaboration.

Best Regards
Development Team
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = config.EMAIL_SENDER
    msg["To"] = config.CLIENT_EMAIL

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    server.login(config.EMAIL_SENDER, config.EMAIL_PASSWORD)

    server.send_message(msg)

    server.quit()