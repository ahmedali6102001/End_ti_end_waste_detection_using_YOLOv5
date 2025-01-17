import logging
import os
from datetime import datetime
from from_root import from_root

log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #naming the file

log_path = os.path.join(from_root(), 'log', log_file) # root dir/folder name/file name 

os.makedirs(log_path, exist_ok=True) #creating the path

  
log_file_path = os.path.join(log_path, log_file)

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
        )