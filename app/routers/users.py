from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.services import  user_service
from app.database import SessionLocal
from app.dependencies import get_db
from app import crud, schemas,auth

import logging
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

#--------------------------
# Register User
#--------------------------

@router.post(
    "/register",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register_user(
    user: schemas.UserCreate,
    db: Session= Depends(get_db)
):
    return user_service.register_user(user, db)

#--------------------------
# Login User
#--------------------------

@router.post("/login")
def login_user(
    from_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    
    return user_service.login_user(from_data,db)