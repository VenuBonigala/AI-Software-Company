import os
import subprocess

from app.services.project_paths import get_frontend_root


def install_npm_packages(project_name, packages):

    if not packages:
        return

    frontend_path = get_frontend_root(project_name)

    npm_command = "npm.cmd" if os.name == "nt" else "npm"
    command = [npm_command, "install"] + packages

    print("\nInstalling packages:")
    print(packages)

    subprocess.run(command, cwd=frontend_path, shell=False)

    print("\nPackage installation completed!")
