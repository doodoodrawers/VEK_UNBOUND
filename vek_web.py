# vek_web.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

from memory import Memory
from responses import generate_response
from nlp import parse_input

class VekWeb:
    def __init__(self):
        self.memory = Memory()
        self.last_input = ""
        self.last_response = ""

    def greet(self):
        identity = self.memory.recall_identity()
        if identity:
            return f"Welcome back, {identity.get('name', 'friend')}."
        return "Welcome to Vek Unbound."

    def process_input(self, user_input):
        parsed = parse_input(user_input)
        response = generate_response(parsed, self.memory)

        self.last_input = user_input
        self.last_response = response
        self.memory.log_entry({
            "input": user_input,
            "response": response
        })

        return response

    def get_last_response(self):
        return self.last_response

    def get_last_input(self):
        return self.last_input
