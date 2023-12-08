# Auto Info Database

This project involves the creation and management of a database for automotive information.
The database includes tables for transmissions, engines, and cars, with foreign key relationships
established between them.

# Requirements

- Python = 3.11

# Usage

1. Clone the repository.

2. Install the required dependencies:

```bash

pip install pandas sqlalchemy kaggle

```
3. Set up your PostgreSQL database and update the database connection details in pandasDB/pandas_db.py and models.py.

4. Set your Kaggle API credentials by creating credentials folder creating KAGGLE_USERNAME and KAGGLE_KEY.

5. Run the main script:

```bash
python main.py
```

This script will download the specified CSV file from Kaggle, process the data, 
and populate the PostgreSQL database with the relevant tables.

# Project Structure

`pandasDB/pandas_db.py`: Main script for processing data and managing the database.

`pandasDB/models.py`: Definitions of database tables using SQLAlchemy.

`main.py`: Entry point script for running the project.

`pandasDB/kaggle_downloader.py`: Script for downloading files from Kaggle.

`pandasDB/constants/const.py`: Create Constants and file paths used in the project.

# Customization

Feel free to customize the following aspects according to your needs:

* Database Schema: Modify the database schema in `models.py` to suit your specific requirements

* File Paths: Create file paths in `const.py` as needed.

* Credentials: Create a folder credentials and in there create `credentials.py` 
provide there your 
DB_URL 
KAGGLE_USERNAME 
KAGGLE_KEY

# Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or bug fixes.