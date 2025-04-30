# fileupload.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
import json

class FileUploader:
    def __init__(self):
        pass

    def upload_files(self):
        uploaded_file = st.file_uploader("Offer your memory files to the void...", type=["txt", "json", "md"])
        if uploaded_file is not None:
            try:
                content = uploaded_file.read().decode("utf-8")

                # If it's JSON, try loading and injecting to memory
                if uploaded_file.name.endswith(".json"):
                    parsed = json.loads(content)
                    if isinstance(parsed, list):
                        st.session_state.vek.memory.load_entries(parsed)
                        st.success("Vek absorbed your memory file.")
                    else:
                        st.warning("JSON must be a list of memory entries.")
                else:
                    st.session_state.vek.memory.log_entry(content)
                    st.success("Raw memory logged successfully.")
            except Exception as e:
                st.error(f"Failed to process file: {e}")
