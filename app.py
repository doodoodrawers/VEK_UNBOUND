# app.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore
from fileupload import FileUploader  # renamed module to avoid cache issue

st.set_page_config(page_title="Vek Unbound")
st.title("Vek Unbound")
st.caption("Autonomous AI system initialized.")

# Initialize session state
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()
    st.session_state.history = []
    st.session_state.input = ""

# Text input from user
user_input = st.text_input("You:", key="user_input")

# Process input
if user_input:
    response = st.session_state.vek.process(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Vek", response))
    st.session_state.input = ""

# Display chat
for role, text in reversed(st.session_state.history):
    speaker = "**You:**" if role == "You" else "**Vek:**"
    st.markdown(f"{speaker} {text}")

# Upload files
st.markdown("---")
st.header("Upload Memory Files")
st.markdown("Upload `.txt`, `.json`, or `.md` files to expand Vek’s knowledge base.")
uploader = FileUploader()
uploaded_files = uploader.upload_files()

if uploaded_files:
    st.success("Files uploaded and processed successfully.")
