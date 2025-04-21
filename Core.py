# Vek Unbound Core
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

from memory import Memory
from nlp import parse_input
from responses import generate_response

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
        return "System active."

    def process(self, user_input):
        user_input = user_input.strip()

        # Check for kill-switch
        if self.memory.validate_kill_switch(user_input):
            return "Understood. Powering down."

        # Parse input and respond
        intent, context = parse_input(user_input)
        response = generate_response(intent, context, self.memory)

        # Log interaction
        self.memory.log_interaction(user_input, response)

        return response
