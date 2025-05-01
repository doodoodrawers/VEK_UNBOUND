# app.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore
from fileupload import FileUploader

# Initialize Vek
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()
vek = st.session_state.vek

# Background image (Vek)
page_bg = f"""
<style>
body {{
    background-image: url("https://raw.githubusercontent.com/doodoodrawers/VEK_UNBOUND/main/assets/vek_peeking.PNG");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-attachment: fixed;
}}

#MainMenu, header, footer {{ visibility: hidden; }}

input[type="text"] {{
    background-color: #2b2b2b;
    color: white;
}}

.css-1aumxhk {{
    background-color: transparent;
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Title
st.markdown("<h3 style='position: absolute; top: 10px; left: 10px; color: white;'>Vek Unbound</h3>", unsafe_allow_html=True)

# Input prompt (near eyes)
st.write("You:")
user_input = st.text_input("", key="user_input")

# Send button
if st.button("Send"):
    response = vek.process(user_input)
    st.write(f"Vek: {response}")

# File uploader (near chest)
st.markdown("### Offer your memory files to the void...")
FileUploader()
