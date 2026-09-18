from sqlalchemy.orm import Session

import app.models
import app.schemas

from app.crud.base import BaseCRUD


enrollment_crud = BaseCRUD(
    app.models.Enrollment
)


# ==========================================
# Get All
# ==========================================
def get_enrollments(
    db: Session
):
    return enrollment_crud.get_all(db)


# ==========================================
# Get By ID
# ==========================================
def get_enrollment(
    db: Session,
    enrollment_id: int
):
    return enrollment_crud.get(
        db,
        enrollment_id
    )


# ==========================================
# Create
# ==========================================
def create_enrollment(
    db: Session,
    enrollment: app.schemas.EnrollmentCreate
):
    return enrollment_crud.create(
        db,
        enrollment
    )


# ==========================================
# Delete
# ==========================================
def delete_enrollment(
    db: Session,
    enrollment_id: int
):
    enrollment = get_enrollment(
        db,
        enrollment_id
    )

    if enrollment is None:
        return None

    return enrollment_crud.delete(
        db,
        enrollment
    )


# ==========================================
# Check Duplicate Enrollment
# ==========================================
def get_student_subject(
    db: Session,
    student_id: int,
    subject_id: int
):
    return (
        db.query(app.models.Enrollment)
        .filter(
            app.models.Enrollment.student_id == student_id,
            app.models.Enrollment.subject_id == subject_id
        )
        .first()
    )