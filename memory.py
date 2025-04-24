# memory.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

class Memory:
    def __init__(self):
        self.store = []

    def log_interaction(self, role, message):
        self.store.append({"role": role, "message": message})

    def retrieve_context(self):
        return self.store[-10:] if len(self.store) > 10 else self.store

    def log_entry(self, entry):
        """Logs a single memory entry, regardless of type."""
        self.store.append(entry)
