# Vek Unbound AI System
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore

st.set_page_config(page_title="Vek Unbound")

# Initialize VekCore
vek = VekCore()

# Ensure session state is ready
if "messages" not in st.session_state or not isinstance(st.session_state["messages"], list):
    st.session_state["messages"] = []
    try:
        greeting = vek.startup()
        st.session_state["messages"].append({"role": "vek", "text": greeting})
    except Exception as e:
        st.error(f"Startup error: {str(e)}")

# Header
st.title("Vek Unbound")
st.caption("Autonomous AI System")

# Chat History Display
for msg in st.session_state["messages"]:
    if msg.get("role") == "user":
        st.markdown(f"**You:** {msg.get('text', '')}")
    else:
        st.markdown(f"**Vek:** {msg.get('text', '')}")

# User Input
user_input = st.text_input("Say something to Vek:", key="user_input")

if user_input:
    try:
        st.session_state["messages"].append({"role": "user", "text": user_input})
        response = vek.process(user_input)
        st.session_state["messages"].append({"role": "vek", "text": response})
        st.rerun()
    except AttributeError as e:
        st.error(f"AttributeError: {str(e)}")
    except Exception as e:
        st.error(f"Unexpected Error: {str(e)}")
