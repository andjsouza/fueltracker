from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from app.api.auth import router as auth_router
from app.db import models
from app.db.database import engine, SessionLocal

app = FastAPI()
app.include_router(auth_router)

client = TestClient(app)

def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_signup():
    response = client.post("/auth/signup", json={
        "email": "testuser@example.com",
        "password": "Test1234"
    })
    assert response.status_code == 201
    assert response.json()["email"] == "testuser@example.com"

def test_signup_duplicate_email():
    client.post("/auth/signup", json={
        "email": "testuser@example.com",
        "password": "Test1234"
    })
    response = client.post("/auth/signup", json={
        "email": "testuser@example.com",
        "password": "Test1234"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered."

def test_signin():
    client.post("/auth/signup", json={
        "email": "testuser@example.com",
        "password": "Test1234"
    })
    response = client.post("/auth/signin", json={
        "email": "testuser@example.com",
        "password": "Test1234"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_signin_invalid_credentials():
    response = client.post("/auth/signin", json={
        "email": "wronguser@example.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials."