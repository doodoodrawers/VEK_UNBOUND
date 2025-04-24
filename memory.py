# memory.py
# Part of Vek Unbound: Genesis Loop
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import os
import json
from datetime import datetime

class Memory:
    def __init__(self, filename="vek_memory.json"):
        self.filename = filename
        self.entries = []
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    self.entries = json.load(f)
            except Exception as e:
                print(f"Failed to load memory file: {e}")
                self.entries = []

    def save(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.entries, f, indent=2)
        except Exception as e:
            print(f"Failed to save memory file: {e}")

    def log_entry(self, entry):
        if isinstance(entry, dict):
            entry["timestamp"] = datetime.now().isoformat()
            self.entries.append(entry)
        elif isinstance(entry, str):
            self.entries.append({"content": entry, "timestamp": datetime.now().isoformat()})
        else:
            self.entries.append({"content": str(entry), "timestamp": datetime.now().isoformat()})
        self.save()

    def get_entries(self):
        return self.entries

    def search(self, keyword):
        return [entry for entry in self.entries if keyword.lower() in str(entry).lower()]

    def clear(self):
        self.entries = []
        self.save()

    def latest(self, n=5):
        return self.entries[-n:]
