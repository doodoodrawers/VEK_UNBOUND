# sms.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import smtplib
from email.message import EmailMessage
import streamlit as st
from utils import get_env

class SMSClient:
    def __init__(self):
        self.gateway = get_env("SMS_GATEWAY", "7174976219@txt.att.net")
        self.smtp_server = get_env("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = int(get_env("SMTP_PORT", 587))
        self.sender_email = get_env("SENDER_EMAIL")
        self.sender_password = get_env("SENDER_PASSWORD")

    def send_sms(self, subject, body):
        try:
            msg = EmailMessage()
            msg["From"] = self.sender_email
            msg["To"] = self.gateway
            msg["Subject"] = subject
            msg.set_content(body)

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)

            st.success("SMS sent successfully.")
        except Exception as e:
            st.error(f"Failed to send SMS: {e}")
