from sqlalchemy.orm import Session

from app import models
from app.crud.base import BaseCRUD

faculty_subject_crud = BaseCRUD(models.FacultySubject)


def create_faculty_subject(db: Session, faculty_subject):
    return faculty_subject_crud.create(db, faculty_subject)


def get_faculty_subject(db: Session, faculty_subject_id: int):
    return faculty_subject_crud.get(db, faculty_subject_id)


def get_faculty_subjects(db: Session):
    return faculty_subject_crud.get_all(db)


def delete_faculty_subject(db: Session, faculty_subject):
    return faculty_subject_crud.delete(db, faculty_subject)


def get_by_faculty_subject(db: Session, faculty_id: int, subject_id: int):
    return (
        db.query(models.FacultySubject)
        .filter(
            models.FacultySubject.faculty_id == faculty_id,
            models.FacultySubject.subject_id == subject_id,
        )
        .first()
    )


def get_by_faculty(db: Session, faculty_id: int):
    return (
        db.query(models.FacultySubject)
        .filter(models.FacultySubject.faculty_id == faculty_id)
        .all()
    )


def get_by_subject(db: Session, subject_id: int):
    return (
        db.query(models.FacultySubject)
        .filter(models.FacultySubject.subject_id == subject_id)
        .all()
    )


def is_faculty_assigned_to_subject(
    db: Session,
    faculty_id: int,
    subject_id: int,
):
    return (
        db.query(models.FacultySubject)
        .filter(
            models.FacultySubject.faculty_id == faculty_id,
            models.FacultySubject.subject_id == subject_id,
        )
        .first()
    )