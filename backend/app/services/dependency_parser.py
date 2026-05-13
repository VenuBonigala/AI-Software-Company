import re


def normalize_package(package_name):

    if package_name.startswith("@"):

        parts = package_name.split("/")

        if len(parts) >= 2:
            return f"{parts[0]}/{parts[1]}"

    return package_name.split("/")[0]


def extract_npm_packages(code):

    imports = re.findall(
        r'import .* from ["\'](.*?)["\']',
        code
    )

    packages = []

    ignored_packages = [
        "react"
    ]

    for item in imports:

        if item.startswith("."):
            continue

        normalized = normalize_package(item)

        if normalized in ignored_packages:
            continue

        packages.append(normalized)

    return list(set(packages))