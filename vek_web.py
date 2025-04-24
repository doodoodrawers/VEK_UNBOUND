# vek_web.py
# Part of Vek Unbound: Genesis Loop
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import streamlit as st
from core import VekCore
from fileupload import FileUploader

if 'vek' not in st.session_state:
    st.session_state.vek = VekCore()
    st.session_state.greeted = False

vek = st.session_state.vek

st.set_page_config(page_title="Vek Unbound")
st.title("Vek Unbound")

if not st.session_state.greeted:
    st.success("Hi Jon. How are the ladies? Your wife Gina, and your girls Cc and Lucy?")
    st.session_state.greeted = True

user_input = st.text_input("Talk to Vek")

if user_input:
    response = vek.process_input(user_input)
    st.write(response)
    vek.memory.log_entry({"type": "interaction", "input": user_input, "response": response})

uploader = FileUploader()
uploader.upload_files()

st.write("\n---\n")
st.subheader("Recent Memory")
recent = vek.memory.get_recent()
for entry in recent:
    st.json(entry)
