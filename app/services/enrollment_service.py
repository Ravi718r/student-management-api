from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.exceptions import (
    StudentNotFoundException,
    SubjectNotFoundException,
    EnrollmentNotFoundException,
    EnrollmentAlreadyExistsException
)

import logging

logger = logging.getLogger(__name__)


# ==========================================
# Create Enrollment
# ==========================================
def create_enrollment(
    db: Session,
    enrollment: schemas.EnrollmentCreate
):

    logger.info(
        f"Enrolling Student {enrollment.student_id}"
    )

    student = crud.get_student(
        db,
        enrollment.student_id
    )

    if student is None:
        raise StudentNotFoundException()

    subject = crud.get_subject(
        db,
        enrollment.subject_id
    )

    if subject is None:
        raise SubjectNotFoundException()

    existing = crud.get_student_subject(
        db,
        enrollment.student_id,
        enrollment.subject_id
    )

    if existing:
        raise EnrollmentAlreadyExistsException()

    return crud.create_enrollment(
        db,
        enrollment
    )


# ==========================================
# Get All
# ==========================================
def get_enrollments(
    db: Session
):
    return crud.get_enrollments(db)


# ==========================================
# Get By ID
# ==========================================
def get_enrollment(
    db: Session,
    enrollment_id: int
):

    enrollment = crud.get_enrollment(
        db,
        enrollment_id
    )

    if enrollment is None:
        raise EnrollmentNotFoundException()

    return enrollment


# ==========================================
# Delete
# ==========================================
def delete_enrollment(
    db: Session,
    enrollment_id: int
):

    enrollment = crud.delete_enrollment(
        db,
        enrollment_id
    )

    if enrollment is None:
        raise EnrollmentNotFoundException()

    return enrollment