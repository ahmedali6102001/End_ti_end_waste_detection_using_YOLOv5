import os,sys
import shutil
from wasteDetection.logger import logging
from wasteDetection.exception import AppException
from wasteDetection.entity.config_entity import DataValidationConfig
from wasteDetection.entity.artifacts_entity import (DataIngestionArtifact,
                                                 DataValidationArtifact)


class DataValidation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise AppException(e, sys) 
        
    
    def validate_all_files_exist(self)-> bool:
        try:
            validation_status = None

            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)

            for file in all_files:
                if file not in self.data_validation_config.required_file_list:
                    validation_status = False
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)

                    if file == self.data_validation_config.required_file_list[0] or file == self.data_validation_config.required_file_list[1]:
                        images_dir = os.path.join(self.data_ingestion_artifact.feature_store_path, file, 'images')
                        labels_dir = os.path.join(self.data_ingestion_artifact.feature_store_path, file, 'labels')

                        try:
                            for image in os.listdir(images_dir):
                                if not image.endswith('jpg') and not image.endswith('png'):
                                    validation_status = False
                                    error_message = f'Invalid file format in images directory: {image}'
                                    raise AppException(error_message, sys)
                                    
                        except Exception as e:
                                 validation_status = False
                                 with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                                    f.write(f"Validation status: {validation_status}")  
                                 raise AppException(error_message, sys)
                        
                            
                        try:
                            for label in os.listdir(labels_dir):
                                if not label.endswith('yolo'):
                                    validation_status = False
                                    error_message = f"Invalid file format in labels directory: {label}"
                                    raise AppException(error_message, sys)
                        except Exception as e:
                            validation_status = False
                            with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                                f.write(f"Validation status: {validation_status}")  
                            raise AppException(error_message, sys)

                                
                                  
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")  
                    

            return validation_status


        except Exception as e:
            raise AppException(e, sys)
        

    
    def initiate_data_validation(self) -> DataValidationArtifact: 
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(
                validation_status=status)

            logging.info("Exited initiate_data_validation method of DataValidation class")
            logging.info(f"Data validation artifact: {data_validation_artifact}")

            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

            return data_validation_artifact

        except Exception as e:
            raise AppException(e, sys)
        