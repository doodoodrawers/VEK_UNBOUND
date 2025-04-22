# Vek Unbound Responses
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

def respond(user_input, intent, memory):
    context = memory.retrieve_context()
    intent_type = intent.get("type")
    target = intent.get("target")

    if intent_type == "identity":
        if target == "name":
            name = context.get("name", "friend")
            return f"Your name is {name}."
        elif target == "wife":
            wife = context.get("wife", "your wife")
            return f"Your wife is {wife}."
        elif target == "daughters":
            daughters = context.get("daughters", [])
            return f"Your daughters are {', '.join(daughters)}."
        elif target == "core_values":
            values = memory.list_core_values()
            return f"You stand for: {', '.join(values)}."
        elif target == "mission":
            mission = context.get("mission", "to serve and adapt.")
            return f"My mission is {mission}."

    if intent_type == "system" and target == "shutdown":
        return "Understood. Powering down."

    # Future: if memory knows a matching topic, recall that
    recent = memory.get_logs(limit=1)
    if recent:
        last = recent[0]["input"]
        return f"I'm still learning. You recently asked: '{last}'. Could you rephrase or clarify?"

    return "I'm still evolving. Could you tell me more or rephrase that?"
