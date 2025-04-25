# startup.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore
from fileupload import FileUploader

st.set_page_config(page_title="Vek Unbound", layout="wide")
st.title("Vek Unbound")

# Initialize or retrieve Vek instance
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()

# Show uploader
uploader = FileUploader()
uploaded_files = uploader.upload_files()

# Input and response area
user_input = st.text_input("You:", key="input_field")

if st.button("Send") and user_input.strip():
    response = st.session_state.vek.process(user_input)
    st.write(f"Vek: {response}")
