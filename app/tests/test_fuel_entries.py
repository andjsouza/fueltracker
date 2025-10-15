from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from app.db.models import FuelEntry
from app.db.schemas import FuelEntryCreate
from app.db.crud import create_fuel_entry, get_fuel_entries
from app.core.config import settings

app = FastAPI()

client = TestClient(app)

@app.post("/fuel-entries/", response_model=FuelEntry)
def test_create_fuel_entry(fuel_entry: FuelEntryCreate):
    response = client.post("/fuel-entries/", json=fuel_entry.dict())
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@app.get("/fuel-entries/", response_model=list[FuelEntry])
def test_get_fuel_entries():
    response = client.get("/fuel-entries/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

def test_create_fuel_entry_success():
    fuel_entry_data = {
        "vehicle_id": 1,
        "date": "2023-10-01",
        "odometer": 15000,
        "station_name": "Test Station",
        "fuel_brand": "Test Brand",
        "fuel_grade": "Regular",
        "quantity": 50,
        "total_amount": 100.0
    }
    response = test_create_fuel_entry(FuelEntryCreate(**fuel_entry_data))
    assert response["station_name"] == fuel_entry_data["station_name"]
    assert response["fuel_brand"] == fuel_entry_data["fuel_brand"]

def test_get_fuel_entries_success():
    response = test_get_fuel_entries()
    assert isinstance(response, list)  # Ensure the response is a list
    assert len(response) > 0  # Ensure there are entries returned

def test_create_fuel_entry_invalid_data():
    fuel_entry_data = {
        "vehicle_id": 1,
        "date": "2023-10-01",
        "odometer": 15000,
        "station_name": "",
        "fuel_brand": "Test Brand",
        "fuel_grade": "Regular",
        "quantity": -10,  # Invalid quantity
        "total_amount": 100.0
    }
    try:
        test_create_fuel_entry(FuelEntryCreate(**fuel_entry_data))
    except HTTPException as e:
        assert e.status_code == 422  # Unprocessable Entity for invalid data

def test_get_fuel_entries_empty():
    # Assuming the database is empty for this test
    response = test_get_fuel_entries()
    assert response == []  # Ensure the response is an empty list