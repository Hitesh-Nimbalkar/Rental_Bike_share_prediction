import os
from datetime import datetime

ROOT_DIR = os.getcwd()

CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


# Database related variables
DATABASE_CLIENT_URL_KEY = "mongodb+srv://nimbalkarhitesh:JrgoWqPF7whQMCZW@rentalbike.5fi8zs7.mongodb.net/test"
DATABASE_NAME_KEY = "Rental_Bike_Share_DB"
DATABASE_COLLECTION_NAME_KEY = "RentalBike"
DATABASE_TRAINING_COLLECTION_NAME_KEY = "Training"
DATABASE_TEST_COLLECTION_NAME_KEY = "Test"



# Training pipeline related vaariables
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"

TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"

# Data Ingestion related variables p6CpHLpKduJ4VB3Q
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"

DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"

# Data Validation related variables
DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_ARTIFACT_DIR_NAME = "data_validation"
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY = "schema_file_name"
DATA_VALIDATION_SCHEMA_DIR_KEY = "schema_dir"
DATA_VALIDATION_REPORT_FILE_NAME_KEY = "report_file_name"
DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY = "report_page_file_name"
