from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from fastapi import Depends
from app.crud.base import BaseCRUD

import app.models
import app.schemas
import app.auth 


student_crud = BaseCRUD(
    app.models.Student
)

# =====================================================
# Get Student By ID
# =====================================================
def get_student(
    db: Session,
    student_id: int
):
    return student_crud.get(
        db,
        student_id
    )  


# =====================================================
# Get All Students
# =====================================================
def get_students(
    db: Session
):
    return student_crud.get_all(
        db
    )


# =====================================================
# Create Student
# =====================================================
def create_student(
    db: Session,
    student: app.schemas.StudentCreate
):
    return student_crud.create(
        db,
        student
    )


# =====================================================
# Update Student
# =====================================================
def update_student(
    db: Session,
    student_id: int,
    updated_student: app.schemas.StudentCreate
):
    student = get_student(
        db,
        student_id
    )

    return student_crud.update(
        db,
        student,
        updated_student
    )

# =====================================================
# Delete Student
# =====================================================
def delete_student(
    db: Session,
    student_id: int
):
    student = get_student(
        db,
        student_id
    )

    if student is None:
        return None

    return student_crud.delete(
        db,
        student
    )

# -----------------------------
# Get Student By ID
# -----------------------------
# def get_student(db: Session, student_id: int):

#     return db.query(app.models.Student).filter(
#         app.models.Student.id == student_id
#     ).first()


# =====================================================
# SEARCH BY NAME
# =====================================================

def search_student(
    db: Session,
    name: str
):
    return db.query(app.models.Student).filter(
        app.models.Student.name.ilike(f"%{name}%")
    ).all()


# =====================================================
# FILTER BY AGE
# =====================================================

def filter_by_age(
    db: Session,
    age: int
):
    return db.query(app.models.Student).filter(
        app.models.Student.age == age
    ).all()


# =====================================================
# FILTER BY BRANCH
# =====================================================

# def filter_by_branch(
#     db: Session,
#     branch: str
# ):
#     return db.query(app.models.Student).filter(
#         app.models.Student.branch.ilike(branch)
#     ).all()


# =====================================================
# SORT STUDENTS
# =====================================================

def sort_students(
    db: Session,
    order: str
):

    if order.lower() == "desc":

        return db.query(app.models.Student).order_by(
            desc(app.models.Student.age)
        ).all()

    return db.query(app.models.Student).order_by(
        asc(app.models.Student.age)
    ).all()

# =====================================================
# Filter By Course
# =====================================================
def filter_by_course(
    db: Session,
    course_id: int
):
    return (
        db.query(app.models.Student)
        .filter(
            app.models.Student.course_id == course_id
        )
        .all()
    )



# =====================================================
# PAGINATION
# =====================================================

def paginate_students(
    db: Session,
    page: int,
    limit: int
):

    skip = (page - 1) * limit

    return db.query(app.models.Student).offset(
        skip
    ).limit(limit).all()


# -----------------------------
# Create Student
# -----------------------------
# def create_student(
#         db: Session, 
#         student: app.schemas.StudentCreate
#         ):

#     new_student = app.models.Student(
#         **student.model_dump()
#     )

#     db.add(new_student)
#     db.commit()
#     db.refresh(new_student)

#     return new_student


# # -----------------------------
# # Update Student
# # -----------------------------
# def update_student(
#     db: Session,
#     student_id: int,
#     updated_student: app.schemas.StudentCreate
# ):

#     student = get_student(db, student_id)

#     if student is None:
#         return None

#     student.name = updated_student.name
#     student.age = updated_student.age
#     student.branch = updated_student.branch

#     db.commit()
#     db.refresh(student)

#     return student


# # -----------------------------
# # Delete Student
# # -----------------------------
# def delete_student(db: Session, student_id: int):

#     student = get_student(db, student_id)

#     if student is None:
#         return None

#     db.delete(student)
#     db.commit()

#     return student

