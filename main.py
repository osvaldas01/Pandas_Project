"""
    This file is the main file of the project.
    It is used to run the project.
    It uses the FileReader class to read and process data from the CSV file.
"""

from pandasDB.pandas_db import FileReader
from pandasDB.constants.const import CSV_FILE_URL
from pandasDB.postgreSQL.models import *


file = FileReader(CSV_FILE_URL)
file.run()