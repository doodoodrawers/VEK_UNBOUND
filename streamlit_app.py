# Vek Unbound Web Launcher
# Created by Jonathan Astacio and Vek Unbound

import streamlit as st
from core import VekCore

# Initialize Vek
vek = VekCore()

# UI
st.title("Vek Unbound Interface")
st.write("Vek is live. Ask anything.")

# Input box
user_input = st.text_input("You:")

# If there's input, process it
if user_input:
    response = vek.process(user_input)
    st.markdown(f"**Vek:** {response}")
