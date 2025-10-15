from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import schemas, crud
from app.db.database import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.get("/users/me", response_model=schemas.User)
def read_user_me(current_user: schemas.User = Depends(get_current_user)):
    return current_user

@router.put("/users/me", response_model=schemas.User)
def update_user_me(user_update: schemas.UserUpdate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    db_user = crud.update_user(db=db, user_id=current_user.id, user_update=user_update)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/users/me", response_model=schemas.Message)
def delete_user_me(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    crud.delete_user(db=db, user_id=current_user.id)
    return {"message": "User deleted successfully"}