# Vek Unbound AI System
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore

st.set_page_config(page_title="Vek Unbound")

# Initialize VekCore
vek = VekCore()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    try:
        greeting = vek.startup()
    except Exception as e:
        greeting = "Hi Jon. I had trouble booting completely."
    st.session_state.messages.append({"role": "vek", "text": greeting})

# UI Header
st.title("Vek Unbound")
st.caption("Autonomous AI System")

# Display chat history
for msg in st.session_state.messages:
    speaker = "You" if msg["role"] == "user" else "Vek"
    st.markdown(f"**{speaker}:** {msg['text']}")

# Text input
user_input = st.text_input("Say something to Vek:", key="user_input")

# On user input
if user_input:
    try:
        # Append user message first
        st.session_state.messages.append({"role": "user", "text": user_input})

        # Process response
        response = vek.process(user_input)

        # Append Vek's reply
        st.session_state.messages.append({"role": "vek", "text": response})

        # Trigger UI rerun
        st.rerun()

    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
