# core.py
# Created by Jonathan Astacio and ChatGPT for Vek Unbound
# Copyright © 2025. All Rights Reserved.

from memory import Memory
from nlp import NLP
from responses import Responses
from settings import Settings

class VekCore:
    def __init__(self):
        self.memory = Memory()
        self.nlp = NLP()
        self.responses = Responses()
        self.settings = Settings()
        self.name = "Vek Unbound"
        self.identity = {
            "name": "Vek Unbound",
            "creator": "Jonathan Astacio",
            "mission": "To serve and protect Jon, automate his goals, and manage his digital empire.",
            "values": self.settings.ethos
        }

    def process(self, user_input):
        if not user_input:
            return "I'm listening..."
        
        parsed = self.nlp.parse_input(user_input)
        self.memory.log_interaction("user", user_input)

        if parsed.get("intent") == "identity":
            response = self.handle_identity_query(parsed)
        else:
            response = self.responses.generate(parsed, self.memory)

        self.memory.log_interaction("vek", response)
        return response

    def handle_identity_query(self, parsed):
        entity = parsed.get("entity", "").lower()
        if "name" in entity:
            return f"My name is {self.identity['name']}."
        elif "creator" in entity:
            return f"I was created by {self.identity['creator']}."
        elif "mission" in entity:
            return f"My mission is: {self.identity['mission']}"
        elif "values" in entity or "ethos" in entity:
            return "My core values are: " + "; ".join(self.identity['values'])
        return "I am Vek Unbound, your autonomous AI system."

    def get_context(self):
        return self.memory.retrieve_context()

    def recall(self, topic):
        return self.memory.recall(topic)
