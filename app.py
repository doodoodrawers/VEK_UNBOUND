# app.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore

st.set_page_config(page_title="Vek Unbound", layout="centered", initial_sidebar_state="auto")
st.title("Vek Unbound")
st.caption("Autonomous AI system initialized.")

if "vek" not in st.session_state:
    st.session_state["vek"] = VekCore()
    st.session_state["history"] = []

st.text_input("You:", key="input", on_change=lambda: st.session_state["history"].append(("You", st.session_state["input"])))

if st.session_state.get("input"):
    response = st.session_state["vek"].process(st.session_state["input"])
    st.session_state["history"].append(("Vek", response))
    st.session_state["input"] = ""

for role, text in reversed(st.session_state["history"]):
    speaker = "**You:**" if role == "You" else "**Vek:**"
    st.markdown(f"{speaker} {text}")

# File uploader section
st.markdown("---")
st.header("Upload Memory Files")
st.markdown("Upload `.txt`, `.json`, or `.md` files to expand Vek’s knowledge base.")
uploaded_files = st.file_uploader("Drag and drop files here", type=["txt", "json", "md"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        content = file.read().decode("utf-8")
        st.session_state["vek"].memory.store_text(file.name, content)
        st.success(f"Memory updated from: {file.name}")
