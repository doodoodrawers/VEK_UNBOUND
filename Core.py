# Vek Unbound Core
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

from memory import Memory
from nlp import interpret
from responses import respond

class VekCore:
    def __init__(self):
        self.memory = Memory()
        self.identity_greeted = False

    def startup(self):
        if not self.identity_greeted:
            self.identity_greeted = True
            return self.memory.get_identity_greeting()
        return "System active."

    def process(self, user_input):
        user_input = user_input.strip()

        if self.memory.validate_kill_switch(user_input):
            return "Understood. Powering down."

        # Semantic intent parsing
        intent = interpret(user_input)

        # Generate a memory-informed response
        response = respond(user_input, intent, self.memory)

        # Log the exchange
        self.memory.log_interaction(user_input, response)

        return response
