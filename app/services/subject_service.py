from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.exceptions import (
    CourseNotFoundException,
    SubjectNotFoundException,
    SubjectAlreadyExistsException,
    SubjectCourseMismatchException
)


import logging

logger = logging.getLogger(__name__)


# ==========================================
# Create Subject
# ==========================================
def create_subject(
    db: Session,
    subject: schemas.SubjectCreate
):
    logger.info(f"Creating subject {subject.code}")

    # Check duplicate code
    existing = crud.get_subject_by_code(
        db,
        subject.code
    )

    if existing:
        logger.warning(
            f"Subject code {subject.code} already exists."
        )
        raise SubjectAlreadyExistsException()

    # Check course exists
    course = crud.get_course(
        db,
        subject.course_id
    )

    if course is None:
        logger.warning(
            f"Course {subject.course_id} not found."
        )
        raise CourseNotFoundException()
    
    

    new_subject = crud.create_subject(
        db,
        subject
    )

    logger.info(
        f"Subject {new_subject.code} created successfully."
    )

    return new_subject


# ==========================================
# Get All Subjects
# ==========================================
def get_subjects(
    db: Session
):
    logger.info("Fetching all subjects")
    return crud.get_subjects(db)


# ==========================================
# Get Subject By ID
# ==========================================
def get_subject(
    db: Session,
    subject_id: int
):
    logger.info(
        f"Fetching subject {subject_id}"
    )

    subject = crud.get_subject(
        db,
        subject_id
    )

    if subject is None:
        raise SubjectNotFoundException()

    return subject


# ==========================================
# Update Subject
# ==========================================
def update_subject(
    db: Session,
    subject_id: int,
    updated_subject: schemas.SubjectUpdate
):
    logger.info(
        f"Updating subject {subject_id}"
    )

    subject = crud.get_subject(
        db,
        subject_id
    )

    if subject is None:
        raise SubjectNotFoundException()

    course = crud.get_course(
        db,
        updated_subject.course_id
    )

    if course is None:
        raise CourseNotFoundException()

    updated = crud.update_subject(
        db,
        subject_id,
        updated_subject
    )

    logger.info(
        f"Subject {subject_id} updated successfully."
    )

    return updated


# ==========================================
# Delete Subject
# ==========================================
def delete_subject(
    db: Session,
    subject_id: int
):
    logger.info(
        f"Deleting subject {subject_id}"
    )

    deleted = crud.delete_subject(
        db,
        subject_id
    )

    if deleted is None:
        raise SubjectNotFoundException()

    logger.info(
        f"Subject {subject_id} deleted successfully."
    )

    return deleted