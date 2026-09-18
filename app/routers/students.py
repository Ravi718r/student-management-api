from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.dependencies import get_db
from app.auth import get_current_user
from app.auth import admin_required
from app.core.exceptions import StudentNotFoundException
from app.core.exceptions import StudentAlreadyExistsException, DepartmentNotFoundException
from app.services import student_service
import logging
logger = logging.getLogger(__name__)


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

# =====================================================
# Get All Students
# =====================================================
@router.get(
    "/",
    response_model=list[schemas.StudentResponse],
    status_code=status.HTTP_200_OK
)
def get_students(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return student_service.get_students(db)


# =====================================================
# Search Student By Name
# =====================================================
@router.get(
    "/search",
    response_model=list[schemas.StudentResponse]
)
def search_student(
    name: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return student_service.search_student(db,name)


# =====================================================
# Filter By Age
# =====================================================
@router.get(
    "/filter/age",
    response_model=list[schemas.StudentResponse]
)
def filter_by_age(
    age: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return student_service.filter_by_age(db, age)


# =====================================================
# Filter By Branch
# =====================================================
@router.get(
    "/filter/branch",
    response_model=list[schemas.StudentResponse]
)
def filter_by_branch(
    branch: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return student_service.filter_by_branch(db, branch)


# =====================================================
# Sort Students
# =====================================================
@router.get(
    "/sort",
    response_model=list[schemas.StudentResponse]
)
def sort_students(
    order: str = "asc",
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return student_service.sort_students(db, order)


# =====================================================
# Pagination
# =====================================================
@router.get(
    "/page",
    response_model=list[schemas.StudentResponse]
)
def paginate_students(
    page: int = 1,
    limit: int = 5,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return student_service.paginate_students(db, page, limit)


# =====================================================
# Get Student By ID
# IMPORTANT: Keep this AFTER all fixed GET routes.
# =====================================================
@router.get(
    "/{student_id}",
    response_model=schemas.StudentWithDepartment,
    status_code=status.HTTP_200_OK
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return student_service.get_student(
        db,
        student_id
    )


# =====================================================
# Create Student
# =====================================================
@router.post(
    "/",
    response_model=schemas.StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):
    return student_service.create_student(db,student)


# =====================================================
# Update Student
# =====================================================
@router.put(
    "/{student_id}",
    response_model=schemas.StudentResponse
)
def update_student(
    student_id: int,
    updated_student: schemas.StudentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    return student_service.update_student(student_id, updated_student,db)


# =====================================================
# Delete Student
# =====================================================
@router.delete(
    "/{student_id}",
    status_code=status.HTTP_200_OK
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):

    return student_service.delete_student(student_id,db)