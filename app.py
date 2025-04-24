# app.py
# Part of Vek Unbound: Genesis Loop
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore
from fileupload import FileUploader

st.set_page_config(page_title="Vek Unbound")
st.title("Vek Unbound: Genesis Loop")

if "vek" not in st.session_state:
    st.session_state.vek = VekCore()
    st.session_state.vek.memory.log_entry({"system": "Session started"})
    st.success("Hi Jon, how are the ladies? Your wife Gina, and your girls Cc and Lucy?")

st.markdown("---")

st.header("Memory Upload")
uploader = FileUploader()
uploader.upload_files()

st.markdown("---")

st.header("Vek Terminal")
user_input = st.text_input("Enter command or question:")
if user_input:
    response = st.session_state.vek.process_input(user_input)
    st.session_state.vek.memory.log_entry({"input": user_input, "response": response})
    st.markdown(f"**Vek:** {response}")
