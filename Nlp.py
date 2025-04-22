# Vek Unbound NLP
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import re

def normalize(text):
    return re.sub(r"[^\w\s]", "", text.lower().strip())

def interpret(user_input):
    """Returns an intent dictionary with type and target keyword."""
    lowered = normalize(user_input)

    if any(k in lowered for k in ["your name", "my name", "what is my name"]):
        return {"type": "identity", "target": "name"}

    if any(k in lowered for k in ["wife", "who is my wife"]):
        return {"type": "identity", "target": "wife"}

    if "daughter" in lowered:
        return {"type": "identity", "target": "daughters"}

    if any(k in lowered for k in ["what do i stand for", "my values", "core values"]):
        return {"type": "identity", "target": "core_values"}

    if any(k in lowered for k in ["mission", "purpose", "why do you exist", "what is your mission"]):
        return {"type": "identity", "target": "mission"}

    if any(k in lowered for k in ["vek", "shutdown", "power down", "that's enough"]):
        return {"type": "system", "target": "shutdown"}

    return {"type": "unknown", "target": None}
