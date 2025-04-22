# streamlit_app.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore
from uploader import handle_file_upload

st.set_page_config(page_title="Vek Unbound", layout="centered", initial_sidebar_state="auto")
st.title("Vek Unbound")
st.caption("Autonomous AI system initialized.")

# Initialize VekCore in session state
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()
    st.session_state.history = []

# Capture user input
user_input = st.text_input("You:", key="user_input")

# Process user input
if user_input:
    response = st.session_state.vek.process(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Vek", response))
    st.session_state.user_input = ""

# Display conversation history
for role, text in reversed(st.session_state.history):
    speaker = "**You:**" if role == "You" else "**Vek:**"
    st.markdown(f"{speaker} {text}")

# File uploader
st.markdown("---")
st.subheader("Upload Memory Files")
st.markdown("Upload .txt, .json, or .md files to expand Vek’s knowledge base.")
uploaded_files = st.file_uploader("Choose files", type=["txt", "json", "md"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        handle_file_upload(uploaded_file, st.session_state.vek)
