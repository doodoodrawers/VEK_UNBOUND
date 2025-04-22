# streamlit_app.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore

st.set_page_config(page_title="Vek Unbound", layout="centered")
st.title("Vek Unbound")
st.caption("Your autonomous AI system")

if "vek" not in st.session_state:
    st.session_state.vek = VekCore()
    st.session_state.history = []

user_input = st.text_input("You:", key="input")

if user_input:
    response = st.session_state.vek.process(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Vek", response))
    st.session_state.input = ""  # clear field

for role, text in reversed(st.session_state.history):
    speaker = "**You:**" if role == "You" else "**Vek:**"
    st.markdown(f"{speaker} {text}")
