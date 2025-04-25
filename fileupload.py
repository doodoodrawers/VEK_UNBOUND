# fileupload.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
import json
import os

class FileUploader:
    def __init__(self):
        self.allowed_extensions = {'.txt', '.json', '.md'}

    def upload_files(self):
        uploaded_files = st.file_uploader("Upload your memory files", type=["txt", "json", "md"], accept_multiple_files=True)
        memory_entries = []

        if uploaded_files:
            for uploaded_file in uploaded_files:
                filename = uploaded_file.name
                extension = os.path.splitext(filename)[1]

                if extension in self.allowed_extensions:
                    content = uploaded_file.read().decode("utf-8")
                    parsed_entries = self.parse_memory_file(content, extension)
                    memory_entries.extend(parsed_entries)

            # Store into Vek's memory
            if "vek" in st.session_state and hasattr(st.session_state.vek, "memory"):
                for entry in memory_entries:
                    st.session_state.vek.memory.log_entry(entry)

        return uploaded_files

    def parse_memory_file(self, content, extension):
        memory_entries = []

        if extension == ".json":
            try:
                data = json.loads(content)
                if isinstance(data, list):
                    memory_entries.extend(data)
                elif isinstance(data, dict):
                    memory_entries.append(data)
            except json.JSONDecodeError:
                memory_entries.append({"error": "Invalid JSON format"})

        else:  # .txt or .md
            for line in content.splitlines():
                cleaned = line.strip()
                if cleaned:
                    memory_entries.append({"type": "text", "content": cleaned})

        return memory_entries
