from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.dependencies import get_db
from app.auth import get_current_user,admin_required

from app.services import department_service

from app.core.exceptions import DepartmentNotFoundException

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)

#========================
# Get All Departments
#========================
@router.get(
    "/",
    response_model=list[schemas.DepartmentResponse],
    status_code=status.HTTP_200_OK
)
def get_departments(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return department_service.get_departments(db)

#========================
# Get Departments By ID
#========================
@router.get(
    "/{department_id}",
    response_model=schemas.DepartmentResponse
)
def get_department(
    department_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
       
    return department_service.get_department(db,department_id)


#========================
# Create Department
#========================
@router.post(
    "/",
    response_model=schemas.DepartmentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_department(
    department: schemas.DepartmentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    return department_service.create_department(
        db,
        department
    )


#========================
# Update Department
#========================
@router.put(
    "/{department_id}",
    response_model=schemas.DepartmentResponse
)
def update_department(
    department_id: int,
    updated_department: schemas.DepartmentCreate,
    db: Session = Depends(get_db),
    current_user= Depends(admin_required)
):
    
    
    return department_service.update_department(db,department_id,updated_department)


#========================
# Delete Department
#========================
@router.delete(
    "/{department_id}"
)
def delete_department(
    department_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return department_service.delete_department(db,department_id)
