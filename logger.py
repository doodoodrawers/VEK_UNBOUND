# logger.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import logging
import os

LOG_FILE = "vek_unbound.log"

# Ensure the log file directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True) if "/" in LOG_FILE else None

# Configure the logger
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("vek")

def log_info(message):
    logger.info(message)

def log_warning(message):
    logger.warning(message)

def log_error(message):
    logger.error(message)

def log_debug(message):
    logger.debug(message)
