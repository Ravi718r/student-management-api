from sqlalchemy.orm import Session

import app.models
import app.schemas

from app.models import subject
from app import models

from app.crud.base import BaseCRUD


subject_crud = BaseCRUD(app.models.Subject)


# ==========================================
# Get All Subjects
# ==========================================
def get_subjects(
    db: Session
):
    return subject_crud.get_all(db)


# ==========================================
# Get Subject By ID
# ==========================================
def get_subject(
    db: Session,
    subject_id: int
):
    return subject_crud.get(
        db,
        subject_id
    )


# ==========================================
# Create Subject
# ==========================================
def create_subject(
    db: Session,
    subject: app.schemas.SubjectCreate
):
    return subject_crud.create(
        db,
        subject
    )


# ==========================================
# Update Subject
# ==========================================
def update_subject(
    db: Session,
    subject_id: int,
    updated_subject: app.schemas.SubjectUpdate
):
    subject = get_subject(
        db,
        subject_id
    )

    if subject is None:
        return None

    return subject_crud.update(
        db,
        subject,
        updated_subject
    )


# ==========================================
# Delete Subject
# ==========================================
def delete_subject(
    db: Session,
    subject_id: int
):
    subject = get_subject(
        db,
        subject_id
    )

    if subject is None:
        return None

    return subject_crud.delete(
        db,
        subject
    )


# ==========================================
# Get Subject By Code
# ==========================================
def get_subject_by_code(
    db: Session,
    code: str
):
    return (
        db.query(app.models.Subject)
        .filter(
            app.models.Subject.code == code
        )
        .first()
    )


def subject_belongs_to_course(
    db: Session,
    subject_id: int,
    course_id: int,
):
    return (
        db.query(models.Subject)
        .filter(
            models.Subject.id == subject_id,
            models.Subject.course_id == course_id,
        )
        .first()
    )