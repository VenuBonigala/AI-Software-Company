import os
import subprocess

from app.services.project_paths import get_frontend_root, get_project_root


def create_react_app(project_name):

    base_path = get_project_root(project_name)
    frontend_path = get_frontend_root(project_name)

    if os.path.exists(frontend_path):
        print("React app already exists.")
        return str(frontend_path)

    command = [
        "npm",
        "create",
        "vite@latest",
        "frontend",
        "--",
        "--template",
        "react"
    ]

    subprocess.run(command, cwd=base_path, shell=True)

    print("React app created successfully!")

    return str(frontend_path)
