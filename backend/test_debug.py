from app.services.error_capture import run_react_app
from app.services.file_reader import read_file
from app.services.file_rewriter import rewrite_file

from app.crews.debug_crew import debug_react_component


component_path = """
app/generated_projects/project_001/frontend/src/components/LoginPage.jsx
""".strip()


result = run_react_app("project_001")

if result["success"]:

    print("\nBuild succeeded. No debugging needed.")

else:

    print("\nBuild failed. Starting debug agent...\n")

    broken_code = read_file(component_path)

    fixed_code = debug_react_component(
        error_logs=result["stderr"],
        broken_code=broken_code
    )

    rewrite_file(component_path, fixed_code)

    print("\nFile rewritten with AI-generated fix.")