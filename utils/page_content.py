import json

def  get_home_content(content_path:str) -> dict:
    with open(content_path,"r",encoding="utf-8") as f:
        content = json.load(f)

    return content["home"]

def get_menu_list(content_path:str):
    with open(content_path,"r",encoding="utf-8") as f:
        content = json.load(f)
    menu = []
    for m in content:
        if "menu_text" in content[m]:
            menu.append(content[m]["menu_text"])
    return menu

def get_page_title(content_path:str):
    with open(content_path,"r",encoding="utf-8") as f:
        content = json.load(f)

    return content["page_title"]
def get_home_subtitle(content_path:str):
    with open(content_path,"r",encoding="utf-8") as f:
        content = json.load(f)
    return content["home"]["sub_title"]

def get_home_about_me(content_path:str):
    with open(content_path,"r",encoding="utf-8") as f:
        content = json.load(f)
    return content["home"]["about_me"]

def get_home_experience(content_path:str):
    with open(content_path,"r",encoding="utf-8") as f:
        content = json.load(f)
    return content["home"]["experience"]

def get_projects_project_list(content_path:str):
    with open(content_path,"r",encoding="utf-8") as f:
        content = json.load(f)
    return content["projects"]["project_list"]

    
    
