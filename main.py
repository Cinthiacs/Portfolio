import streamlit as st
from streamlit_option_menu import option_menu
from routes.home import home_page
from routes.projects import projects_page
from routes.contact import contact_page
from utils.project_path import get_cssfile_path, get_content_path
from utils.page_content import get_menu_list, get_page_title

def main():
    if"lang" not in st.session_state:
        st.session_state.lang = "pt-br"
    
    st.set_page_config(
      page_title = get_page_title(get_content_path(st.session_state.lang)),
      page_icon="📃"
    )

    css_file = get_cssfile_path()
    
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), 
                    unsafe_allow_html=True)

    menu = get_menu_list(get_content_path(st.session_state.lang))
    selected = option_menu(
        menu_title=None,
        options= menu,
        icons=["house-heart","code-slash","envelope-check-fill"],
        menu_icon= "cast",
        orientation="horizontal",
    )

    if selected == menu[0]:
        home_page()

    if selected == menu[1]:
        projects_page()
    
    if selected == menu[2]:
        contact_page()

if __name__ == "__main__":
    main()