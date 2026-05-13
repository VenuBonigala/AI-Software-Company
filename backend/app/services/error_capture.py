import subprocess


def run_react_app(project_name):

    frontend_path = f"""
app/generated_projects/{project_name}/frontend
""".strip()

    command = ["npm", "run", "build"]

    result = subprocess.run(
        command,
        cwd=frontend_path,
        capture_output=True,
        text=True,
        shell=True
    )

    return {
        "success": result.returncode == 0,
        "stdout": result.stdout,
        "stderr": result.stderr
    }