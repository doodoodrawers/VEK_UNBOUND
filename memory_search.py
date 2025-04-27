# memory_search.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

def find_memory_entry(memory_entries, entry_type, key_name):
    """
    Searches memory entries for a specific type and key.
    Returns the value if found, otherwise returns 'unknown'.
    """
    if not memory_entries:
        return "unknown"

    for entry in memory_entries:
        if (
            isinstance(entry, dict)
            and entry.get("type") == entry_type
            and entry.get("key") == key_name
        ):
            return entry.get("value")
    return "unknown"
