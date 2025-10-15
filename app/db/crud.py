from sqlalchemy.orm import Session
from . import models, schemas

# Create a new user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get a user by ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Get all users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Update a user
def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        for key, value in user.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

# Delete a user
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# Create a new vehicle
def create_vehicle(db: Session, vehicle: schemas.VehicleCreate):
    db_vehicle = models.Vehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

# Get a vehicle by ID
def get_vehicle(db: Session, vehicle_id: int):
    return db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()

# Get all vehicles
def get_vehicles(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Vehicle).filter(models.Vehicle.user_id == user_id).offset(skip).limit(limit).all()

# Update a vehicle
def update_vehicle(db: Session, vehicle_id: int, vehicle: schemas.VehicleUpdate):
    db_vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if db_vehicle:
        for key, value in vehicle.dict(exclude_unset=True).items():
            setattr(db_vehicle, key, value)
        db.commit()
        db.refresh(db_vehicle)
    return db_vehicle

# Delete a vehicle
def delete_vehicle(db: Session, vehicle_id: int):
    db_vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if db_vehicle:
        db.delete(db_vehicle)
        db.commit()
    return db_vehicle

# Create a new fuel entry
def create_fuel_entry(db: Session, fuel_entry: schemas.FuelEntryCreate):
    db_fuel_entry = models.FuelEntry(**fuel_entry.dict())
    db.add(db_fuel_entry)
    db.commit()
    db.refresh(db_fuel_entry)
    return db_fuel_entry

# Get a fuel entry by ID
def get_fuel_entry(db: Session, fuel_entry_id: int):
    return db.query(models.FuelEntry).filter(models.FuelEntry.id == fuel_entry_id).first()

# Get all fuel entries
def get_fuel_entries(db: Session, vehicle_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.FuelEntry).filter(models.FuelEntry.vehicle_id == vehicle_id).offset(skip).limit(limit).all()

# Update a fuel entry
def update_fuel_entry(db: Session, fuel_entry_id: int, fuel_entry: schemas.FuelEntryUpdate):
    db_fuel_entry = db.query(models.FuelEntry).filter(models.FuelEntry.id == fuel_entry_id).first()
    if db_fuel_entry:
        for key, value in fuel_entry.dict(exclude_unset=True).items():
            setattr(db_fuel_entry, key, value)
        db.commit()
        db.refresh(db_fuel_entry)
    return db_fuel_entry

# Delete a fuel entry
def delete_fuel_entry(db: Session, fuel_entry_id: int):
    db_fuel_entry = db.query(models.FuelEntry).filter(models.FuelEntry.id == fuel_entry_id).first()
    if db_fuel_entry:
        db.delete(db_fuel_entry)
        db.commit()
    return db_fuel_entry