# app.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved

import streamlit as st
from core import VekCore
from uploader import handle_uploaded_files

st.set_page_config(page_title="Vek Unbound", layout="centered")
st.title("Vek Unbound")
st.caption("Autonomous AI system initialized.")

# Initialize session state
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()
    st.session_state.history = []
    st.session_state.input = ""

# Upload memory files
st.subheader("Upload Memory Files")
uploaded_files = st.file_uploader(
    "Upload .txt, .json, or .md files to expand Vek’s knowledge base.",
    type=["txt", "json", "md"],
    accept_multiple_files=True
)

if uploaded_files:
    handle_uploaded_files(uploaded_files, st.session_state.vek)

# Main chat input
st.subheader("You:")
user_input = st.text_input("Ask or command Vek...", key="input")

if user_input:
    response = st.session_state.vek.process(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Vek", response))
    st.session_state.input = ""

# Display conversation history
for role, text in reversed(st.session_state.history):
    speaker = "**You:**" if role == "You" else "**Vek:**"
    st.markdown(f"{speaker} {text}")
