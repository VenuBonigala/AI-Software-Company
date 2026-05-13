from app.services.error_capture import run_react_app
from app.services.file_reader import read_file
from app.services.file_rewriter import rewrite_file
from app.services.project_paths import get_component_path, get_project_root

from app.crews.debug_crew import debug_react_component


project_name = "project_001"
project_root = get_project_root(project_name)
component_path = get_component_path(project_name, "LoginPage.jsx")


result = run_react_app(project_name)

if result["success"]:

    print("\nBuild succeeded. No debugging needed.")

else:

    print("\nBuild failed. Starting debug agent...\n")

    failed_file = result.get("failed_file")
    if failed_file:
        component_path = project_root / failed_file

    broken_code = read_file(component_path)

    fixed_code = debug_react_component(
        error_logs=result["stderr"],
        broken_code=broken_code
    )

    rewrite_file(component_path, fixed_code)

    print("\nFile rewritten with AI-generated fix.")
