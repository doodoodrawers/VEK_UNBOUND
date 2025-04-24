# memory.py
# Part of Vek Unbound: Genesis Loop
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import json
import os
import datetime

class Memory:
    def __init__(self, memory_file='memory.json'):
        self.memory_file = memory_file
        self.entries = []
        self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                try:
                    self.entries = json.load(f)
                except json.JSONDecodeError:
                    self.entries = []

    def save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.entries, f, indent=4)

    def log_entry(self, entry):
        timestamped_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            **entry
        }
        self.entries.append(timestamped_entry)
        self.save_memory()

    def get_recent(self, count=10):
        return self.entries[-count:]
