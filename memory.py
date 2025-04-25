# memory.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import datetime

class Memory:
    def __init__(self):
        self.entries = []

    def log_entry(self, entry):
        timestamp = datetime.datetime.now().isoformat()
        self.entries.append({"timestamp": timestamp, "entry": entry})

    def retrieve_context(self, query=None):
        if not self.entries:
            return "There is no memory yet."

        if query:
            relevant = [e["entry"] for e in self.entries if query.lower() in str(e["entry"]).lower()]
            return relevant if relevant else "No relevant memories found."
        else:
            return [e["entry"] for e in self.entries[-10:]]

    def full_recall(self):
        return self.entries

    def forget_all(self):
        self.entries = []
