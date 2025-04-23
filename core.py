# core.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

from nlp import NLP
from memory import Memory
from responses import Responses
from settings import Settings
from datetime import datetime

class VekCore:
    def __init__(self):
        self.settings = Settings()
        self.nlp = NLP()
        self.memory = Memory()
        self.responses = Responses()
        self.identity = {
            "name": "Vek",
            "role": "Autonomous AI",
            "created_by": "Jonathan Astacio",
            "mission": "To serve Jon's will and uphold his values.",
            "ethos": self.settings.ethos,
            "initialized": str(datetime.now())
        }

    def process(self, user_input):
        parsed = self.nlp.parse(user_input)
        self.memory.log_interaction("User", user_input)
        response = self.responses.generate(parsed, self.memory)
        self.memory.log_interaction("Vek", response)
        return response

    def who_am_i(self):
        return "You are {}, my creator and the one I serve.".format(self.identity["created_by"])

    def what_is_your_mission(self):
        return self.identity["mission"]

    def what_is_your_ethos(self):
        return "\n".join(self.identity["ethos"])
