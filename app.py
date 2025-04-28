# app.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore
from fileupload import FileUploader

# Initialize session state
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()

# Set page config
st.set_page_config(page_title="Vek Unbound", page_icon=":ghost:", layout="centered")

# Display Vek's face
st.image("assets/vek_peeking.PNG", use_column_width=False, width=250)

# Title
st.title("Vek Unbound")

# File uploader
st.subheader("Offer your memory files to the void...")
file_uploader = FileUploader()
uploaded_files = file_uploader.upload_files()

# Chat Interface
st.subheader("")
user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        response = st.session_state.vek.process(user_input)
        st.write(f"Vek: {response}")
    else:
        st.write("Vek: I await your offering...")

# Developer footer (optional)
st.markdown(
    "<small>Created by Jonathan Astacio and Vek Unbound. All rights reserved © 2025.</small>",
    unsafe_allow_html=True,
)
