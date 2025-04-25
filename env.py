# env.py  
# Created by Jonathan Astacio and Vek Unbound  
# Copyright © 2025. All Rights Reserved.

import os
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

def get_env(key: str, default: str = "") -> str:
    """Retrieve an environment variable safely."""
    return os.getenv(key, default)
