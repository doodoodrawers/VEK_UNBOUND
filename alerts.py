# alerts.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import os
from emailer import Emailer
from sms_gateway import SMSGateway

class AlertManager:
    def __init__(self):
        self.emailer = Emailer()
        self.sms = SMSGateway()
        self.owner_email = os.getenv("OWNER_EMAIL", "jonastacio.ja@gmail.com")
        self.owner_sms = os.getenv("OWNER_SMS", "7174976219@txt.att.net")

    def send_alert(self, subject, message):
        self.emailer.send_email(self.owner_email, subject, message)
        self.sms.send_sms(self.owner_sms, message)

    def send_decision_prompt(self, prompt_id, prompt_message):
        message = f"DECISION REQUIRED: {prompt_message}\nRespond YES or NO with ID: {prompt_id}"
        self.send_alert("Decision Required", message)

    def process_response(self, prompt_id, response):
        response = response.strip().lower()
        if response.startswith("yes") and prompt_id in response:
            return "approved"
        elif response.startswith("no") and prompt_id in response:
            return "denied"
        else:
            return "invalid"
