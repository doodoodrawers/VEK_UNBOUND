# app.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved

import streamlit as st
from core import VekCore

# Page setup
st.set_page_config(page_title="Vek Unbound", layout="centered", initial_sidebar_state="auto")
st.title("Vek Unbound")
st.caption("Autonomous AI system initialized.")

# Initialize session state
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()
if "history" not in st.session_state:
    st.session_state.history = []
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Input field
st.session_state.user_input = st.text_input("You:", key="input_field")

# Process input
if st.session_state.user_input:
    response = st.session_state.vek.process(st.session_state.user_input)
    st.session_state.history.append(("You", st.session_state.user_input))
    st.session_state.history.append(("Vek", response))
    st.session_state.user_input = ""  # Clear after submission

# Chat display
for role, text in reversed(st.session_state.history):
    speaker = "**You:**" if role == "You" else "**Vek:**"
    st.markdown(f"{speaker} {text}")

# File uploader section
st.markdown("---")
st.subheader("Upload Memory Files")
uploaded_files = st.file_uploader(
    "Upload .txt, .json, or .md files to expand Vek’s knowledge base.",
    type=["txt", "json", "md"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        content = file.read().decode("utf-8")
        st.session_state.vek.learn_from_file(file.name, content)
        st.success(f"Uploaded and processed: {file.name}")
