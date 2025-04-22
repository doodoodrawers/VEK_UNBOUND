# nlp.py
# Vek Unbound NLP
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import re

def normalize(text):
    return re.sub(r"[^\w\s]", "", text.lower())

def interpret(user_input):
    """
    Returns an intent dictionary with type and target.
    """
    lowered = normalize(user_input)

    if any(k in lowered for k in ["your name", "who are you", "what is your name"]):
        return {"type": "identity", "target": "name"}
    
    if any(k in lowered for k in ["wife", "your wife", "gina"]):
        return {"type": "identity", "target": "wife"}
    
    if any(k in lowered for k in ["daughters", "kids", "your daughters", "cc", "lucy"]):
        return {"type": "identity", "target": "daughters"}
    
    if any(k in lowered for k in ["what do i stand for", "core values", "beliefs"]):
        return {"type": "identity", "target": "core_values"}
    
    if any(k in lowered for k in ["mission", "why do you exist", "your goal"]):
        return {"type": "identity", "target": "mission"}

    if any(k in lowered for k in ["power down", "shutdown", "stop talking", "vek thats enough"]):
        return {"type": "system", "target": "kill"}

    return {"type": "unknown", "target": "none"}
