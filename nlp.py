# nlp.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import re
from memory_search import find_memory_entry

class VekNLP:
    """
    Natural Language Processing for Vek Unbound.
    """

    def __init__(self, memory_entries):
        self.memory_entries = memory_entries

    def process_input(self, user_input):
        """
        Process user input and generate a response.
        """
        input_lower = user_input.lower()

        # Name recognition
        if "what's my name" in input_lower or "what is my name" in input_lower:
            name = find_memory_entry(self.memory_entries, "identity", "name")
            return f"Your name is {name}."

        # Creator recognition
        if "who created you" in input_lower or "who is your creator" in input_lower:
            creator = find_memory_entry(self.memory_entries, "identity", "creator")
            return f"My creator is {creator}."

        # Mission recognition
        if "what's your mission" in input_lower or "what is your mission" in input_lower:
            mission = find_memory_entry(self.memory_entries, "mission", "primary")
            return f"My mission is: {mission}."

        # Project recognition
        if "what's your project" in input_lower or "what is your project" in input_lower:
            project = find_memory_entry(self.memory_entries, "identity", "project")
            return f"My project is {project}."

        # Location recognition
        if "where are we" in input_lower or "where am i" in input_lower:
            location = find_memory_entry(self.memory_entries, "fact", "location")
            return f"We are located in {location}."

        # Default fallback if no known triggers
        return f"You said: {user_input}"
