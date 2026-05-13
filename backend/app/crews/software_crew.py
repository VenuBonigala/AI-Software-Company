from crewai import Crew, Task
from app.agents.pm_agent import pm_agent
from app.agents.frontend_agent import frontend_agent
import re
from app.services.react_setup import create_react_app
from app.services.react_injector import update_app_jsx
from app.services.file_writer import save_react_component
from app.services.dependency_parser import extract_npm_packages
from app.services.npm_installer import install_npm_packages

def run_software_crew(user_prompt):

    pm_task = Task(
        description=f"""
        Analyze this software request:

        {user_prompt}

        Break it into frontend development tasks.
        """,

        expected_output="""
        A structured breakdown of frontend tasks.
        """,

        agent=pm_agent
    )

    frontend_task = Task(
    description=f"""
    Based on the project manager instructions,
    generate a React + Tailwind component.

    User Request:
    {user_prompt}

    IMPORTANT RULES:

    - Return ONLY plain text
    - Do NOT use markdown bullets
    - Do NOT add **
    - Do NOT add explanations

    STRICT OUTPUT FORMAT:

    COMPONENT_NAME: LoginPage

    FILENAME: LoginPage.jsx

    CODE:
    ```jsx
    full react component code
    ```
    """,

    expected_output="""
    Structured React component output.
    """,

    agent=frontend_agent
)

    crew = Crew(
        agents=[pm_agent, frontend_agent],
        tasks=[pm_task, frontend_task],
        verbose=True
    )

    create_react_app("project_001")

    result = crew.kickoff()
    output = result.raw

    print("\nCREW EXECUTION COMPLETED\n")

    filename_match = re.search(r"FILENAME:\s*(.*)", output)
    code_match = re.search(r"```jsx(.*?)```", output, re.DOTALL)

    if filename_match and code_match:

        filename = filename_match.group(1).strip()
        code = code_match.group(1).strip()

        component_name = filename.replace(".jsx", "")

        saved_path = save_react_component(
            project_name="project_001",
            filename=filename,
            code=code
        )

        update_app_jsx(
            project_name="project_001",
            component_name=component_name,
            filename=filename
        )

        packages = extract_npm_packages(code)

        print("\nDetected Packages:")
        print(packages)

        install_npm_packages(
            project_name="project_001",
            packages=packages
        )

        print(f"\nComponent saved successfully!")
        print(f"Saved at: {saved_path}")

    else:
        print("\nCould not parse component output.")
        print("\nRAW OUTPUT:\n")
        print(output)

    return result