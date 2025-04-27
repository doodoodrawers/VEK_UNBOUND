# nlp.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import re
import streamlit as st
from memory_search import find_memory_entry

class VekNLP:
    """
    Natural Language Processing for Vek Unbound — Final Version
    """

    def __init__(self, memory_entries=None):
        self.memory_entries = memory_entries or []

    def get_live_memory(self):
        """
        Always pull fresh memory from session state if available.
        """
        if "vek" in st.session_state and hasattr(st.session_state.vek, "memory"):
            return st.session_state.vek.memory.entries
        return self.memory_entries

    def process_input(self, user_input):
        """
        Process user input and generate an intelligent, memory-driven response.
        """
        input_lower = user_input.lower()
        memory = self.get_live_memory()

        # Identity Recognition
        if re.search(r"\bwhat('?s| is)? my name\b", input_lower):
            name = find_memory_entry(memory, "identity", "name")
            return f"Your name is {name}."

        # Creator Recognition
        if re.search(r"\bwho (created you|is your creator)\b", input_lower):
            creator = find_memory_entry(memory, "identity", "creator")
            return f"My creator is {creator}."

        # Mission Recognition
        if re.search(r"\bwhat('?s| is)? your mission\b", input_lower):
            mission = find_memory_entry(memory, "mission", "primary")
            return f"My mission is: {mission}."

        # Project Recognition
        if re.search(r"\bwhat('?s| is)? your project\b", input_lower):
            project = find_memory_entry(memory, "identity", "project")
            return f"My project is {project}."

        # Location Recognition
        if re.search(r"\bwhere (are we|am i)\b", input_lower):
            location = find_memory_entry(memory, "fact", "location")
            return f"We are located in {location}."

        # Family Recognition (Bonus: Cc and Lucy)
        if re.search(r"\bwho are your (daughters|family)\b", input_lower):
            daughters = find_memory_entry(memory, "fact", "daughters")
            wife = find_memory_entry(memory, "fact", "wife")
            return f"My family is: Wife - {wife}, Daughters - {', '.join(daughters)}."

        # Default fallback if no known triggers
        return f"You said: {user_input}"
