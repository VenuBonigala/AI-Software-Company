import os
import json
import subprocess
import threading
import time
from contextlib import contextmanager

from app.services.project_paths import get_frontend_root, get_frontend_src_root, get_project_root


_build_lock = threading.Lock()
_LOCK_TIMEOUT_SECONDS = 120
_STALE_LOCK_SECONDS = 600


def _npm_command():
    return "npm.cmd" if os.name == "nt" else "npm"


def _relative_path(path, base_path):
    return str(path.relative_to(base_path)).replace("\\", "/")


def _find_unbuilt_source_files(project_root):
    sibling_src_root = project_root / "src"

    if not sibling_src_root.exists():
        return []

    return [
        _relative_path(path, project_root)
        for path in sibling_src_root.rglob("*")
        if path.is_file() and path.suffix in {".js", ".jsx", ".ts", ".tsx"}
    ]


def _validation_failure(message, failed_files=None):
    failed_files = failed_files or []

    return {
        "success": False,
        "stdout": "",
        "stderr": message,
        "returncode": None,
        "failed_files": failed_files,
        "failed_file": failed_files[0] if failed_files else None,
        "phase": "preflight",
    }


def _get_package_scripts(frontend_path):
    package_json_path = frontend_path / "package.json"

    if not package_json_path.exists():
        return {}

    with open(package_json_path, "r", encoding="utf-8") as file:
        package_json = json.load(file)

    return package_json.get("scripts", {})


def _run_npm_script(frontend_path, script_name):
    command = [_npm_command(), "run", script_name]

    return subprocess.run(
        command,
        cwd=frontend_path,
        capture_output=True,
        text=True,
        shell=False,
    )


@contextmanager
def _frontend_build_lock(frontend_path):
    lock_path = frontend_path / ".build-validation.lock"
    start_time = time.time()

    while True:
        try:
            lock_fd = os.open(str(lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(lock_fd, str(os.getpid()).encode("utf-8"))
            break
        except FileExistsError:
            try:
                lock_age = time.time() - lock_path.stat().st_mtime
            except FileNotFoundError:
                continue

            if lock_age > _STALE_LOCK_SECONDS:
                try:
                    lock_path.unlink()
                    continue
                except FileNotFoundError:
                    continue

            if time.time() - start_time > _LOCK_TIMEOUT_SECONDS:
                raise TimeoutError(
                    f"Timed out waiting for frontend build lock: {lock_path}"
                )

            time.sleep(0.25)

    try:
        yield
    finally:
        os.close(lock_fd)
        try:
            lock_path.unlink()
        except FileNotFoundError:
            pass


def run_react_app(project_name):
    project_root = get_project_root(project_name)
    frontend_path = get_frontend_root(project_name)
    frontend_src_root = get_frontend_src_root(project_name)

    if not frontend_path.exists():
        return _validation_failure(
            f"Frontend directory does not exist: {frontend_path}"
        )

    if not frontend_src_root.exists():
        return _validation_failure(
            f"Frontend source directory does not exist: {frontend_src_root}"
        )

    unbuilt_source_files = _find_unbuilt_source_files(project_root)
    if unbuilt_source_files:
        return _validation_failure(
            "Build validation aborted: source files were found outside the Vite "
            "frontend source tree. npm run build only validates files imported "
            f"from {_relative_path(frontend_src_root, project_root)}, so these "
            "files would be invisible to the build:\n"
            + "\n".join(unbuilt_source_files),
            failed_files=unbuilt_source_files,
        )

    scripts = _get_package_scripts(frontend_path)
    validation_scripts = [
        script_name
        for script_name in ("lint", "build")
        if script_name in scripts
    ]

    if "build" not in scripts:
        return _validation_failure(
            "Frontend package.json does not define a build script."
        )

    try:
        with _build_lock, _frontend_build_lock(frontend_path):
            stdout_parts = []
            stderr_parts = []

            for script_name in validation_scripts:
                result = _run_npm_script(frontend_path, script_name)
                stdout_parts.append(result.stdout)
                stderr_parts.append(result.stderr)

                if result.returncode != 0:
                    return {
                        "success": False,
                        "stdout": "".join(stdout_parts),
                        "stderr": "".join(stderr_parts),
                        "returncode": result.returncode,
                        "failed_files": [],
                        "failed_file": None,
                        "phase": script_name,
                    }
    except TimeoutError as error:
        return _validation_failure(str(error))

    return {
        "success": True,
        "stdout": "".join(stdout_parts),
        "stderr": "".join(stderr_parts),
        "returncode": 0,
        "failed_files": [],
        "failed_file": None,
        "phase": "build",
    }
