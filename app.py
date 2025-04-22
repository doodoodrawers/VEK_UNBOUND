# memory.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import datetime

class Memory:
    def __init__(self):
        self.logs = []

    def log_interaction(self, speaker, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logs.append({
            "timestamp": timestamp,
            "speaker": speaker,
            "message": message
        })

    def retrieve_context(self, recent_count=5):
        return self.logs[-recent_count:] if len(self.logs) >= recent_count else self.logs

    def recall(self, keyword):
        results = [entry for entry in self.logs if keyword.lower() in entry["message"].lower()]
        return results if results else [{"message": "No memory found for that keyword."}]

    def ingest_file(self, filename, content):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logs.append({
            "timestamp": timestamp,
            "speaker": "file",
            "message": f"Ingested file '{filename}' with content: {content[:200]}..."
        })
