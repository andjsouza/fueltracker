from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from app.db import models, schemas, crud
from app.db.database import get_db

app = FastAPI()

@app.post("/vehicles/", response_model=schemas.Vehicle)
def create_vehicle(vehicle: schemas.VehicleCreate, db: Session = next(get_db())):
    db_vehicle = crud.get_vehicle_by_name(db, name=vehicle.name)
    if db_vehicle:
        raise HTTPException(status_code=400, detail="Vehicle already registered")
    return crud.create_vehicle(db=db, vehicle=vehicle)

@app.get("/vehicles/{vehicle_id}", response_model=schemas.Vehicle)
def read_vehicle(vehicle_id: int, db: Session = next(get_db())):
    db_vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle

@app.put("/vehicles/{vehicle_id}", response_model=schemas.Vehicle)
def update_vehicle(vehicle_id: int, vehicle: schemas.VehicleUpdate, db: Session = next(get_db())):
    db_vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return crud.update_vehicle(db=db, vehicle_id=vehicle_id, vehicle=vehicle)

@app.delete("/vehicles/{vehicle_id}", response_model=schemas.Vehicle)
def delete_vehicle(vehicle_id: int, db: Session = next(get_db())):
    db_vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    crud.delete_vehicle(db=db, vehicle_id=vehicle_id)
    return db_vehicle