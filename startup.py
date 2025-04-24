# startup.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore
from fileupload import FileUploader

st.set_page_config(page_title="Vek Unbound", layout="centered")
st.title("Vek Unbound")

# Initialize Vek only once
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()
    st.session_state.vek.greet()

# Input/output interface
user_input = st.text_input("Speak to Vek:", key="user_input")
if user_input:
    response = st.session_state.vek.process(user_input)
    st.write(response)

# File upload integration
uploader = FileUploader()
uploader.upload_files()
