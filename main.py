from src.vggClassifier.constants import *
from src.vggClassifier.utils.common import read_yaml, create_directories
from src.vggClassifier import logger
from src.vggClassifier.components.data_ingestion import DataIngestion
from src.vggClassifier.config.configuration import DataIngestionManager
from src.vggClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "DATA_INGESTION_STAGE"


# Many layer verification
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed! <<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e