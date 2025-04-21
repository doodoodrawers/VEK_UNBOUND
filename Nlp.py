# Vek Unbound NLP
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

def parse_input(user_input):
    lowered = user_input.lower()

    if "name" in lowered:
        return "identity", "name"
    elif "wife" in lowered:
        return "identity", "wife"
    elif "daughter" in lowered:
        return "identity", "daughters"
    elif "stand for" in lowered:
        return "identity", "core_values"
    elif "mission" in lowered:
        return "identity", "mission"
    elif "kill" in lowered or "shutdown" in lowered:
        return "system", "shutdown"

    return "unknown", None
