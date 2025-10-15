from sqlalchemy.orm import Session
from app.db import models, schemas
from app.core.security import hash_password


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_password = hash_password(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> models.User:
    return db.query(models.User).filter(models.User.email == email).first()


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate) -> models.User:
    db_user = get_user(db, user_id)
    if db_user:
        for key, value in user_update.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int) -> None:
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()