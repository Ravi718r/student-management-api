from sqlalchemy.orm import Session

import app.models
import app.schemas

from app.crud.base import BaseCRUD


course_crud = BaseCRUD(app.models.Course)


# Get all Courses
def get_courses(db: Session):
    return course_crud.get_all(db)


# Get Student By Id 
def get_course(
        db: Session,
        course_id: int 
):
    return course_crud.get(
        db,
        course_id
    )


# Create Course
def create_course(
        db: Session,
        course: app.schemas.CourseCreate
):
    return course_crud.create(
        db,
        course
    )


# Update Course
def update_course(
        db: Session,
        course_id: int,
        updated_course: app.schemas.CourseUpdate
):
    return course_crud.update(
        db,
        course_id,
        updated_course
    )



# Delete Course
def delete_course(
        db: Session,
        course_id: int
):
    return course_crud.delete(
        db,
        course_id
    )


# Get Course By Code
def get_course_by_code(
        db: Session,
        code: str
):
    return (
        db.query(app.models.Course)
        .filter(
            app.models.Course.code == code
        )
        .first()
    )