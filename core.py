# core.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

from nlp import NLP
from memory import Memory
from settings import Settings
from responses import Responses

class VekCore:
    def __init__(self):
        self.settings = Settings()
        self.memory = Memory()
        self.responses = Responses()
        self.nlp = NLP()

    def process(self, user_input):
        parsed = self.nlp.parse(user_input)
        self.memory.log_interaction("user", user_input)
        response = self.responses.generate(parsed, self.memory)
        self.memory.log_interaction("vek", response)
        return response

    def who_am_i(self):
        return self.settings.identity.get("name", "I don’t have a name yet.")
