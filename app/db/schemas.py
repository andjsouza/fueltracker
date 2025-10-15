from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    email: str
    display_name: Optional[str] = None
    preferred_currency: Optional[str] = "USD"
    preferred_distance_unit: Optional[str] = "km"
    preferred_volume_unit: Optional[str] = "L"
    time_zone: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    display_name: Optional[str] = None
    password: Optional[str] = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class VehicleBase(BaseModel):
    name: str
    make: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    fuel_type: Optional[str] = None

class VehicleCreate(VehicleBase):
    user_id: int

class VehicleUpdate(BaseModel):
    name: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None

class Vehicle(VehicleBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class FuelEntryBase(BaseModel):
    vehicle_id: int
    date: datetime
    odometer: int
    station_name: str
    fuel_brand: str
    fuel_grade: str
    quantity: float
    total_amount: float
    notes: Optional[str] = None

class FuelEntryCreate(FuelEntryBase):
    pass

class FuelEntryUpdate(BaseModel):
    station_name: Optional[str] = None
    fuel_brand: Optional[str] = None
    fuel_grade: Optional[str] = None
    total_amount: Optional[float] = None
    quantity: Optional[float] = None
    odometer: Optional[int] = None
    date: Optional[datetime] = None
    notes: Optional[str] = None

class FuelEntry(FuelEntryBase):
    id: int

    class Config:
        orm_mode = True

class Stats(BaseModel):
    average_cost_per_liter: float
    average_consumption: float
    total_distance: float
    total_spend: float
    average_distance_per_day: float

class BrandGradeStats(BaseModel):
    brand: str
    average_cost_per_liter: float
    average_consumption: float
    number_of_fillups: int

class Dashboard(BaseModel):
    current_rolling_average_consumption: float
    rolling_average_cost_per_liter: float
    total_spend: float
    total_distance: float
    average_cost_per_km: float
    average_distance_per_day: float
    brand_grade_comparison: List[BrandGradeStats]

class Token(BaseModel):
    access_token: str
    token_type: str

class UserLogin(BaseModel):
    email: str
    password: str

class Message(BaseModel):
    message: str

class StatsOverview(BaseModel):
    total_distance: float
    total_fuel: float
    total_cost: float
    average_consumption: Optional[float] = None
    average_cost_per_liter: Optional[float] = None
    average_cost_per_km: Optional[float] = None
    # Add more fields as needed

class VehicleStats(BaseModel):
    vehicle_id: int
    total_distance: float
    total_fuel: float
    total_cost: float
    average_consumption: Optional[float] = None
    average_cost_per_liter: Optional[float] = None
    average_cost_per_km: Optional[float] = None
    # Add more fields as needed

class BrandStats(BaseModel):
    brand_name: str
    total_fuel: float
    total_cost: float
    average_consumption: Optional[float] = None
    average_cost_per_liter: Optional[float] = None
    average_cost_per_km: Optional[float] = None
    # Add more fields as needed

class PeriodStats(BaseModel):
    start_date: str
    end_date: str
    total_distance: float
    total_fuel: float
    total_cost: float
    average_consumption: Optional[float] = None
    average_cost_per_liter: Optional[float] = None
    average_cost_per_km: Optional[float] = None
    # Add more fields as needed