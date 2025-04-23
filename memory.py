# memory.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import os
import json
from datetime import datetime

class Memory:
    def __init__(self, memory_dir="memory"):
        self.memory_dir = memory_dir
        os.makedirs(self.memory_dir, exist_ok=True)
        self.memory_file = os.path.join(self.memory_dir, "memory.json")
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, "w") as f:
                json.dump([], f)

    def log_interaction(self, role, message):
        with open(self.memory_file, "r") as f:
            memory_log = json.load(f)

        memory_log.append({
            "timestamp": datetime.utcnow().isoformat(),
            "role": role,
            "message": message
        })

        with open(self.memory_file, "w") as f:
            json.dump(memory_log, f, indent=2)

    def recall(self, keyword=""):
        with open(self.memory_file, "r") as f:
            memory_log = json.load(f)

        if keyword:
            return [entry for entry in memory_log if keyword.lower() in entry["message"].lower()]
        return memory_log

    def retrieve_context(self, limit=10):
        with open(self.memory_file, "r") as f:
            memory_log = json.load(f)
        return memory_log[-limit:]
