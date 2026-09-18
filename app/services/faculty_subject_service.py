import logging

from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.exceptions import (
    FacultyNotFoundException,
    SubjectNotFoundException,
    FacultySubjectNotFoundException,
    FacultySubjectAlreadyExistsException,
)

logger = logging.getLogger(__name__)


def create_faculty_subject(
    db: Session,
    faculty_subject: schemas.FacultySubjectCreate,
):
    faculty = crud.get_faculty(db, faculty_subject.faculty_id)
    if not faculty:
        raise FacultyNotFoundException()

    subject = crud.get_subject(db, faculty_subject.subject_id)
    if not subject:
        raise SubjectNotFoundException()

    existing = crud.get_by_faculty_subject(
        db,
        faculty_subject.faculty_id,
        faculty_subject.subject_id,
    )

    if existing:
        raise FacultySubjectAlreadyExistsException()

    logger.info(
        f"Assigning Subject {faculty_subject.subject_id} "
        f"to Faculty {faculty_subject.faculty_id}"
    )

    return crud.create_faculty_subject(db, faculty_subject)


def get_faculty_subject(
    db: Session,
    faculty_subject_id: int,
):
    mapping = crud.get_faculty_subject(
        db,
        faculty_subject_id,
    )

    if not mapping:
        raise FacultySubjectNotFoundException()

    return mapping


def get_faculty_subjects(db: Session):
    return crud.get_faculty_subjects(db)


def delete_faculty_subject(
    db: Session,
    faculty_subject_id: int,
):
    mapping = crud.get_faculty_subject(
        db,
        faculty_subject_id,
    )

    if not mapping:
        raise FacultySubjectNotFoundException()

    logger.info(
        f"Deleting FacultySubject {faculty_subject_id}"
    )

    return crud.delete_faculty_subject(db, mapping)


def get_faculty_subjects_by_faculty(
    db: Session,
    faculty_id: int,
):
    faculty = crud.get_faculty(db, faculty_id)

    if not faculty:
        raise FacultyNotFoundException()

    return crud.get_by_faculty(db, faculty_id)


def get_faculty_subjects_by_subject(
    db: Session,
    subject_id: int,
):
    subject = crud.get_subject(db, subject_id)

    if not subject:
        raise SubjectNotFoundException()

    return crud.get_by_subject(db, subject_id)