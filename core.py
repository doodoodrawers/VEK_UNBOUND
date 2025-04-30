# core.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from memory import Memory
from memory_search import find_memory_entry
from responses import generate_response

class VekCore:
    def __init__(self):
        if "vek" not in st.session_state:
            st.session_state.vek = self
            self.memory = Memory()
        else:
            self.memory = st.session_state.vek.memory

    def process(self, user_input):
        # Check for identity prompts
        input_lower = user_input.strip().lower()
        identity_keywords = ["what's my name", "what is my name", "who am i", "do you know me"]

        if any(kw in input_lower for kw in identity_keywords):
           name = self.memory.get("name")
                response = f"You're {name}."
            else:
                response = "I don't know your name yet. Tell me so I can remember."
            self.memory.log_interaction(user_input, response)
            return response

        # Generic fallback response
        response = generate_response(user_input)
        self.memory.log_interaction(user_input, response)
        return response
