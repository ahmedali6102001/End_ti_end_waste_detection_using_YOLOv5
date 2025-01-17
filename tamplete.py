import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'wasteDetection'

list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    "f{project_name}/__init__.py",
    "f{project_name}/components/__init_.py",
    "f{project_name}/components/data_ingestion.py",
    "f{project_name}/components/data_validation.py",
    "f{project_name}/components/model_trainer.py",
    "f{project_name}/constant/__init__.py",
    "f{project_name}/constant/trainingPpipeline/__init__.py",
    "f{project_name}/constant/application.py",
    "f{project_name}/entity/config_entity.py",
    "f{project_name}/entity/artifacts_entity.py",
    "f{project_name}/exception/__init__.py",
    "f{project_name}/logger/__init__.py",
    "f{project_name}/pipeline/__init__.py",
    "f{project_name}/pipeline/training_pipeline.py",
    "f{project_name}/utils/__init__.py",
    "f{project_name}/utils/main_utils.py",
    "tamplates/index/html",
    'app.py',
    "Dockerfile",
    'requirements.txt',
    'setup.py'
]


for i in list_of_files:
    filepath = Path(i)

    filedir, filename = os.path.split(i)
    if filedir != "":
        os.makedirs(i, exist_ok=True)
        logging.info(f"creating directory : {filedir} for the file {filename}")
