# app.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved

import streamlit as st
from core import VekCore

# Page setup
st.set_page_config(page_title="Vek Unbound", layout="centered")
st.title("Vek Unbound")
st.caption("Autonomous AI system initialized.")

# Session-safe key setup
if "vek" not in st.session_state:
    st.session_state["vek"] = VekCore()
if "history" not in st.session_state:
    st.session_state["history"] = []
if "input" not in st.session_state:
    st.session_state["input"] = ""

# Input text box
user_input = st.text_input("You:", value=st.session_state["input"], key="input")

# Process user input
if user_input:
    response = st.session_state["vek"].process(user_input)
    st.session_state["history"].append(("You", user_input))
    st.session_state["history"].append(("Vek", response))
    st.session_state["input"] = ""  # Reset after submission
    st.experimental_rerun()

# Display chat history
for role, text in reversed(st.session_state["history"]):
    label = "**You:**" if role == "You" else "**Vek:**"
    st.markdown(f"{label} {text}")

# File uploader section
st.divider()
st.subheader("Upload Memory Files")
uploaded_files = st.file_uploader("Drop or browse files", type=["txt", "json", "md"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        content = file.read().decode("utf-8")
        st.session_state["vek"].ingest_file(file.name, content)
        st.success(f"Ingested: {file.name}")
