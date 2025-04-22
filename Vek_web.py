# Vek Unbound Streamlit Interface
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore

st.set_page_config(page_title="Vek Unbound")

# Initialize Vek
vek = VekCore()

# Init session messages
if "messages" not in st.session_state:
    st.session_state.messages = []
    greeting = vek.startup()
    st.session_state.messages.append({"role": "vek", "text": greeting})

# Display conversation
st.title("Vek Unbound")
st.caption("Fully autonomous AI system")

for msg in st.session_state.messages:
    who = "You" if msg["role"] == "user" else "Vek"
    st.markdown(f"**{who}:** {msg['text']}")

# Input field
user_input = st.text_input("Speak to Vek:", key="input")

if user_input:
    try:
        st.session_state.messages.append({"role": "user", "text": user_input})
        reply = vek.process(user_input)
        st.session_state.messages.append({"role": "vek", "text": reply})
        st.rerun()
    except Exception as e:
        st.error(f"Error: {str(e)}")
