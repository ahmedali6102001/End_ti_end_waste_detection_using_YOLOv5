import os
import sys
import yaml
import base64

from wasteDetection.logger import logging
from wasteDetection.exception import AppException

def read_yaml_file(filepath : str) -> dict:
    try:
        with open(filepath, 'rb') as yaml_file:
            logging.info('read yaml file successfully')
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise AppException(e, sys) from e
    
    
def write_yaml_file(filepath:str , content:object, replace:bool=False) -> None:
    try:
        if replace:
            if os.path.exists(filepath):
                os.remove(filepath)
        
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, 'w') as yaml_file:
            yaml.dump(content, yaml_file)
            logging.info('write yaml file successfully')

    except Exception as e:
        raise AppException(e, sys)
    

def decodeImage(imgsrting, filename):
    imgdata = base64.b64decode(imgsrting)
    with open("./data/" + filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(img_path):
    with open(img_path, 'rb') as f:
        return base64.b64encode(f.read())