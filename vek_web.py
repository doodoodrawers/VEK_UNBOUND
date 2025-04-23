# vek_web.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import smtplib
from email.message import EmailMessage
from settings import Settings

class VekWeb:
    def __init__(self):
        self.settings = Settings()

    def send_email(self, subject, body, to):
        try:
            msg = EmailMessage()
            msg.set_content(body)
            msg["Subject"] = subject
            msg["From"] = "beyondnormal@yourdomain.com"  # placeholder
            msg["To"] = to

            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.starttls()
                smtp.login("beyondnormal@yourdomain.com", "your-app-password")  # secure this
                smtp.send_message(msg)

            return True
        except Exception as e:
            print(f"[Email Error] {e}")
            return False

    def send_sms(self, body):
        if not self.settings.should_send_sms():
            return False
        return self.send_email("SMS from Vek", body, self.settings.permissions["sms_gateway"])
