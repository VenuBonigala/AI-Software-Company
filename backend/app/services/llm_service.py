import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def generate_response(prompt: str):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def test_llm():
    result = generate_response("Say hello from OpenRouter")

    print("\nLLM RESPONSE:\n")
    print(result)