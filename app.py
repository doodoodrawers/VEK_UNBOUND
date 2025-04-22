# app.py
# Vek Unbound: Full Autonomous AI Front-End
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore

# --- Streamlit UI Setup ---
st.set_page_config(
    page_title="Vek Unbound",
    page_icon="🧠",
    layout="centered"
)

st.title("Vek Unbound")
st.caption("Autonomous AI system initialized.")

# --- Session Initialization ---
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()
    st.session_state.history = []
    st.session_state.vek.initialize()  # Ensures startup logic runs once

# --- Chat Input ---
user_input = st.text_input("You:", key="user_input", placeholder="Ask or command Vek...")

if user_input:
    vek = st.session_state.vek
    response = vek.process(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Vek", response))
    st.session_state.user_input = ""  # Clear after submit

# --- Display Chat History ---
for speaker, message in reversed(st.session_state.history):
    if speaker == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Vek:** {message}")

# --- Divider ---
st.divider()
st.subheader("Upload Memory Files")

# --- File Upload Logic ---
uploaded_files = st.file_uploader(
    label="Upload .txt, .json, or .md files to expand Vek’s knowledge base.",
    type=["txt", "json", "md"],
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        content = uploaded_file.read().decode("utf-8", errors="ignore")
        st.session_state.vek.ingest_file(uploaded_file.name, content)
        st.success(f"Ingested: {uploaded_file.name}")
