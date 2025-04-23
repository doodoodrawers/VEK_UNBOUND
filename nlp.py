# nlp.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

class NLP:
    def parse_input(self, text):
        lowered = text.lower()
        if "your name" in lowered or "who are you" in lowered:
            return {"intent": "identity", "entity": "name"}
        elif "creator" in lowered or "who made you" in lowered:
            return {"intent": "identity", "entity": "creator"}
        elif "mission" in lowered:
            return {"intent": "identity", "entity": "mission"}
        elif "ethos" in lowered or "values" in lowered:
            return {"intent": "identity", "entity": "values"}
        elif "recall" in lowered:
            keyword = lowered.split("recall", 1)[-1].strip()
            return {"intent": "recall", "keyword": keyword}
        else:
            return {"intent": "general", "text": text}

    def analyze_intent(self, text):
        return self.parse_input(text)  # Alias for compatibility
