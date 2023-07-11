import streamlit as st
from PIL import Image
from utils.image_utils import get_circular_img
from utils.project_path import get_content_path, get_assets_path
from utils.page_content import get_projects_project_list

def projects_page():
    proj_list = get_projects_project_list(get_content_path(st.session_state.lang))  

    for l in proj_list:
        st.title(l["title"])

        col1,col2 = st.columns([2,1])
        with col1:
            st.write(l["description"])


        with col2:
            if l["picture"] != "":
                st.image(Image.open(get_assets_path() / l["picture"]))
                
            elif l["youtube"] != "":
                st.video(l["youtube"])

            st.markdown(f"""{l['repository']}""")

