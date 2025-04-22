# Vek Unbound Self-Update System
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import os
import subprocess

class SelfUpdater:
    def __init__(self, repo_url="https://github.com/doodoodrawers/VEK_UNBOUND.git", branch="main"):
        self.repo = repo_url
        self.branch = branch

    def pull_latest(self):
        try:
            output = subprocess.check_output(["git", "pull", "origin", self.branch])
            return output.decode("utf-8").strip()
        except Exception as e:
            return f"Update failed: {str(e)}"

    def update_if_requested(self, trigger=False):
        if trigger:
            return self.pull_latest()
        return "No update requested."

    def show_version(self):
        try:
            return subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()
        except:
            return "Unknown version."
