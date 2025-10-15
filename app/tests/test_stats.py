from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.stats import router as stats_router

app = FastAPI()
app.include_router(stats_router)

client = TestClient(app)

def test_get_statistics():
    response = client.get("/api/stats")
    assert response.status_code == 200
    assert "average_cost_per_liter" in response.json()
    assert "average_consumption" in response.json()

def test_get_statistics_by_vehicle():
    response = client.get("/api/stats?vehicle_id=1")
    assert response.status_code == 200
    assert "average_cost_per_liter" in response.json()
    assert "average_consumption" in response.json()

def test_get_statistics_no_data():
    response = client.get("/api/stats?vehicle_id=999")  # Assuming this vehicle ID does not exist
    assert response.status_code == 404
    assert response.json() == {"detail": "No data found for the specified vehicle."}