import os
import smtplib

from email.mime.text import MIMEText

sender = os.environ["SMTP_USER"]
password = os.environ["SMTP_PASSWORD"]

receiver = os.environ["MAIL_TO"]

artifact_url = os.environ["ARTIFACT_URL"]

body = f"""
Firmware Automation Completed

Please check:

Artifact Link:
{artifact_url}
"""

msg = MIMEText(body)

msg["Subject"] = "Firmware Automation Report"

msg["From"] = sender
msg["To"] = receiver

server = smtplib.SMTP("smtp.office365.com", 587)

server.starttls()

server.login(sender, password)

server.sendmail(
    sender,
    receiver,
    msg.as_string()
)

server.quit()
