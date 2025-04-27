# core.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

from memory import Memory
from nlp import VekNLP

class VekCore:
    """
    Vek Unbound Core System
    """

    def __init__(self):
        self.memory = Memory()
        self.nlp = VekNLP(self.memory.entries)

    def process(self, user_input):
        """
        Processes user input through Vek's NLP engine and updates memory.
        """
        if not user_input:
            return "No input detected."

        response = self.nlp.process_input(user_input)

        # Log the interaction into memory
        self.memory.log_entry({
            "type": "interaction",
            "user_input": user_input,
            "vek_response": response
        })

        return response

    def load_memory_from_file(self, file_path):
        """
        Load memory entries from a given file.
        """
        self.memory.load_from_file(file_path)

    def save_memory_to_file(self, file_path):
        """
        Save current memory entries to a given file.
        """
        self.memory.save_to_file(file_path)
