from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import crud, models, schemas
from app.db.database import get_db

router = APIRouter()

@router.get("/stats/overview", response_model=schemas.StatsOverview)
def get_overview_stats(db: Session = Depends(get_db)):
    return crud.get_overview_stats(db)

@router.get("/stats/vehicle/{vehicle_id}", response_model=schemas.VehicleStats)
def get_vehicle_stats(vehicle_id: int, db: Session = Depends(get_db)):
    return crud.get_vehicle_stats(db, vehicle_id)

@router.get("/stats/brand/{brand_name}", response_model=schemas.BrandStats)
def get_brand_stats(brand_name: str, db: Session = Depends(get_db)):
    return crud.get_brand_stats(db, brand_name)

@router.get("/stats/period", response_model=schemas.PeriodStats)
def get_period_stats(start_date: str, end_date: str, db: Session = Depends(get_db)):
    return crud.get_period_stats(db, start_date, end_date)