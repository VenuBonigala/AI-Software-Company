import os
import re

from app.services.project_paths import get_component_path


def sanitize_filename(filename):

    filename = filename.strip()

    filename = re.sub(r"[*:\"<>?|]", "", filename)

    filename = filename.replace(" ", "")

    return filename


def save_react_component(project_name, filename, code):

    filename = sanitize_filename(filename)

    file_path = get_component_path(project_name, filename)

    os.makedirs(file_path.parent, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(code)

    return str(file_path)

def read_file(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
def rewrite_file(file_path, new_code):

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_code)
