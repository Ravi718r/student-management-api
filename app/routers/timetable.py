from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app import schemas, services
from app.auth import (
    get_current_user,
    admin_required,
)

from app.core.exceptions import (
    FacultySubjectAssignmentException
)

from app import crud;

from app.dependencies import get_db

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


router = APIRouter(
    prefix="/timetable",
    tags=["Timetable"],
)


@router.post(
    "",
    response_model=schemas.TimetableResponse,
)
def create_timetable(
    timetable: schemas.TimetableCreate,
    db: Session = Depends(get_db),
    user=Depends(admin_required),
):
    
    assignment = crud.is_faculty_assigned_to_subject(
        db,
        timetable.faculty_id,
        timetable.subject_id,
    )

    if not assignment:
        raise FacultySubjectAssignmentException()

    return services.create_timetable(
        db,
        timetable,
    )


@router.get(
    "",
    response_model=list[schemas.TimetableWithDetails],
)
def get_timetables(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return services.get_timetables(db)


@router.get(
    "/course/{course_id}",
    response_model=list[schemas.TimetableWithDetails],
)
def get_course_timetable(
    course_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return services.get_course_timetable(
        db,
        course_id,
    )


@router.get(
    "/faculty/{faculty_id}",
    response_model=list[schemas.TimetableWithDetails],
)
def get_faculty_timetable(
    faculty_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return services.get_faculty_timetable(
        db,
        faculty_id,
    )


@router.get(
    "/{timetable_id}",
    response_model=schemas.TimetableWithDetails,
)
def get_timetable(
    timetable_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return services.get_timetable(
        db,
        timetable_id,
    )


@router.put(
    "/{timetable_id}",
    response_model=schemas.TimetableResponse,
)
def update_timetable(
    timetable_id: int,
    updated: schemas.TimetableUpdate,
    db: Session = Depends(get_db),
    user=Depends(admin_required),
):
    return services.update_timetable(
        db,
        timetable_id,
        updated,
    )


@router.delete(
    "/{timetable_id}",
)
def delete_timetable(
    timetable_id: int,
    db: Session = Depends(get_db),
    user=Depends(admin_required),
):
    services.delete_timetable(
        db,
        timetable_id,
    )

    return {
        "message": "Timetable deleted successfully."
    }