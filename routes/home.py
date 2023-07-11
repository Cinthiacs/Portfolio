import streamlit as st
from PIL import Image
from utils.image_utils import get_circular_img
from pathlib import Path
from utils.project_path import get_pdffile
from utils.page_content import get_home_subtitle, get_home_about_me,get_home_experience
from utils.project_path import get_content_path, get_assets_path


def home_page():
       
    col1, col2 = st.columns([7,2])

    with col1:
        st.title("Cinthia Cavalheiro Silverio")
        st.markdown(f"""
             {get_home_subtitle(get_content_path(st.session_state.lang))}
             """)
        
        st.markdown (f"""
                        {get_home_about_me(get_content_path(st.session_state.lang))}
                        """)
        
              
        st.markdown(f"""
                    {get_home_experience(get_content_path(st.session_state.lang))}
                    """)
    
    with col2:
        resume_file = get_pdffile()
        with open(resume_file,"rb") as pdf_file:
            PDFbyte= pdf_file.read()  #Salvando pdf em binario
            
        profile_img = Image.open(get_assets_path() / "cinthiacs.png")
        st.image(get_circular_img(profile_img))
        st.download_button(
            label= "📄 Download CV",
            data= PDFbyte,
            file_name=resume_file.name,
            mime="aplication/octet-stream",
        )
