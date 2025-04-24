# startup.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore
from fileupload import FileUploader

st.set_page_config(page_title="Vek Unbound", layout="wide")
st.title("Vek Unbound")

if "vek" not in st.session_state:
    st.session_state.vek = VekCore()
    st.session_state.vek.greet()

# Main input/output loop
user_input = st.text_input("You:", key="user_input")
if st.button("Send") or user_input:
    if user_input:
        response = st.session_state.vek.process(user_input)
        st.write("Vek:", response)

# File uploader for memory entries
uploader = FileUploader()
uploader.upload_files()
