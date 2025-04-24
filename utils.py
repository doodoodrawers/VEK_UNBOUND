# utils.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

def format_response(text):
    """
    Clean and format the AI's raw response for presentation.
    """
    return text.strip()


def truncate_text(text, max_length=2000):
    """
    Shorten long text to avoid overflow issues.
    """
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text


def is_valid_input(user_input):
    """
    Basic validation to ensure input isn't empty or malformed.
    """
    return bool(user_input and user_input.strip())


def extract_keywords(text):
    """
    Placeholder for NLP keyword extraction. Expand in future.
    """
    return [word.strip('.,!?') for word in text.lower().split() if len(word) > 3]
