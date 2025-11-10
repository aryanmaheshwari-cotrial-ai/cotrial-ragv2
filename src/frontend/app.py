"""Main entry point - redirects to login."""

import streamlit as st

st.set_page_config(
    page_title="CoTrial RAG",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Redirect to login if not authenticated, otherwise to trials
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.switch_page("pages/login.py")
else:
    st.switch_page("pages/trials.py")
