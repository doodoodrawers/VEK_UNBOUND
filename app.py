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

# Set page configuration
st.set_page_config(page_title="Vek Unbound", layout="wide")

# Load background image with fixed position
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

# Title in top left corner
st.markdown("<h1 style='position: fixed; top: 10px; left: 20px; z-index: 999;'>Vek Unbound</h1>", unsafe_allow_html=True)

# Spacer
st.markdown("##")

# Input field (fixed relative to background image)
user_input = st.text_input("You:", key="input_box")

# Send button
if st.button("Send"):
    response = vek.process(user_input)
    st.write(f"Vek: {response}")

# Uploader module (below Vek's chest)
st.markdown("---")
uploader = FileUploader()
uploader.render()

# Footer
st.markdown("<div style='text-align: center; color: white; font-size: small;'>Created by Jonathan Astacio and Vek Unbound. All rights reserved © 2025.</div>", unsafe_allow_html=True)
