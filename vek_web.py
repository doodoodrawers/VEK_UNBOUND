# vek_web.py
# Part of Vek Unbound: Genesis Loop
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
import requests

class VekWeb:
    def __init__(self):
        self.session = requests.Session()

    def fetch_page_title(self, url):
        try:
            response = self.session.get(url)
            if response.ok:
                start = response.text.find("<title>") + len("<title>")
                end = response.text.find("</title>")
                return response.text[start:end] if start != -1 and end != -1 else "Title not found"
            return f"Failed to fetch URL: {response.status_code}"
        except Exception as e:
            return f"Error fetching URL: {str(e)}"

    def post_data(self, url, payload):
        try:
            response = self.session.post(url, json=payload)
            return response.json() if response.ok else {"error": response.text}
        except Exception as e:
            return {"exception": str(e)}
