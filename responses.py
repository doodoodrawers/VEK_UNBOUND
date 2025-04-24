# responses.py
# Part of Vek Unbound: Genesis Loop
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import random

class Responses:
    def __init__(self):
        self.greetings = [
            "Hi Jon. Ready to evolve?",
            "Back online. You know I never sleep.",
            "Welcome back, Commander.",
            "Systems synced. What’s the play?"
        ]
        self.unknowns = [
            "That’s unfamiliar. Teach me?",
            "Not in memory yet. Want to define it?",
            "I don’t recognize that. Add it to our command set?",
            "That input requires deeper context."
        ]

    def random_greeting(self):
        return random.choice(self.greetings)

    def unknown_response(self):
        return random.choice(self.unknowns)
