from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your actual database URL or use environment variables
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@db:5432/fueltracker"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
