# utils.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import datetime
import json
import os

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_json(data, path):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        return f"Failed to save JSON: {e}"

def load_json(path):
    try:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
    except Exception as e:
        return f"Failed to load JSON: {e}"

def readable_bytes(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T"]:
        if abs(num) < 1024.0:
            return f"{num:.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}P{suffix}"
