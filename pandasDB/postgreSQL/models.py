"""
This file contains the models for the database.
It defines the tables and their columns.
"""

from sqlalchemy import Column, Integer, String, create_engine, Float
from sqlalchemy.orm import declarative_base
from pandasDB.credentials.credentials import DB_URL

engine = create_engine(DB_URL)
Base = declarative_base()

Base.metadata.clear()


class Transmissions(Base):
    """
    Class to create the transmissions table.
    """

    __tablename__ = 'transmissions'
    transmission_id = Column('transmission_id', Integer, primary_key=True)
    transmission = Column('transmission', String)
    transmission_type = Column('transmission_type', String)

class Engine(Base):
    """
    Class to create the engine table.
    """

    __tablename__ = 'engine'
    engine_id = Column('engine_id', Integer, primary_key=True)
    engine_type = Column('engine_type', String)
    fuel_type = Column('fuel_type', String)
    cc_displacement = Column('cc_displacement', Integer)
    power = Column('power_bhp', Integer)
    torque = Column('torque_nm', Float)
    mileage = Column('mileage_kmpl', Float)

class Cars(Base):
    """
    Class to create the cars table.
    """

    __tablename__ = 'cars'
    car_id = Column('id', Integer, primary_key=True)
    car_name = Column('car_name', String)
    make = Column('make', String)
    model = Column('model', String)
    make_year = Column('make_year', Integer)
    color = Column('color', String)
    body_type = Column('body_type', String)
    mileage_run = Column('mileage_run', String)
    no_of_owners = Column('no_of_owners', String)
    seating_capacity = Column('seating_capacity', Integer)
    fuel_tank_capacity = Column('fuel_tank_capacity', Integer)
    emission = Column('emission', String)
    price = Column('price', Float)
    trans_id = Column(Integer)
    engine_id = Column(Integer)

Base.metadata.create_all(engine)



