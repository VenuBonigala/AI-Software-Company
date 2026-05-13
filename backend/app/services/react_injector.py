import os


def update_app_jsx(project_name, component_name, filename):

    app_jsx_path = f"""
app/generated_projects/{project_name}/frontend/src/App.jsx
""".strip()

    filename_without_extension = filename.replace(".jsx", "")

    content = f"""
import './App.css'
import {component_name} from './components/{filename_without_extension}'

function App() {{
  return (
    <>
      <{component_name} />
    </>
  )
}}

export default App
"""

    with open(app_jsx_path, "w", encoding="utf-8") as file:
        file.write(content)

    print("App.jsx updated successfully!")