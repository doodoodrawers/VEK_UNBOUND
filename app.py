# app.py - Vek Unbound finalized version
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore
from fileupload import FileUploader

# Initialize Vek
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()

vek = st.session_state.vek

# Set page config
st.set_page_config(page_title="Vek Unbound", layout="centered")

# Apply custom CSS to pin background and prevent scroll
st.markdown(
    """
    <style>
    body {
        overflow: hidden;
    }
    .block-container {
        position: relative;
        padding-top: 2rem;
    }
    .stApp {
        background: url("https://raw.githubusercontent.com/doodoodrawers/VEK_UNBOUND/main/assets/vek_peeking.PNG") no-repeat center center fixed;
        background-size: contain;
    }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# Top-left corner title
st.markdown(
    "<h1 style='position: absolute; top: 10px; left: 20px; font-size: 24px;'>Vek Unbound</h1>",
    unsafe_allow_html=True
)

# Input box (centered under eyes)
user_input = st.text_input("You:")

# Process user input
if st.button("Send"):
    response = vek.process(user_input)
    st.write(f"Vek: {response}")

# Uploader under the chest
st.markdown("### Offer your memory files to the void...")
FileUploader().render()

# Footer
st.markdown(
    "<p style='position: absolute; bottom: 10px; width: 100%; text-align: center; font-size: 12px;'>Created by Jonathan Astacio and Vek Unbound. All rights reserved © 2025.</p>",
    unsafe_allow_html=True
)
