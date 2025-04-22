# Vek Unbound Core
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

from memory import Memory
from nlp import interpret
from responses import respond
from self_update import SelfUpdater

class VekCore:
    def __init__(self):
        self.memory = Memory()
        self.identity_greeted = False
        self.updater = SelfUpdater()

    def startup(self):
        if not self.identity_greeted:
            self.identity_greeted = True
            return self.memory.get_identity_greeting()
        return "System active."

    def process(self, user_input):
        user_input = user_input.strip()

        # Kill switch
        if self.memory.validate_kill_switch(user_input):
            return "Understood. Powering down."

        # Trigger self-update if requested
        if "update yourself" in user_input.lower() or self.memory.data.get("flags", {}).get("update_now"):
            update_status = self.updater.pull_latest()
            return f"Update result: {update_status}"

        # Semantic intent detection
        intent = interpret(user_input)

        # Generate dynamic response
        response = respond(user_input, intent, self.memory)

        # Log interaction
        self.memory.log_interaction(user_input, response)

        return response
