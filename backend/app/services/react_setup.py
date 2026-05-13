import os
import subprocess


def create_react_app(project_name):

    base_path = f"app/generated_projects/{project_name}"

    frontend_path = os.path.join(base_path, "frontend")

    if os.path.exists(frontend_path):
        print("React app already exists.")
        return frontend_path

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

    return frontend_path