from vggClassifier.constants import *
from vggClassifier.utils.common import read_yaml, create_directories
from vggClassifier.entity.config_entity import DataIngestionConfig


class DataIngestionManager:
    '''
        - Creates the required folders using config.yaml
        - Sets the data_ingestion properties as a dict
        - Finally wraps the dict as an entity (here DataIngestionConfig)
    '''
    def __init__(self, \
                 CONFIG_FILE_PATH,
                 PARAMS_FILE_PATH):
        self.params_filepath = PARAMS_FILE_PATH
        self.config_filepath = CONFIG_FILE_PATH

        # load these yaml
        self.config_dict = read_yaml(filepath=self.config_filepath)
        self.params_dict = read_yaml(filepath=self.params_filepath)

        # create artifacts_root directory 
        create_directories([self.config_dict.artifacts_root]) # BoxConfig type


    def get_data_ingestion_as_entity(self)->DataIngestionConfig:
        """
            Creates data_ingestion folder
            Sets the key-value of data_ingestion in config.yaml
            Returns as a DataIngestionConfig type
        """
        config = self.config_dict.data_ingestion

        # create root directory
        create_directories([config.root_dir])

        data_ingest_obj = DataIngestionConfig( root_dir=config.root_dir,\
                             source_url=config.source_url,
                             unzip_dir=config.unzip_dir,
                             local_data_file=config.local_data_file
                              )
        return data_ingest_obj
