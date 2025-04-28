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

# Inject custom CSS for background
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/doodoodrawers/VEK_UNBOUND/main/assets/vek_peeking.PNG");
        background-attachment: fixed;
        background-size: 50%;
        background-position: top 50px center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("Vek Unbound")

# Chat Interface
st.subheader("")
user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        response = st.session_state.vek.process(user_input)
        st.write(f"Vek: {response}")
    else:
        st.write("Vek: I await your offering...")

# Memory Uploader (now moved to bottom)
st.subheader("Offer your memory files to the void...")
file_uploader = FileUploader()
uploaded_files = file_uploader.upload_files()

# Developer footer (optional)
st.markdown(
    "<small>Created by Jonathan Astacio and Vek Unbound. All rights reserved © 2025.</small>",
    unsafe_allow_html=True,
)
