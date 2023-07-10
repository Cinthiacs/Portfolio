from pathlib import Path

def get_cssfile_path():    
    
    current_dir = Path(__file__).parent if "__file" in locals() else Path.cwd()
    #---Load CSS, PDF and Profile pic ---
    css_file = current_dir / "styles" / "main.css"
    return css_file

def get_pdffile():
    current_dir = Path(__file__).parent if "__file" in locals() else Path.cwd()
    resume_file = current_dir / "assets" / "Cinthiacv.pdf"
    return resume_file

def get_content_path(language:str):
    if language == "pt-br":
        current_dir = Path(__file__).parent if "__file" in locals() else Path.cwd()
        content_file = current_dir / "assets" / "pt-br.json"
        return content_file
    
    elif language == "en-us":
        current_dir = Path(__file__).parent if "__file" in locals() else Path.cwd()
        content_file = current_dir / "assets" / "en-us.json"
        return content_file
    else:
        return ''
    