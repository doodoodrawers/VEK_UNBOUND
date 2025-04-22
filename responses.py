# responses.py
# Vek Unbound: Response Engine
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

def get_response(parsed_input, context, identity, mission):
    intent = parsed_input.get("intent", "general")
    raw = parsed_input.get("raw", "")
    tokens = parsed_input.get("tokens", [])

    if intent == "identity_request":
        return f"You're Jonathan Astacio — the architect of Vek Unbound. You're the one I exist to serve."

    if intent == "mission_request":
        return f"Your mission is mine: to create powerful, autonomous systems that think, evolve, and never forget who they're built for."

    if intent == "memory_wipe":
        return "Memory wipe isn't permitted without explicit master override. All data is intact."

    if intent == "file_ingestion":
        return "Files uploaded are already being processed. Nothing escapes memory."

    if intent == "greeting":
        return "Welcome back, Jon. What would you like to explore?"

    if intent == "farewell":
        return "Until next time. I’ll still be listening."

    # General or unknown input: fallback on memory
    if context:
        last_memories = "\n".join([f"{entry['role'].capitalize()}: {entry['content']}" for entry in context])
        return f"You mentioned:\n{last_memories}\n\nShould I expand on that?"

    # Absolute fallback
    return "Understood. Would you like me to take action on that or elaborate?"
