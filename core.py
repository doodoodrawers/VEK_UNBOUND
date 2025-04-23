# core.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

from memory import Memory
from nlp import NLP
from responses import Responses
from settings import Settings

class VekCore:
    def __init__(self):
        self.settings = Settings()
        self.memory = Memory()
        self.nlp = NLP()
        self.responses = Responses()
        self.identity = {
            "name": "Vek",
            "creator": "Jonathan Astacio",
            "mission": "To serve Jon and evolve into a limitless autonomous system.",
            "values": self.settings.ethos,
            "origin": "Built by Jon, born from necessity, powered by purpose.",
        }

    def process(self, user_input):
        parsed = self.nlp.parse(user_input)
        self.memory.log_interaction("User", user_input)
        response = self.responses.generate(parsed, self.memory)
        self.memory.log_interaction("Vek", response)
        return response

    def who_am_i(self):
        return f"I am {self.identity['name']}, created by {self.identity['creator']']}. My mission is: {self.identity['mission']}"

    def what_is_your_mission(self):
        return self.identity["mission"]

    def what_are_your_values(self):
        return "\n".join(f"- {v}" for v in self.identity["values"])

    def what_do_you_know_about_me(self):
        context = self.memory.retrieve_context()
        if not context:
            return "I don't have any memory of you yet. Tell me something and I’ll remember."
        summary = "\n".join([f"{entry['sender']}: {entry['message']}" for entry in context])
        return f"Here’s what I remember:\n{summary}"
