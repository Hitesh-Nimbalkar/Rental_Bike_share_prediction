
from Prediction_Application.logger import logging
from Prediction_Application.components.data_ingestion import DataIngestion
from Prediction_Application.config.configuration import Configuration
from Prediction_Application.entity.config_entity import DataIngestionConfig
from Prediction_Application.entity.artifact_entity import DataIngestionArtifact
from Prediction_Application.exception import ApplicationException
import os,sys


class Training_Pipeline:

    def __init__(self,config: Configuration=Configuration())->None:
        try:
            logging.info(f"\n{'*'*20} Initiating the Training Pipeline {'*'*20}\n\n")
            self.config = config
        except Exception as e:
            raise ApplicationException(e,sys) from e

    def start_data_ingestion(self,data_ingestion_config:DataIngestionConfig)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config = data_ingestion_config)
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise ApplicationException(e,sys) from e
        

    def run_training_pipeline(self):
        try:
            data_ingestion_config=self.config.get_data_ingestion_config()

            data_ingestion_artifact = self.start_data_ingestion(data_ingestion_config)
      
        except Exception as e:
            raise ApplicationException(e,sys) from e

    def __del__(self):
        logging.info(f"\n{'*'*20} Training Pipeline Complete {'*'*20}\n\n")



train_obj = Training_Pipeline()
train_obj.run_training_pipeline() # training the model for the files in the table