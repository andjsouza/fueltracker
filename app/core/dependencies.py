from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.security import get_current_user

# Dependency to get the current user
def get_current_active_user(current_user: str = Depends(get_current_user)):
    return current_user

# Dependency to get the database session
def get_db_session() -> Session:
    db = get_db()
    try:
        yield db
    finally:
        db.close()