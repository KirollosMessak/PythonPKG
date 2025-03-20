import os
from pathlib import Path
import logging
from venv import logger
package_name = "mongodb_connect"

list_of_files = [
    '.github/workflows/ci.yaml',# GitHub Actions workflows are stored.
     # These workflows automate tasks like CI/CD, testing, and deployment
   "src/__init__.py",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/mongo_crud.py", 
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/unit/unit.py",
   "tests/integration/__init__.py",
   "tests/integration/int.py",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
    'pyproject.toml',
    #for configuring Python packages, introduced in PEP 518.
    # It replaces setup.py and setup.cfg in modern package management.
    'tox.ini',#Standardize testing across teams and CI/CD pipelines
    # Run tests automatically with tools like pytest or unittest
    #1️⃣ Creates isolated environments for testing.
    #2️⃣ Installs dependencies and runs test commands.
    #3️⃣ Ensures compatibility across Python versions."""
   "experiments/experiments.ipynb", 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file