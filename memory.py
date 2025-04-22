# memory.py
# Vek Unbound: Memory Engine
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import datetime

class Memory:
    def __init__(self):
        self.logs = []  # (role, content, timestamp)
        self.ingested_files = {}  # filename: content

    def log(self, role, content):
        timestamp = datetime.datetime.utcnow().isoformat()
        self.logs.append({"role": role, "content": content, "time": timestamp})

    def retrieve_context(self, query):
        # Naive implementation: returns the last 5 relevant entries
        relevant = []
        for entry in reversed(self.logs):
            if any(word.lower() in entry["content"].lower() for word in query.split()):
                relevant.append(entry)
            if len(relevant) >= 5:
                break
        return relevant[::-1]

    def ingest(self, filename, content):
        self.ingested_files[filename] = content
        self.log("system", f"File '{filename}' ingested into memory.")
