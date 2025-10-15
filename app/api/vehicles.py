from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import models, schemas, crud
from app.core.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Vehicle)
def create_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle_by_name(db, name=vehicle.name)
    if db_vehicle:
        raise HTTPException(status_code=400, detail="Vehicle already registered")
    return crud.create_vehicle(db=db, vehicle=vehicle)

@router.get("/", response_model=list[schemas.Vehicle])
def read_vehicles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    vehicles = crud.get_vehicles(db, skip=skip, limit=limit)
    return vehicles

@router.get("/{vehicle_id}", response_model=schemas.Vehicle)
def read_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle

@router.put("/{vehicle_id}", response_model=schemas.Vehicle)
def update_vehicle(vehicle_id: int, vehicle: schemas.VehicleUpdate, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return crud.update_vehicle(db=db, vehicle_id=vehicle_id, vehicle=vehicle)

@router.delete("/{vehicle_id}", response_model=schemas.Vehicle)
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return crud.delete_vehicle(db=db, vehicle_id=vehicle_id)