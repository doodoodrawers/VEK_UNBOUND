# tikmanager.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import os
import datetime
from utils import timestamp

class TikTokManager:
    def __init__(self):
        self.upload_log = []
        self.failed_uploads = []
        self.auto_mode = False

    def prepare_post(self, content, filepath=None, hashtags=None):
        post = {
            "content": content,
            "filepath": filepath or "",
            "hashtags": hashtags or [],
            "timestamp": timestamp()
        }
        return post

    def upload_post(self, post):
        try:
            # Placeholder for actual TikTok API or third-party integration
            success = True  # Simulate upload success

            if success:
                self.upload_log.append(post)
                return f"Uploaded successfully: {post['content'][:30]}..."
            else:
                raise Exception("Upload failed due to unknown error")

        except Exception as e:
            post["error"] = str(e)
            self.failed_uploads.append(post)
            return f"Failed to upload: {e}"

    def enable_auto_upload(self):
        self.auto_mode = True
        return "Auto-upload mode enabled."

    def disable_auto_upload(self):
        self.auto_mode = False
        return "Auto-upload mode disabled."

    def get_upload_summary(self):
        return {
            "total_uploaded": len(self.upload_log),
            "failed_uploads": len(self.failed_uploads),
            "auto_mode": self.auto_mode
        }
