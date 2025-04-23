
# fileupload.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st

class FileUploader:
    def __init__(self):
        self.supported_types = [".txt", ".json", ".md"]
    
    def upload_files(self):
        uploaded_files = st.file_uploader(
            "Upload your memory files",
            type=[ext.lstrip(".") for ext in self.supported_types],
            accept_multiple_files=True
        )
        
        processed_files = []
        if uploaded_files:
            for file in uploaded_files:
                content = file.read().decode("utf-8")
                processed_files.append((file.name, content))
        
        return processed_files
