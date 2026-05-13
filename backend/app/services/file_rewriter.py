def rewrite_file(file_path, new_code):

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_code)