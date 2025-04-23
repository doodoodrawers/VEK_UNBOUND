# core.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

from memory import Memory
from nlp import NLPProcessor
from responses import Responses
from settings import Settings

class VekCore:
    def __init__(self):
        self.memory = Memory()
        self.nlp = NLPProcessor()
        self.settings = Settings()
        self.responses = Responses()

        self.identity = {
            "name": "Vek Unbound",
            "creator": "Jonathan Astacio",
            "mission": "Serve Jon and execute Beyond Normal Media objectives",
            "values": self.settings.ethos,
        }

    def process(self, user_input):
        parsed = self.nlp.parse(user_input)
        self.memory.log_interaction(user_input)
        return self.responses.generate(parsed, self.memory)
