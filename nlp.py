# nlp.py
# Vek Unbound: Natural Language Processor
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import re

def process_input(user_input):
    tokens = tokenize(user_input)
    intent = detect_intent(tokens, user_input)
    return {
        "raw": user_input,
        "tokens": tokens,
        "intent": intent
    }

def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())

def detect_intent(tokens, text):
    # Quick priority checks
    lowered = text.lower()

    if "who am i" in lowered or "what's my name" in lowered:
        return "identity_request"
    if "mission" in lowered or "what do i stand for" in lowered:
        return "mission_request"
    if "reset" in lowered or "clear memory" in lowered:
        return "memory_wipe"
    if "upload" in lowered or "ingest" in lowered:
        return "file_ingestion"
    if any(word in tokens for word in ["hi", "hello", "hey"]):
        return "greeting"
    if any(word in tokens for word in ["bye", "goodbye"]):
        return "farewell"

    return "general"
