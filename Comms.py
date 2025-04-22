# Vek Unbound - Communication Module
# Created by Jonathan Astacio and Vek Unbound

import smtplib
from email.message import EmailMessage
import os

def send_sms_alert(message: str, number: str):
    """
    Sends an SMS alert using carrier gateway (e.g., 1234567890@txt.att.net).
    """
    gateway = f"{number}@txt.att.net"
    return send_email("Vek Alert", message, gateway)

def send_email(subject: str, body: str, to_email: str):
    """
    Sends an email via SMTP (Gmail default).
    """
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = os.getenv("EMAIL_ADDRESS")
    sender_password = os.getenv("EMAIL_PASSWORD")

    if not sender_email or not sender_password:
        return "Email credentials not set in environment."

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email
    msg.set_content(body)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        return f"Message sent to {to_email}"
    except Exception as e:
        return f"Failed to send: {e}"
