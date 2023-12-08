"""
Module containing data processing functionality, including reading, transforming, 
and storing data in a database.
Defines the FileReader class with methods for handling CSV files, 
creating database tables, and managing data types.
"""

import pandas as pd
import os
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
from pandasDB.constants.const import COLUMNS_MAP, CSV_FILE_URL, TABLES
from pandasDB.credentials.credentials import DB_URL
from pandasDB.kaggle.kaggle_downloader import KaggleDownloader
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FileReader:
    """
    Class to handle CSV file reading and database table creation.
    """
    def __init__(self, file_name=CSV_FILE_URL):
        self.file_name = file_name
        self.Base = declarative_base()
        self.engine = create_engine(DB_URL)
        self.downloader = KaggleDownloader()
        self.inspector = inspect(self.engine)

    def read_data_from_csv(self):
        """
        Reads data from a CSV file and returns a pandas DataFrame.
        """
        auto_data = pd.read_csv(self.file_name, delimiter=',')
        return auto_data

    def remove_csv_file(self):
        """
        Removes the CSV file from the project directory.
        """
        os.remove(self.file_name)

    def drop_all_tables_from_db(self):
        """
        Drops all tables from the database.
        """
        Session = sessionmaker(bind=self.engine)
        session = Session()

        try:
            self.Base.metadata.drop_all(self.engine)
        except Exception as e:
            print(e)
        finally:
            session.close()

    def rename_csv_data(self):
        """
        Renames the columns of the CSV file to match the database table columns.
        """
        auto_data = self.read_data_from_csv()
        auto_data.rename(columns=COLUMNS_MAP, inplace=True)
        auto_data.drop_duplicates(inplace=True)
        return auto_data

    def return_correct_data_type(self):
        """
        Returns the correct data type for each column.
        """
        data = self.rename_csv_data()
        data['price'] = data['price'].str.replace(',', '')
        new_columns_type = ['mileage_kmpl', 'price', 'mileage_run']
        for col in new_columns_type:
            data[col] = pd.to_numeric(data[col], errors='coerce', downcast='float')
        return data

    def create_trans_table(self):
        """
        Creates the transmissions table in the database.
        """
        auto_data = self.return_correct_data_type()
        data = auto_data[['transmission', 'transmission_type']]
        data.drop_duplicates(inplace=True)
        data.to_sql(name='transmissions', con=create_engine(DB_URL), if_exists='append',
                    index=False, index_label='transmission_id')

    def create_engine_table(self):
        """
        Creates the engine table in the database.
        """
        auto_data = self.return_correct_data_type()
        data = auto_data[['fuel_type', 'engine_type', 'cc_displacement', 'power_bhp', 'torque_nm', 'mileage_kmpl']]
        data.drop_duplicates(inplace=True)
        data.to_sql('engine', con=create_engine(DB_URL), if_exists='append', index=False, index_label='engine_id')

    def read_data_from_db(self, table_name):
        """
        Reads data from the database and returns a pandas DataFrame.
        """
        connection = self.engine.connect()
        df = pd.read_sql_table(table_name, connection)
        return df

    def create_cars_table(self):
        """
        Creates the cars table in the database.
        """
        auto_data = self.return_correct_data_type()
        transmission_data = self.read_data_from_db('transmissions')

        auto_data = auto_data.merge(
            transmission_data,
            how='inner',
            on=['transmission', 'transmission_type'],
        )

        engine_data = self.read_data_from_db('engine')

        auto_data = auto_data.merge(
            engine_data,
            how='inner',
            on=['fuel_type', 'engine_type', 'cc_displacement', 'power_bhp', 'torque_nm', 'mileage_kmpl'],
        )
        auto_data.drop(columns=['fuel_type', 'engine_type', 'cc_displacement', 'power_bhp', 'torque_nm', 'mileage_kmpl',
                                'transmission', 'transmission_type'], axis=1, inplace=True)

        auto_data.to_sql(name='cars', con=create_engine(DB_URL), if_exists='replace',
                         index=False)

    def create_foreign_keys(self):
        """
        Creates foreign keys for the cars table.
        """
        foreign = {
            'transmission_id': 'transmissions',
            'engine_id': 'engine',
        }

        for column, foreign_key in foreign.items():
            with self.engine.connect() as con:
                statement = text(f'ALTER TABLE cars ADD FOREIGN KEY ({column}) REFERENCES {foreign_key}({column});')
                con.execute(statement)
                con.commit()

    def run(self):
        """
        Runs the file.
        """
        if 'FINAL_SPINNY_900.csv' not in self.file_name:
            self.remove_csv_file()

            if self.inspector.has_table('transmissions') and \
                    self.inspector.has_table('engine') and \
                    self.inspector.has_table('cars'):
                self.drop_all_tables_from_db()
        else:
            self.downloader.download_file()

            if self.inspector.has_table('transmissions') and \
                    self.inspector.has_table('engine') and \
                    self.inspector.has_table('cars'):
                self.drop_all_tables_from_db()

            self.create_engine_table()
            self.create_trans_table()
            self.create_cars_table()
            self.create_foreign_keys()
