# comms.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import json
import os
import requests

class CommunicationHub:
    def __init__(self):
        self.discord_webhook = os.getenv("DISCORD_WEBHOOK_URL")
        self.telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

    def send_discord(self, message: str) -> bool:
        if not self.discord_webhook:
            print("Discord webhook not configured.")
            return False
        payload = {"content": message}
        try:
            response = requests.post(self.discord_webhook, json=payload)
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Discord send failed: {e}")
            return False

    def send_telegram(self, message: str) -> bool:
        if not self.telegram_token or not self.telegram_chat_id:
            print("Telegram credentials missing.")
            return False
        url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        payload = {
            "chat_id": self.telegram_chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Telegram send failed: {e}")
            return False
