import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format= '[%(asctime)s]: %(message)s:')

project_name = 'wasteDetection'

list_of_files = [
    '.github/workflows/.gitkeep', #needed for deployment  (.gitkeep) because i can't push an empty file in the begining
    'data/.gitkeep',  #the passed images in the deployed app will pass throught the backend and saved in this folder
    f'{project_name}/__init__.py', #constructor file to be as a local package to install the component in the wasteDetection
    f'{project_name}/components/__init__.py',
    f'{project_name}/components/data_ingestion.py',
    f'{project_name}/components/data_validation.py',
    f'{project_name}/components/model_trainer.py',
    f'{project_name}/constant/__init__.py',
    f'{project_name}/constant/training_pipeline/__init__.py',
    f'{project_name}/constant/application.py',
    f'{project_name}/entity/config_entity.py',
    f'{project_name}/entity/artifacts_entity.py',
    f'{project_name}/exception/__init__.py',   
    f'{project_name}/logger/__init__.py',  
    f'{project_name}/pipeline/__init__.py',
    f'{project_name}/pipeline/training_pipeline.py',
    f'{project_name}/utils/__init__.py',
    f'{project_name}/utils/main_utils.py',
    'research/trials.ipynb',
    'templete/index.html',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py'
    ]

for i in list_of_files:
    filepath = Path(i)  # this function to detect the OS and then convert the path in the way that the OS can understand

    #we need to create the folders then files
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        #if the directory is not empty then create the directory
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for thr file {filename}')

    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        #if the file is not exist or it is empty then create the file
        with open(filepath, "w") as f:
            logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} is already created....")


