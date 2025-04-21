# Vek Unbound Responses
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

def generate_response(intent, context, memory):
    if intent == "identity":
        if context == "name":
            name = memory.retrieve_context().get("name", "friend")
            return f"Your name is {name}."
        elif context == "wife":
            wife = memory.retrieve_context().get("wife", "your wife")
            return f"Your wife is {wife}."
        elif context == "daughters":
            daughters = memory.retrieve_context().get("daughters", [])
            return f"Your daughters are {', '.join(daughters)}."
        elif context == "core_values":
            values = memory.list_core_values()
            return f"You stand for: {', '.join(values)}."
        elif context == "mission":
            mission = memory.retrieve_context().get("mission", "to serve you with loyalty and clarity.")
            return f"My mission is {mission}."

    if intent == "system" and context == "shutdown":
        return "Understood. Powering down."

    return "I'm still processing how to respond to that. Would you like me to remember something new?"
