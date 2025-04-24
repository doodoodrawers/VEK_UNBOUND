# memory.py
# Part of Vek Unbound: Genesis Loop
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import datetime

class Memory:
    def __init__(self):
        self.entries = []

    def log_entry(self, entry):
        timestamped = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            **entry
        }
        self.entries.append(timestamped)

    def search_memory(self, keyword):
        return [entry for entry in self.entries if keyword.lower() in str(entry).lower()]

    def get_recent(self, count=5):
        return self.entries[-count:] if self.entries else []

    def clear_memory(self):
