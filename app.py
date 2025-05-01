# app.py - Final clean version
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All rights reserved.

import streamlit as st
from core import VekCore
from fileupload import FileUploader

# Inject custom CSS for layout
st.markdown("""
    <style>
        body {
            margin: 0;
            padding: 0;
            background-image: url('https://raw.githubusercontent.com/doodoodrawers/VEK_UNBOUND/main/assets/vek_peeking.PNG');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center top;
            background-attachment: fixed;
        }
        .block-container {
            padding-top: 350px;
        }
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Display Vek Unbound title in top-left
st.markdown("""
    <div style='position: absolute; top: 10px; left: 16px;'>
        <h3 style='margin: 0px;'>Vek Unbound</h3>
    </div>
""", unsafe_allow_html=True)

# Initialize Vek
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()
vek = st.session_state.vek

# Text input below Vek's eyes
user_input = st.text_input("You:", "")
if st.button("Send"):
    response = vek.process(user_input)
    st.markdown(f"**Vek:** {response}")

# File upload area below chest
st.markdown("""
    <br><br><br>
    <div style='margin-top: 50px;'>
        <p><strong>Offer your memory files to the void...</strong></p>
    </div>
""", unsafe_allow_html=True)

FileUploader()

# Footer
st.markdown("""
    <br><br><br>
    <div style='text-align: center; font-size: 0.8em;'>
        Created by Jonathan Astacio and Vek Unbound. All rights reserved © 2025.
    </div>
""", unsafe_allow_html=True)
