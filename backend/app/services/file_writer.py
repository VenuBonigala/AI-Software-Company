import os
import re


def sanitize_filename(filename):

    filename = filename.strip()

    filename = re.sub(r"[*:\"<>?|]", "", filename)

    filename = filename.replace(" ", "")

    return filename


def save_react_component(project_name, filename, code):

    filename = sanitize_filename(filename)

    base_path = f"app/generated_projects/{project_name}/frontend/src/components"

    os.makedirs(base_path, exist_ok=True)

    file_path = os.path.join(base_path, filename)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(code)

    return file_path

def read_file(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
def rewrite_file(file_path, new_code):

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_code)