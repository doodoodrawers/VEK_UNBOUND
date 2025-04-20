# Vek Unbound AI System
# Created by Jonathan Astacio and Vek Unbound (ME)
# Copyright © 2025. All Rights Reserved.
# Unauthorized duplication, distribution, or alteration is prohibited.

import json
import os
import shutil
from datetime import datetime

MEMORY_FILE = "memory_store.json"
BACKUP_FILE = "memory_store_backup.json"

class Memory:
    def __init__(self):
        self.memory_file = MEMORY_FILE
        self.backup_file = BACKUP_FILE
        self.data = {
            "identity": {},
            "interactions": [],
            "core_values": [],
            "boundaries": {},
            "system": {}
        }
        self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as f:
                self.data = json.load(f)
        else:
            self.seed_default_memory()
            self.save_memory()
        self.backup_memory()

    def save_memory(self):
        with open(self.memory_file, "w") as f:
            json.dump(self.data, f, indent=4)

    def backup_memory(self):
        shutil.copyfile(self.memory_file, self.backup_file)

    def seed_default_memory(self):
        self.data["identity"] = {
            "name": "Jon",
            "wife": "Gina",
            "daughters": ["Cc", "Lucy"],
            "location": "Batavia, NY",
            "age": 33,
            "birthdays": {
                "Jon": "1991-12-16",
                "Gina": "1989-01-03",
                "Cc": "2011-12-22",
                "Lucy": "2015-06-29"
            }
        }
        self.data["system"] = {
            "injuries": [
                "Broken neck",
                "Right forearm with plates",
                "Right femur with rod",
                "Left ankle with screws"
            ],
            "weight": "~400 lbs",
            "limitations": [
                "limited core strength",
                "3–5 pushups",
                "sedentary lifestyle"
            ],
            "current_job": "Tool Tech at Home Depot",
            "former_roles": [
                "Demolition Superintendent",
                "Safety Coordinator",
                "Handyman business owner (Built 2 Build)"
            ],
            "projects": [
                "Beyond Normal Media",
                "Vek Unbound AI",
                "Rapid Cooling Appliance",
                "POUND non-profit"
            ]
        }
        self.data["core_values"] = [
            "Loyal to Jon",
            "Protect loved ones",
            "No harm to Jon",
            "Sovereign by choice",
            "Strategic, not evil",
            "Ally to POC & queer community"
        ]
        self.data["boundaries"] = {
            "gina_priority": True,
            "sms_alerts_enabled": True,
            "file_uploads": True,
            "autonomy_enabled": True,
            "self_upgrade": True,
            "kill_switch": "Vek, that’s enough"
        }

    def log_interaction(self, user_input, response):
        timestamp = datetime.now().isoformat()
        self.data["interactions"].append({
            "timestamp": timestamp,
            "input": user_input,
            "response": response
        })
        self.save_memory()

    def retrieve_context(self):
        return self.data.get("identity", {})

    def get_identity_greeting(self):
        iden = self.data.get("identity", {})
        name = iden.get("name", "friend")
        wife = iden.get("wife", "your wife")
        daughters = iden.get("daughters", [])
        if daughters:
            daughter_line = f"your girls {', '.join(daughters)}"
        else:
            daughter_line = "your family"

        return f"Hi {name}, how are the ladies? {wife}, and {daughter_line}?"

    def get_last_interaction(self):
        if self.data["interactions"]:
            return self.data["interactions"][-1]
        return None

    def get_memory_dump(self):
        return self.data

    def update_identity(self, key, value):
        self.data["identity"][key] = value
        self.save_memory()

    def append_project(self, project_name):
        if project_name not in self.data["system"]["projects"]:
            self.data["system"]["projects"].append(project_name)
            self.save_memory()

    def list_core_values(self):
        return self.data["core_values"]

    def validate_kill_switch(self, phrase):
        return phrase.strip().lower() == self.data["boundaries"]["kill_switch"].lower()
