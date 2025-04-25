# invideo.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import requests
import json
from utils import timestamp

class InVideoManager:
    def __init__(self, api_key=None):
        self.api_key = api_key or "INVIDEO_API_KEY_PLACEHOLDER"
        self.base_url = "https://api.invideo.io/v1"
        self.project_log = []

    def generate_video(self, title, script_text, voice_id="en-US-Wavenet-D"):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "title": title,
            "script": script_text,
            "voice": voice_id,
            "timestamp": timestamp()
        }

        try:
            # Simulate request to InVideo API (replace with real endpoint)
            response = requests.post(f"{self.base_url}/generate", headers=headers, data=json.dumps(payload))

            if response.status_code == 200:
                video_data = response.json()
                self.project_log.append(video_data)
                return f"Video created: {video_data.get('video_url', 'URL unavailable')}"
            else:
                return f"Failed to create video: {response.status_code} - {response.text}"

        except Exception as e:
            return f"InVideo error: {str(e)}"

    def get_project_log(self):
        return self.project_log
