import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

llm = LLM(
    model=os.getenv("MODEL_NAME"),
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)