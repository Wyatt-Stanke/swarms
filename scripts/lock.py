import subprocess

import toml

# Open "pyproject.toml" and capture the dependencies
with open("pyproject.toml") as file:
    pyproject = toml.load(file)
    pyproject_deps = list(pyproject["tool"]["poetry"]["dependencies"].keys())
    python_version = pyproject["tool"]["poetry"]["dependencies"]["python"]


# Run "poetry export --format requirements.txt --without-hashes --without-urls" and capture the output
with subprocess.Popen(
    ["poetry", "export", "--format", "requirements.txt", "--without-hashes", "--without-urls"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
) as proc:
    raw = proc.stdout.read()
    requirements = []
    for requirement in raw.split("\n"):
        try:
            package, version = requirement.split(" ; ")[0].split("==")
        except ValueError:
            pass
        if package in pyproject_deps:
            requirements.append(f'{package} = "{version}"')

# Deduplicate the requirements
requirements = list(set(requirements))
requirements.sort()
# Prepend the python version to the requirements
requirements.insert(0, f'python = "{python_version}"')

# Add the requirements to the "pyproject.toml" file
with open("pyproject.toml") as file:
    pyproject = toml.load(file)
    pyproject["tool"]["poetry"]["dependencies"] = {
        requirement.split(" = ")[0]: requirement.split(" = ")[1].strip('"') for requirement in requirements
    }

    # Write the updated "pyproject.toml" file
    with open("pyproject.toml", "w") as file:
        toml.dump(pyproject, file)
