from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from fastapi import Depends

import app.models
import app.schemas
import app.auth

from app.crud.base import BaseCRUD

#-------------------------------
# GET USER BY EMAIL
#-------------------------------

def get_user_by_email(
        db: Session,
        email: str
):
    return db.query(app.models.User).filter(
        app.models.User.email == email
    ).first()

#-------------------------------
# Autheticate user
#-------------------------------

def authenticate_user(
    db: Session,
    email: str,
    password: str
):

    print("Email received:", email)

    user = get_user_by_email(db, email)

    print("User found:", user)

    if user is None:
        return None

    print("Stored Hash:", user.hashed_password)

    print("Password Match:",
          app.auth.verify_password(password, user.hashed_password))

    if not app.auth.verify_password(
        password,
        user.hashed_password
    ):
        return None

    return user

#-------------------------------
# CREATE USER 
#-------------------------------

def create_user(
        db: Session,
        user: app.schemas.UserCreate
):
    hashed_password = app.auth.hash_password(
        user.password
    )

    new_user = app.models.User(

        username = user.username,
        email = user.email,
        hashed_password = hashed_password,

        role="student"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
