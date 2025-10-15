from pydantic_settings import BaseSettings
from fastapi import APIRouter

class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int

    # Application settings
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()


router = APIRouter()

@router.get("/")
def read_settings():
    return {"message": "Settings endpoint is working."}