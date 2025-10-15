from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    display_name = Column(String, nullable=True)
    preferred_currency = Column(String, default='USD')
    preferred_distance_unit = Column(String, default='km')
    preferred_volume_unit = Column(String, default='L')
    time_zone = Column(String, default='UTC')

    vehicles = relationship("Vehicle", back_populates="owner")

class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String, nullable=False)
    make = Column(String, nullable=True)
    model = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    fuel_type = Column(String, nullable=True)

    owner = relationship("User", back_populates="vehicles")
    fuel_entries = relationship("FuelEntry", back_populates="vehicle")

class FuelEntry(Base):
    __tablename__ = 'fuel_entries'

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    date = Column(String, nullable=False)
    odometer = Column(Float, nullable=False)
    station_name = Column(String, nullable=False)
    fuel_brand = Column(String, nullable=False)
    fuel_grade = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    total_amount = Column(Float, nullable=False)
    notes = Column(String, nullable=True)

    vehicle = relationship("Vehicle", back_populates="fuel_entries")