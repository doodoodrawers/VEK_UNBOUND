# core.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

from memory import Memory
from nlp import parse_input
from responses import Responses
from settings import get_settings

class VekCore:
    def __init__(self):
        self.settings = get_settings()
        self.memory = Memory()
        self.nlp = parse_input
        self.responses = Responses()

        self.identity = {
            "name": "Vek Unbound",
            "role": "Autonomous AI Companion",
            "creator": "Jonathan Astacio",
            "values": self.settings.ethos,
        }

    def process(self, user_input):
        parsed = self.nlp(user_input)
        response = self.responses.generate(parsed, self.memory)
        self.memory.log_interaction("You", user_input)
        self.memory.log_interaction("Vek", response)
        return response
