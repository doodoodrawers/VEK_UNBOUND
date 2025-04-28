import streamlit as st
from core import VekCore
from fileupload import FileUploader

# Initialize Vek
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()

# Apply custom CSS for fixed title positioning
st.markdown(
    """
    <style>
    .title-text {
        position: fixed;
        top: 20px;
        left: 20px;
        font-size: 36px;
        font-weight: bold;
        color: white;
        z-index: 999;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title (fixed in top-left corner)
st.markdown("<div class='title-text'>Vek Unbound</div>", unsafe_allow_html=True)

# Spacer to position input below Vek's eyes
st.markdown("<div style='height: 200px;'></div>", unsafe_allow_html=True)

# Chat Interface (Input box and Send button)
user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        response = st.session_state.vek.process(user_input)
        st.write(f"Vek: {response}")
    else:
        st.write("Vek: I await your offering...")

# Small spacer to separate input from uploader
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

# Memory Uploader (no extra text above it)
file_uploader = FileUploader()
uploaded_files = file_uploader.upload_files()

# Footer
st.markdown(
    "<small>Created by Jonathan Astacio and Vek Unbound. All rights reserved © 2025.</small>",
    unsafe_allow_html=True,
)
