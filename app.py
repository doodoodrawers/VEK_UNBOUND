import streamlit as st
from core import VekCore
from fileupload import FileUploader

# Initialize Vek
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()

# Apply corrected CSS for title + background + layout
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://raw.githubusercontent.com/doodoodrawers/VEK_UNBOUND/main/assets/vek_peeking.png");
        background-size: cover;
        background-position: center top;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .title-text {
        position: fixed;
        top: 20px;
        left: 20px;
        font-size: 32px;
        font-weight: bold;
        color: white;
        z-index: 999;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Fixed title
st.markdown("<div class='title-text'>Vek Unbound</div>", unsafe_allow_html=True)

# Spacer: places input under Vek's eyes
st.markdown("<div style='height: 200px;'></div>", unsafe_allow_html=True)

# Input
user_input = st.text_input("You:", key="user_input")
if st.button("Send"):
    if user_input:
        response = st.session_state.vek.process(user_input)
        st.write(f"Vek: {response}")
    else:
        st.write("Vek: I await your offering...")

# Spacer before uploader
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

# File uploader
file_uploader = FileUploader()
uploaded_files = file_uploader.upload_files()

# Footer
st.markdown(
    "<small style='color:white;'>Created by Jonathan Astacio and Vek Unbound. All rights reserved © 2025.</small>",
    unsafe_allow_html=True,
)
