# uploader.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
import os

class FileUploader:
    def __init__(self, upload_dir="uploads"):
        self.upload_dir = upload_dir
        os.makedirs(self.upload_dir, exist_ok=True)

    def upload_files(self):
        uploaded_files = st.file_uploader(
            "Upload Memory Files",
            type=["txt", "json", "md"],
            accept_multiple_files=True
        )

        if uploaded_files:
            for uploaded_file in uploaded_files:
                file_path = os.path.join(self.upload_dir, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.success(f"Uploaded: {uploaded_file.name}")

            st.info("Memory files uploaded. You can now trigger processing.")
        return uploaded_files
    def handle_file_upload(uploaded_files):
    uploader = FileUploader()
    uploader.upload_files()
