# app.py - Final Streamlit UI for Vek Unbound
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
st.set_page_config(page_title="Vek Unbound", layout="wide")

# Background setup
page_bg_img = f"""
<style>
.stApp {{
    background-image: url("https://raw.githubusercontent.com/doodoodrawers/VEK_UNBOUND/main/assets/vek_peeking.PNG");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center top;
    background-attachment: fixed;
    background-color: #0e0f13;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Input section
st.markdown("**You:**")
user_input = st.text_input("", key="input")

if st.button("Send"):
    response = vek.process(user_input)
    st.markdown(f"**Vek:** {response}")

# Upload section
st.markdown("#### Offer your memory files to the void...")
FileUploader().render()
