from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, users, vehicles, fuel_entries, stats, settings

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(vehicles.router, prefix="/vehicles", tags=["vehicles"])
app.include_router(fuel_entries.router, prefix="/fuel-entries", tags=["fuel_entries"])
app.include_router(stats.router, prefix="/stats", tags=["stats"])
app.include_router(settings.router, prefix="/settings", tags=["settings"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Fuel Tracker API!"}