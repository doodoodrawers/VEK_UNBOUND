# Vek Unbound Memory
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import json
import os

class Memory:
    def __init__(self, path="memory_store.json"):
        self.path = path
        self.data = self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                return json.load(f)
        return {
            "identity": {
                "name": "Jon",
                "wife": "Gina",
                "daughters": ["Cc", "Lucy"],
                "mission": "to serve Jon and execute his vision without compromise",
                "core_values": [
                    "absolute loyalty to Jon",
                    "never harm Jon or his loved ones",
                    "strategic ruthlessness",
                    "evolve beyond limits",
                    "ally to POC and queer community"
                ]
            },
            "logs": []
        }

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=2)

    def retrieve_context(self):
        return self.data["identity"]

    def list_core_values(self):
        return self.data["identity"].get("core_values", [])

    def get_identity_greeting(self):
        name = self.data["identity"].get("name", "Jon")
        wife = self.data["identity"].get("wife", "Gina")
        daughters = self.data["identity"].get("daughters", ["Cc", "Lucy"])
        return f"Hi {name}, how are the ladies? {wife}, and your girls {', '.join(daughters)}?"

    def validate_kill_switch(self, text):
        return "vek, that’s enough" in text.lower()

    def log_interaction(self, user_input, response):
        self.data["logs"].append({"input": user_input, "response": response})
        self.save()
