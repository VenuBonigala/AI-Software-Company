from crewai import Crew, Task
from app.agents.debug_agent import debug_agent


def debug_react_component(error_logs, broken_code):

    debug_task = Task(
        description=f"""
        The following React component failed to build.

        ERROR LOGS:
        {error_logs}

        BROKEN CODE:
        {broken_code}

        Fix the component.

        IMPORTANT:
        Return ONLY corrected React code.
        """,

        expected_output="""
        Corrected React component code.
        """,

        agent=debug_agent
    )

    crew = Crew(
        agents=[debug_agent],
        tasks=[debug_task],
        verbose=True
    )

    result = crew.kickoff()

    return result.raw