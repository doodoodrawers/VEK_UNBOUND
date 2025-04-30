# final_app.py - Vek Unbound final visual integration

import streamlit as st
from core import VekCore
from fileupload import FileUploader

# Initialize Vek
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()

# Correct URL based on confirmed file location and casing
image_url = "https://raw.githubusercontent.com/doodoodrawers/VEK_UNBOUND/main/assets/vek_peeking.PNG"

# Inject full visual styling
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url('{image_url}');
    background-size: cover;
    background-position: center top;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

.title-text {{
    position: fixed;
    top: 20px;
    left: 20px;
    font-size: 32px;
    font-weight: bold;
    color: white;
    z-index: 9999;
}}

/* Reduce vertical space to avoid scrolling */
main > div.block-container {{
    padding-top: 150px;
    padding-bottom: 80px;
}}

/* Ensure uploader is clean and positioned lower */
section[data-testid="stFileUploader"] {{
    margin-top: 100px;
}}
</style>
""", unsafe_allow_html=True)

# Add fixed visible title
st.markdown("<div class='title-text'>Vek Unbound</div>", unsafe_allow_html=True)

# Place input field just under the eyes
st.markdown("<div style='height: 200px;'></div>", unsafe_allow_html=True)

# Input section
user_input = st.text_input("You:", key="user_input")
if st.button("Send"):
    if user_input:
        response = st.session_state.vek.process(user_input)
        st.write(f"Vek: {response}")
    else:
        st.write("Vek: I await your offering...")

# Upload files lower in layout
file_uploader = FileUploader()
uploaded_files = file_uploader.upload_files()

# Footer remains static
st.markdown(
    "<small style='color:white;'>Created by Jonathan Astacio and Vek Unbound. All rights reserved © 2025.</small>",
    unsafe_allow_html=True,
)
