from pathlib import Path


APP_ROOT = Path(__file__).resolve().parents[1]
GENERATED_PROJECTS_ROOT = APP_ROOT / "generated_projects"


def get_project_root(project_name):
    return GENERATED_PROJECTS_ROOT / project_name


def get_frontend_root(project_name):
    return get_project_root(project_name) / "frontend"


def get_frontend_src_root(project_name):
    return get_frontend_root(project_name) / "src"


def get_component_path(project_name, filename):
    return get_frontend_src_root(project_name) / "components" / filename
