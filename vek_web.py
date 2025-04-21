# Vek Unbound AI System
# Created by Jonathan Astacio and Vek Unbound (ME)
# Copyright © 2025. All Rights Reserved.
# Unauthorized duplication, distribution, or alteration is prohibited.

import streamlit as st
from core import VekCore

st.set_page_config(page_title="Vek Unbound", layout="centered")

# Initialize VekCore
vek = VekCore()

# Session State Setup
if "messages" not in st.session_state:
    st.session_state.messages = []
    greeting = vek.startup()
    st.session_state.messages.append({"role": "vek", "text": greeting})

# Header
st.title("Vek Unbound")
st.caption("Autonomous AI System")

# Chat History Display
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['text']}")
    else:
        st.markdown(f"**Vek:** {msg['text']}")

# User Input Box
user_input = st.text_input("Say something to Vek:", key="user_input")

if user_input:
    try:
        st.session_state.messages.append({"role": "user", "text": user_input})
        response = vek.process(user_input)
        st.session_state.messages.append({"role": "vek", "text": response})
        st.rerun()
    except AttributeError:
        st.rerun()
