import os
from pathlib import Path
import logging
from venv import logger

files = [
    '.github/workflows/.gitkeep',# GitHub Actions workflows are stored.
     # These workflows automate tasks like CI/CD, testing, and deployment
    'src/__init__.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_trainer.py',
    'src/components/model_evaluation.py',
    'src/pipeline/__init__.py',
    'src/pipeline/training_pipeline.py',
    'src/pipeline/prediction_pipeline.py',
    'src/utils/__init__.py',
    'src/utils/utils.py',
    'src/logger/logging.py',# it's used to configure logging for Python project
    'src/exeptions/exception.py',#used to define custom exception classes for error handling in a Python project.
    'tests/unit/__init__.py',
    'tests/unit/integration/__init__.py',
    'init_setup.sh',
    'requirements.txt',
    'requirements_dev.txt',
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    #for configuring Python packages, introduced in PEP 518.
    # It replaces setup.py and setup.cfg in modern package management.
    'tox.ini',#Standardize testing across teams and CI/CD pipelines
    # Run tests automatically with tools like pytest or unittest
    #1️⃣ Creates isolated environments for testing.
    #2️⃣ Installs dependencies and runs test commands.
    #3️⃣ Ensures compatibility across Python versions."""
    'experiment/experiments.ipynb'
]

for filepath in files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !='':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'creating directory :{filedir} for file :{filename}')
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath == 0)):
        with open(filepath, 'w') as f:
            pass