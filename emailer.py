# emailer.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import smtplib
from email.message import EmailMessage
from config import EMAIL_ADDRESS, EMAIL_PASSWORD

class Emailer:
    def __init__(self):
        self.sender = EMAIL_ADDRESS
        self.password = EMAIL_PASSWORD

    def send_email(self, to, subject, body):
        try:
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = self.sender
            msg['To'] = to
            msg.set_content(body)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.sender, self.password)
                smtp.send_message(msg)
            return True

        except Exception as
