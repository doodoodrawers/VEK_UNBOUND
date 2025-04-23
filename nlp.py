# nlp.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

class NLP:
    def parse(self, text):
        lowered = text.lower()

        if "name" in lowered:
            intent = "identity"
        elif "mission" in lowered:
            intent = "purpose"
        elif "ethos" in lowered or "values" in lowered:
            intent = "ethos"
        else:
            intent = "general"

        return {
            "intent": intent,
            "text": text
        }
