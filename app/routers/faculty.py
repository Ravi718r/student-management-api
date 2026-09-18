from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import schemas
from app.dependencies import get_db
from app.auth import (
    get_current_user,
    admin_required
)

from app.services import faculty_service

router = APIRouter(
    prefix="/faculty",
    tags=["Faculty"]
)


# =====================================================
# Get All Faculty
# =====================================================
@router.get(
    "/",
    response_model=list[schemas.FacultyResponse],
    status_code=status.HTTP_200_OK
)
def get_faculties(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Retrieve all faculty members.
    """

    return faculty_service.get_faculties(db)


# =====================================================
# Get Faculty By Department
# =====================================================
@router.get(
    "/department/{department_id}",
    response_model=list[schemas.FacultyResponse],
    status_code=status.HTTP_200_OK
)
def get_faculty_by_department(
    department_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Retrieve all faculty members of a department.
    """

    return faculty_service.get_faculty_by_department(
        db,
        department_id
    )


# =====================================================
# Get Faculty By ID
# IMPORTANT:
# Keep AFTER all fixed GET routes.
# =====================================================
@router.get(
    "/{faculty_id}",
    response_model=schemas.FacultyWithDepartment,
    status_code=status.HTTP_200_OK
)
def get_faculty(
    faculty_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Retrieve faculty by ID.
    """

    return faculty_service.get_faculty(
        db,
        faculty_id
    )


# =====================================================
# Create Faculty
# =====================================================
@router.post(
    "/",
    response_model=schemas.FacultyResponse,
    status_code=status.HTTP_201_CREATED
)
def create_faculty(
    faculty: schemas.FacultyCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    """
    Create a new faculty member.

    Only Admin can create faculty.
    """

    return faculty_service.create_faculty(
        db,
        faculty
    )


# =====================================================
# Update Faculty
# =====================================================
@router.put(
    "/{faculty_id}",
    response_model=schemas.FacultyResponse,
    status_code=status.HTTP_200_OK
)
def update_faculty(
    faculty_id: int,
    faculty: schemas.FacultyUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    """
    Update faculty details.

    Only Admin can update faculty.
    """

    return faculty_service.update_faculty(
        faculty_id,
        faculty,
        db
    )


# =====================================================
# Delete Faculty
# =====================================================
@router.delete(
    "/{faculty_id}",
    status_code=status.HTTP_200_OK
)
def delete_faculty(
    faculty_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    """
    Delete faculty.

    Only Admin can delete faculty.
    """

    return faculty_service.delete_faculty(
        faculty_id,
        db
    )