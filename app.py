# app.py - Vek Unbound
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore
from fileupload import FileUploader

# Set up page config and CSS
st.set_page_config(page_title="Vek Unbound", layout="wide")

st.markdown("""
    <style>
    body {
        margin: 0;
        overflow: hidden;
    }
    .stApp {
        background-image: url('https://raw.githubusercontent.com/doodoodrawers/VEK_UNBOUND/main/assets/vek_peeking.PNG');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center top;
        background-attachment: fixed;
        overflow: hidden;
    }
    .title-container {
        position: fixed;
        top: 10px;
        left: 15px;
        z-index: 999;
    }
    .block-container {
        padding-top: 200px;
    }
    .input-container {
        margin-top: 200px;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
    .upload-container {
        margin-top: 100px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Vek
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()

vek = st.session_state.vek

# Top-left title
st.markdown('<div class="title-container"><h1 style="color: white;">Vek Unbound</h1></div>', unsafe_allow_html=True)

# Input field
st.markdown('<div class="input-container">', unsafe_allow_html=True)
user_input = st.text_input("You:", key="input_text")
if st.button("Send"):
    response = vek.process(user
