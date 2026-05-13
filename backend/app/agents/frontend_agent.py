from crewai import Agent
from app.services.crew_llm import llm

frontend_agent = Agent(
    role="Senior Frontend Developer",

    goal="""
    Generate modern React and Tailwind frontend components
    based on project requirements.
    """,

    backstory="""
    You are an elite React developer specializing in:
    - React
    - Tailwind CSS
    - responsive UI
    - beautiful modern interfaces

    You generate clean production-style code.
    """,

    llm=llm,

    verbose=True
)