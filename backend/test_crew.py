from app.crews.software_crew import run_software_crew

prompt = "Build a modern login page using React and Tailwind CSS"

result = run_software_crew(prompt)

print("\n" + "=" * 50)
print("FINAL RESULT")
print("=" * 50)

try:
    print(result.raw)
except:
    print(result)