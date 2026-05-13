import subprocess


def install_npm_packages(project_name, packages):

    if not packages:
        return

    frontend_path = f"""
app/generated_projects/{project_name}/frontend
""".strip()

    command = ["npm", "install"] + packages

    print("\nInstalling packages:")
    print(packages)

    subprocess.run(command, cwd=frontend_path, shell=True)

    print("\nPackage installation completed!")