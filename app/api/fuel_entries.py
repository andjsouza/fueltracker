from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import crud, models, schemas
from app.db.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.FuelEntry)
def create_fuel_entry(fuel_entry: schemas.FuelEntryCreate, db: Session = Depends(get_db)):
    return crud.create_fuel_entry(db=db, fuel_entry=fuel_entry)

@router.get("/", response_model=list[schemas.FuelEntry])
def read_fuel_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    fuel_entries = crud.get_fuel_entries(db=db, skip=skip, limit=limit)
    return fuel_entries

@router.get("/{fuel_entry_id}", response_model=schemas.FuelEntry)
def read_fuel_entry(fuel_entry_id: int, db: Session = Depends(get_db)):
    db_fuel_entry = crud.get_fuel_entry(db=db, fuel_entry_id=fuel_entry_id)
    if db_fuel_entry is None:
        raise HTTPException(status_code=404, detail="Fuel entry not found")
    return db_fuel_entry

@router.put("/{fuel_entry_id}", response_model=schemas.FuelEntry)
def update_fuel_entry(fuel_entry_id: int, fuel_entry: schemas.FuelEntryUpdate, db: Session = Depends(get_db)):
    db_fuel_entry = crud.get_fuel_entry(db=db, fuel_entry_id=fuel_entry_id)
    if db_fuel_entry is None:
        raise HTTPException(status_code=404, detail="Fuel entry not found")
    return crud.update_fuel_entry(db=db, fuel_entry_id=fuel_entry_id, fuel_entry=fuel_entry)

@router.delete("/{fuel_entry_id}", response_model=schemas.FuelEntry)
def delete_fuel_entry(fuel_entry_id: int, db: Session = Depends(get_db)):
    db_fuel_entry = crud.get_fuel_entry(db=db, fuel_entry_id=fuel_entry_id)
    if db_fuel_entry is None:
        raise HTTPException(status_code=404, detail="Fuel entry not found")
    return crud.delete_fuel_entry(db=db, fuel_entry_id=fuel_entry_id)