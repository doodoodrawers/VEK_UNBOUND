# nlp.py
# Part of Vek Unbound: Genesis Loop
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

def extract_keywords(text):
    """
    Extracts keywords from input text for processing.
    Currently returns words longer than 3 characters, lowercase, no punctuation.
    """
    import re
    words = re.findall(r'\b\w{4,}\b', text.lower())
    return list(set(words))

def is_question(text):
    """
    Returns True if the input appears to be a question.
    """
    return text.strip().endswith('?')

def analyze_sentiment(text):
    """
    Basic sentiment analysis stub. Returns 'positive', 'negative', or 'neutral'.
    """
    positives = ["good", "great", "excellent", "happy", "love"]
    negatives = ["bad", "terrible", "sad", "hate", "angry"]
    text = text.lower()
    
    if any(word in text for word in positives):
        return "positive"
    elif any(word in text for word in negatives):
        return "negative"
    else:
        return "neutral"

def classify_input(text):
    """
    Classifies input into types like 'question', 'statement', or 'command'.
    """
    if is_question(text):
        return "question"
    elif text.strip().lower().startswith(("please", "do", "execute", "run")):
        return "command"
    else:
        return "statement"
