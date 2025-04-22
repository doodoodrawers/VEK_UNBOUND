# Vek Unbound Uploader
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
import json
from memory import Memory

def upload_interface(memory: Memory):
    st.subheader("Upload Knowledge or Identity Files")

    uploaded_file = st.file_uploader("Drop a .json or .txt file to extend memory", type=["json", "txt"])

    if uploaded_file:
        try:
            if uploaded_file.type == "application/json":
                uploaded_data = json.load(uploaded_file)
                memory.data["identity"].update(uploaded_data)
                memory.save()
                st.success("Memory successfully updated from uploaded file.")

            elif uploaded_file.type == "text/plain":
                content = uploaded_file.read().decode("utf-8")
                memory.log_interaction("FILE_UPLOAD", content)
                st.success("Text file logged to memory.")

            else:
                st.warning("Unsupported file format.")
        except Exception as e:
            st.error(f"Upload failed: {str(e)}")
