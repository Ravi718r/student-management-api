from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app import schemas, services

from app.auth import (
    get_current_user,
    admin_required,
)

router = APIRouter(
    prefix="/faculty-subjects",
    tags=["Faculty Subjects"],
)


@router.post(
    "",
    response_model=schemas.FacultySubjectResponse,
)
def create_faculty_subject(
    faculty_subject: schemas.FacultySubjectCreate,
    db: Session = Depends(get_db),
    user=Depends(admin_required),
):
    return services.create_faculty_subject(
        db,
        faculty_subject,
    )


@router.get(
    "",
    response_model=list[schemas.FacultySubjectWithDetails],
)
def get_faculty_subjects(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return services.get_faculty_subjects(db)


@router.get(
    "/faculty/{faculty_id}",
    response_model=list[schemas.FacultySubjectWithDetails],
)
def get_by_faculty(
    faculty_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return services.get_faculty_subjects_by_faculty(
        db,
        faculty_id,
    )


@router.get(
    "/subject/{subject_id}",
    response_model=list[schemas.FacultySubjectWithDetails],
)
def get_by_subject(
    subject_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return services.get_faculty_subjects_by_subject(
        db,
        subject_id,
    )


@router.get(
    "/{faculty_subject_id}",
    response_model=schemas.FacultySubjectWithDetails,
)
def get_faculty_subject(
    faculty_subject_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return services.get_faculty_subject(
        db,
        faculty_subject_id,
    )


@router.delete(
    "/{faculty_subject_id}",
)
def delete_faculty_subject(
    faculty_subject_id: int,
    db: Session = Depends(get_db),
    user=Depends(admin_required),
):
    services.delete_faculty_subject(
        db,
        faculty_subject_id,
    )

    return {
        "message": "Faculty Subject mapping deleted successfully."
    }