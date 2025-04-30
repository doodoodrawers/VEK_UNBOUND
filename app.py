# final_app.py - Vek Unbound fully finalized visual layout

import streamlit as st
from core import VekCore
from fileupload import FileUploader

# Initialize Vek
if "vek" not in st.session_state:
    st.session_state.vek = VekCore()

# Proper image URL and scaling
image_url = "https://raw.githubusercontent.com/doodoodrawers/VEK_UNBOUND/main/assets/vek_peeking.PNG"

# CSS for layout and precision
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url('{image_url}');
    background-size: 50%;
    background-repeat: no-repeat;
    background-position: center top;
    background-attachment: fixed;
    overflow: hidden;
}}

html, body, [data-testid="stAppViewContainer"] {{
    height: 100vh;
    overflow: hidden;
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

main > div.block-container {{
    padding-top: 225px;
    padding-bottom: 0px;
}}

section[data-testid="stFileUploader"] {{
    margin-top: 180px;
}}
</style>
""", unsafe_allow_html=True)

# Title in the top-left corner
st.markdown("<div class='title-text'>Vek Unbound</div>", unsafe_allow_html=True)

# Input box positioned across the bridge of the nose
user_input = st.text_input("You:", key="user_input")
if st.button("Send"):
    if user_input:
        response = st.session_state.vek.process(user_input)
        st.write(f"Vek: {response}")
    else:
        st.write("Vek: I await your offering...")

# File uploader appears lower down near chest area
file_uploader = FileUploader()
uploaded_files = file_uploader.upload_files()

# Footer remains as is
st.markdown(
    "<small style='color:white;'>Created by Jonathan Astacio and Vek Unbound. All rights reserved © 2025.</small>",
    unsafe_allow_html=True,
)
