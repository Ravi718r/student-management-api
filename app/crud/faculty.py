from sqlalchemy.orm import Session

from app import models
from app.crud.base import BaseCRUD


# =====================================================
# Base CRUD
# =====================================================

faculty_crud = BaseCRUD(models.Faculty)


# =====================================================
# Get Faculty By ID
# =====================================================

def get_faculty(
    db: Session,
    faculty_id: int
):
    return faculty_crud.get(
        db,
        faculty_id
    )


# =====================================================
# Get All Faculty
# =====================================================

def get_faculties(
    db: Session
):
    return faculty_crud.get_all(
        db
    )


# =====================================================
# Create Faculty
# =====================================================

def create_faculty(
    db: Session,
    faculty
):
    return faculty_crud.create(
        db,
        faculty
    )


# =====================================================
# Update Faculty
# =====================================================

def update_faculty(
    db: Session,
    db_faculty,
    faculty
):
    return faculty_crud.update(
        db,
        db_faculty,
        faculty
    )


# =====================================================
# Delete Faculty
# =====================================================

def delete_faculty(
    db: Session,
    db_faculty
):
    return faculty_crud.delete(
        db,
        db_faculty
    )


# =====================================================
# Get Faculty By Employee ID
# =====================================================

def get_faculty_by_employee_id(
    db: Session,
    employee_id: str
):
    return (
        db.query(models.Faculty)
        .filter(
            models.Faculty.employee_id == employee_id
        )
        .first()
    )


# =====================================================
# Get Faculty By Email
# =====================================================

def get_faculty_by_email(
    db: Session,
    email: str
):
    return (
        db.query(models.Faculty)
        .filter(
            models.Faculty.email == email
        )
        .first()
    )


# =====================================================
# Get Faculty By Phone
# =====================================================

def get_faculty_by_phone(
    db: Session,
    phone: str
):
    return (
        db.query(models.Faculty)
        .filter(
            models.Faculty.phone == phone
        )
        .first()
    )


# =====================================================
# Get Faculty By Department
# =====================================================

def get_faculty_by_department(
    db: Session,
    department_id: int
):
    return (
        db.query(models.Faculty)
        .filter(
            models.Faculty.department_id == department_id
        )
        .all()
    )