# nlp.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import re

class NLP:
    def __init__(self):
        self.commands = {
            "greet": ["hi", "hello", "hey", "greetings"],
            "status": ["how are you", "what's up", "how's it going"],
            "start": ["start system", "initialize", "boot up"],
            "stop": ["shutdown", "stop system", "terminate"],
            "upload": ["upload memory", "add file", "load data"],
            "diagnostics": ["run diagnostics", "system check", "scan system"],
            "alert": ["send alert", "test alert", "trigger warning"],
            "reset": ["clear memory", "reset context", "wipe logs"]
        }

    def normalize(self, text):
        return re.sub(r"[^\w\s]", "", text.lower()).strip()

    def interpret(self, input_text):
        input_text = self.normalize(input_text)
        for command, phrases in self.commands.items():
            for phrase in phrases:
                if phrase in input_text:
                    return command
        return "unknown"
