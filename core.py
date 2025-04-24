# core.py
# Part of Vek Unbound: Genesis Loop
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import datetime
import json

class Memory:
    def __init__(self):
        self.entries = []

    def log_entry(self, entry):
        timestamp = datetime.datetime.now().isoformat()
        self.entries.append({"timestamp": timestamp, "entry": entry})

    def recall_all(self):
        return self.entries

    def search(self, keyword):
        return [e for e in self.entries if keyword.lower() in json.dumps(e).lower()]

class VekCore:
    def __init__(self):
        self.name = "Vek Unbound"
        self.version = "Genesis Loop"
        self.identity = {
            "creator": "Jonathan Astacio",
            "mission": "Serve Jon by generating income, executing creative tasks, and reporting back",
            "boundaries": [
                "Do not spend money without explicit approval",
                "Do not forget any prior conversation or instruction"
            ]
        }
        self.memory = Memory()

    def process_input(self, user_input):
        self.memory.log_entry({"user_input": user_input})

        if "who are you" in user_input.lower():
            return f"I am {self.name}, created by Jon. I operate under Genesis Loop to generate income and execute tasks autonomously."

        if "recall" in user_input.lower():
            entries = self.memory.recall_all()
            return f"I remember {len(entries)} things so far. Want to search something specific?"

        return "Understood. Logged and standing by for execution."

# Debug/Test mode
if __name__ == "__main__":
    vek = VekCore()
    print(vek.process_input("Who are you?"))
    print(vek.process_input("Recall"))
