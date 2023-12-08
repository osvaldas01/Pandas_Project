"""
    This file contains all the constants used in the project.
"""

COLUMNS_MAP = {
    'Transmission': 'transmission',
    'Transmission_Type': 'transmission_type',
    'Fuel_Type': 'fuel_type',
    'Engine_Type': 'engine_type',
    'CC_Displacement': 'cc_displacement',
    'Power(BHP)': 'power_bhp',
    'Torque(Nm)': 'torque_nm',
    'Mileage(kmpl)': 'mileage_kmpl',
    'Car_Name': 'car_name',
    'Make': 'make',
    'Model': 'model',
    'Make_Year': 'make_year',
    'Color': 'color',
    'Body_Type': 'body_type',
    'Mileage_Run': 'mileage_run',
    'No_of_Owners': 'no_of_owners',
    'Seating_Capacity': 'seating_capacity',
    'Fuel_Tank_Capacity(L)': 'fuel_tank_capacity',
    'Emission': 'emission',
    'Price': 'price',
}

CSV_FILE_URL = 'pandasDB/cars/FINAL_SPINNY_900.csv'
DATA_SET = 'rakkesharv/used-cars-detailed-dataset'
DATA_FILE_LOCATION = 'pandasDB/csv_files'
TABLES = ['cars', 'engine', 'transmissions']