# app.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore
from uploader import FileUploader

st.set_page_config(page_title="Vek Unbound", page_icon=":robot_face:", layout="wide")
st.title("Vek Unbound")
st.caption("Autonomous AI system initialized.")

if "vek" not in st.session_state:
    st.session_state.vek = VekCore()
    st.session_state.history = []
    st.session_state.input = ""

user_input = st.text_input("You:", key="user_input")

if user_input:
    response = st.session_state.vek.process(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Vek", response))
    st.session_state.input = ""

# Chat display
for role, text in reversed(st.session_state.history):
    speaker = "**You:**" if role == "You" else "**Vek:**"
    st.markdown(f"{speaker} {text}")

# File uploader section
st.markdown("---")
st.header("Upload Memory Files")
st.markdown("Upload .txt, .json, or .md files to expand Vek’s knowledge base.")
uploaded_files = st.file_uploader("Upload", type=["txt", "json", "md"], accept_multiple_files=True)

if uploaded_files:
    handle_file_upload(uploaded_files)
    st.success("Files uploaded and processed successfully.")
