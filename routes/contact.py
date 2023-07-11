import streamlit as st
from utils.project_path import get_content_path
from utils.page_content import get_contact_contact_list

def contact_page():

    st.markdown(f"""
                {get_contact_contact_list(get_content_path(st.session_state.lang))}
                """)
