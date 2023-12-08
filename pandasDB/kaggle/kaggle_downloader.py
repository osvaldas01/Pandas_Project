"""
Module for downloading datasets from Kaggle using Kaggle API. 
It defines the KaggleDownloader class with methods to authenticate and download files.
"""

import os
from kaggle.api.kaggle_api_extended import KaggleApi
from pandasDB.constants.const import DATA_SET, DATA_FILE_LOCATION
from pandasDB.credentials.credentials import KAGGLE_USERNAME, KAGGLE_KEY

class KaggleDownloader:
    """
    Class to handle Kaggle dataset downloads.

    """
    def __init__(self):
        self.data_set = DATA_SET
        self.data_file_location = DATA_FILE_LOCATION
    
    def download_file(self):
        """
        Downloads the specified Kaggle dataset and extracts the files to a given location.
        """
        os.environ['KAGGLE_USERNAME'] = KAGGLE_USERNAME
        os.environ['KAGGLE_KEY'] = KAGGLE_KEY

        api = KaggleApi()
        api.authenticate()

        api.dataset_download_files(self.data_set, path=self.data_file_location, unzip=True)