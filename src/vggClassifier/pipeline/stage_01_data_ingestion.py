from vggClassifier.constants import *
from vggClassifier.utils.common import read_yaml, create_directories
from vggClassifier import logger
from vggClassifier.components.data_ingestion import DataIngestion
from vggClassifier.config.configuration import DataIngestionManager


STAGE_NAME = "DATA_INGESTION_STAGE"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        dim = DataIngestionManager( CONFIG_FILE_PATH, PARAMS_FILE_PATH )
        config = dim.get_data_ingestion_as_entity()
        data_ingestion_object = DataIngestion(config)
        data_ingestion_object.download_data()
        data_ingestion_object.unzip_data()


# verification of this stage <actual invokation after dvc>
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed! <<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e