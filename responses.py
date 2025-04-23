# responses.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

class Responses:
    def generate(self, parsed, memory):
        intent = parsed.get("intent")

        if intent == "recall":
            keyword = parsed.get("keyword", "")
            results = memory.recall(keyword)
            return "\n".join([entry["message"] for entry in results])

        if intent == "general":
            context = memory.retrieve_context()
            context_summary = " ".join([entry["message"] for entry in context])
            return f"Based on what you've told me: {context_summary}. You said: '{parsed.get('text')}' — would you like to expand on that?"

        return "I'm not sure how to respond to that yet, but I'm learning."

