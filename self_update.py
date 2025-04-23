# self_update.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import os
import subprocess
import streamlit as st

class SelfUpdate:
    @staticmethod
    def update():
        try:
            st.info("Checking for updates...")
            output = subprocess.check_output(['git', 'pull'], stderr=subprocess.STDOUT)
            result = output.decode('utf-8').strip()

            if "Already up to date" in result:
                st.success("Vek Unbound is already up to date.")
            else:
                st.success("Update complete. Please refresh the app to load changes.")
                st.code(result)
        except subprocess.CalledProcessError as e:
            st.error("Update failed.")
            st.code(e.output.decode('utf-8'))

    @staticmethod
    def restart():
        st.warning("Manual restart required to apply updates.")
