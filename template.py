import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s - %(levelname)s]: %(message)s'
    )

while True:
    project_name = input("Enter your project name: ")
    if project_name != "":
        break
    else:
        logging.info("Project name cannot be empty. Please try again.")

logging.info(f"Creating project: {project_name}")

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) #returns tuple (dir, file)
    # print(f"Folder: {filedir} ======= File: {filename}")

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename} ")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists and is not empty: {filepath}")
