# analytics.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

from logger import log_info, log_warning, log_error
from datetime import datetime
import json
import os

class Analytics:
    def __init__(self, path="analytics_data.json"):
        self.path = path
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, "r") as file:
                    return json.load(file)
            except Exception as e:
                log_error(f"Failed to load analytics data: {e}")
                return {}
        return {}

    def save_data(self):
        try:
            with open(self.path, "w") as file:
                json.dump(self.data, file, indent=2)
        except Exception as e:
            log_error(f"Failed to save analytics data: {e}")

    def log_event(self, category, event, metadata=None):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "timestamp": timestamp,
            "event": event,
            "metadata": metadata or {}
        }

        if category not in self.data:
            self.data[category] = []

        self.data[category].append(entry)
        self.save_data()
        log_info(f"Analytics logged: {category} -> {event}")
