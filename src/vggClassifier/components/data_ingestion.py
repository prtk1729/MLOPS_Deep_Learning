import gdown
from vggClassifier.constants import *
from vggClassifier.utils.common import read_yaml, create_directories
from vggClassifier import *
from vggClassifier.config.configuration import DataIngestionConfig


class DataIngestion:
    '''
        - Downloads data from gdrive
        - Then unzips the zip file
    '''
    def __init__(self, config: DataIngestionConfig):
        self.config = config # this is the config.data_ingestion

    def download_data(self):
        try: 
            url = self.config.source_url
            file_id = url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            zip_filename = self.config.local_data_file
            gdown.download(prefix + file_id, zip_filename)
            logger.info(f"Downloading complete and renamed as: {zip_filename}")
        except Exception as e:
            raise e

    def unzip_data(self):
        '''
            - Make the unzip_dir
            - unzip inside this dir
        '''
        # create dir to put the files after unzip
        unzip_dir = self.config.unzip_dir
        create_directories([unzip_dir])

        # unzip the files
        import zipfile
        zip_filename = self.config.local_data_file
        with zipfile.ZipFile(zip_filename, "r") as f:
            f.extractall(unzip_dir)
            logger.info(f"Zipped file: {zip_filename} is unzipped at: {unzip_dir}")
