from app.services.error_capture import run_react_app

result = run_react_app("project_001")

print("\nSUCCESS:")
print(result["success"])

print("\nSTDOUT:")
print(result["stdout"])

print("\nSTDERR:")
print(result["stderr"])