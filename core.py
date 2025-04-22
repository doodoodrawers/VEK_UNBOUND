# core.py
# Vek Unbound: Core System Logic
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

from memory import Memory
from nlp import process_input
from settings import IDENTITY, MISSION, CORE_VALUES
from responses import get_response

class VekCore:
    def __init__(self):
        self.memory = Memory()
        self.identity = IDENTITY
        self.mission = MISSION
        self.core_values = CORE_VALUES
        self.initialized = False

    def initialize(self):
        if not self.initialized:
            self.memory.log("system", "Vek initialized.")
            self.initialized = True

    def process(self, user_input):
        self.memory.log("user", user_input)

        # Smart NLP Routing
        parsed = process_input(user_input)
        context = self.memory.retrieve_context(user_input)

        # Dynamic Response
        response = get_response(parsed, context, self.identity, self.mission)
        self.memory.log("vek", response)
        return response

    def ingest_file(self, filename, content):
        self.memory.ingest(filename, content)
        self.memory.log("system", f"Ingested file: {filename}")
