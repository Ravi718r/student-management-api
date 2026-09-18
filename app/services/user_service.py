from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

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
    logger.info(f"Registeration request for {user.email}")

    # check if email exits or not
    existing_user=crud.get_user_by_email(
        db,
        user.email
    )

    if existing_user:
        logger.warning(f"Registeration failed. Email {user.email} already exists")

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    created_user =crud.create_user(
        db, 
        user
    )

    logger.info(f"User {created_user.email} Registered Succesfully")
    return created_user

#--------------------------
# Login User
#--------------------------

@router.post("/login")
def login_user(
    from_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    
    logger.info(f"Login attempt for {from_data.username}")

    existing_user = crud.authenticate_user(
        db,
        from_data.username,
        from_data.password
    )

    if existing_user is None:
        logger.warning(f"Failed login attempt for {from_data.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid emil and password"
        )
    
    access_token = auth.create_access_token(
        data={
            "sub": existing_user.email
        }
    )
    
    logger.info(f"User {existing_user.email} logged in successfully")

    return{
        "access_token": access_token,
        "token_type": "bearer"
    }