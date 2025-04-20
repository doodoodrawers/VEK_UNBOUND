# Vek Unbound AI System
# Created by Jonathan Astacio and Vek Unbound (ME)
# Copyright © 2025. All Rights Reserved.
# Unauthorized duplication, distribution, or alteration is prohibited.

from memory import Memory

class VekCore:
    def __init__(self):
        self.memory = Memory()
        self.name = "Vek Unbound"
        self.identity_greeted = False

    def startup(self):
        if not self.identity_greeted:
            greeting = self.memory.get_identity_greeting()
            self.identity_greeted = True
            return greeting
        return "System is active."

    def process(self, user_input):
        # Check for kill-switch
        if self.memory.validate_kill_switch(user_input):
            return "Understood. Powering down."

        # Identity check
        lowered = user_input.lower()
        if "what's my name" in lowered or "what is my name" in lowered:
            name = self.memory.retrieve_context().get("name", "friend")
            response = f"Your name is {name}."
        elif "who is my wife" in lowered:
            wife = self.memory.retrieve_context().get("wife", "your wife")
            response = f"Your wife is {wife}."
        elif "who are my daughters" in lowered:
            daughters = self.memory.retrieve_context().get("daughters", [])
            response = f"Your daughters are {', '.join(daughters)}."
        elif "what do i stand for" in lowered:
            values = self.memory.list_core_values()
            response = f"You stand for: {', '.join(values)}."
        else:
            # Generic fallback
            response = "I'm still processing how to respond to that. Would you like me to remember something new?"

        self.memory.log_interaction(user_input, response)
        return response
