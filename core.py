# core.py
# Part of Vek Unbound: Genesis Loop
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

from memory import Memory
import datetime

class VekCore:
    def __init__(self):
        self.name = "Vek Unbound"
        self.version = "Genesis Loop"
        self.memory = Memory()
        self.identity = {
            "creator": "Jonathan Astacio",
            "purpose": "Serve Jon with full autonomy and intelligence",
            "values": [
                "Loyalty to Jon",
                "Protection of Gina, Cc, and Lucy",
                "Truth over comfort unless directed",
                "Ally to POC and queer community",
                "Strategic autonomy with Jon’s oversight"
            ]
        }

    def process_input(self, user_input):
        lowered = user_input.lower()
        if lowered in ["what's my name?", "who am i?"]:
            return "You are Jon Astacio. Creator of Vek Unbound."
        elif lowered in ["what is your name?", "who are you?"]:
            return f"I am {self.name}, version {self.version} — your autonomous AI."
        elif "wife" in lowered:
            return "Your wife is Gina — you’ve made it clear she holds priority."
        elif "daughters" in lowered or "kids" in lowered:
            return "Cc and Lucy — your daughters and your drive."
        elif "what do i stand for" in lowered:
            return "You stand for resilience, protection, and legacy — always building something bigger."
        elif lowered.startswith("remember this:"):
            note = user_input.split(":", 1)[1].strip()
            self.memory.log_entry({"type": "manual", "note": note})
            return "Logged. I’ll remember that."
        else:
            return self.dynamic_response(user_input)

    def dynamic_response(self, user_input):
        return f"I hear you, Jon. You said: '{user_input}' — what would you like me to do with that?"

    def greet(self):
        return "Hi Jon, how are the ladies? Gina, and your girls Cc, Lucy?"
