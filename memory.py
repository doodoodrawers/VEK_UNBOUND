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
            return {"context": "no_memory"}

        if query:
            relevant = [e["entry"] for e in self.entries if query in e["entry"]]
            if relevant:
                return {"context": relevant[0]}  # first match
            else:
                return {"context": "no_relevant_memory"}
        else:
            return {"context": "general_memory"}

    def full_recall(self):
        return self.entries

    def forget_all(self):
        self.entries = []

    def log_interaction(self, user_input, response):
        entry = f"User: {user_input} -> Vek: {response}"
        self.log_entry(entry)

    def load_entries(self, entries):
        self.entries.extend(entries)
