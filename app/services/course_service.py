from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.exceptions import (
    DepartmentNotFoundException,
    CourseNotFoundException,
    CourseAlreadyExistsException
)

import logging

logger = logging.getLogger(__name__)


# ==========================================
# Create Course
# ==========================================
def create_course(
    db: Session,
    course: schemas.CourseCreate
):
    logger.info(f"Creating course {course.code}")

    # Check if course code already exists
    existing = crud.get_course_by_code(
        db,
        course.code
    )

    if existing:
        logger.warning(
            f"Course code {course.code} already exists."
        )
        raise CourseAlreadyExistsException()

    # Check department
    department = crud.get_department(
        db,
        course.department_id
    )

    if department is None:
        logger.warning(
            f"Department {course.department_id} not found."
        )
        raise DepartmentNotFoundException()

    new_course = crud.create_course(
        db,
        course
    )

    logger.info(
        f"Course {new_course.code} created successfully."
    )

    return new_course


# ==========================================
# Get All Courses
# ==========================================
def get_courses(
    db: Session
):
    logger.info("Fetching all courses")
    return crud.get_courses(db)


# ==========================================
# Get Course By ID
# ==========================================
def get_course(
    db: Session,
    course_id: int
):
    logger.info(
        f"Fetching course {course_id}"
    )

    course = crud.get_course(
        db,
        course_id
    )

    if course is None:
        logger.warning(
            f"Course {course_id} not found."
        )
        raise CourseNotFoundException()

    return course


# ==========================================
# Update Course
# ==========================================
def update_course(
    db: Session,
    course_id: int,
    updated_course: schemas.CourseUpdate
):
    logger.info(
        f"Updating course {course_id}"
    )

    course = crud.get_course(
        db,
        course_id
    )

    if course is None:
        raise CourseNotFoundException()

    department = crud.get_department(
        db,
        updated_course.department_id
    )

    if department is None:
        raise DepartmentNotFoundException()

    updated = crud.update_course(
        db,
        course_id,
        updated_course
    )

    logger.info(
        f"Course {course_id} updated successfully."
    )

    return updated


# ==========================================
# Delete Course
# ==========================================
def delete_course(
    db: Session,
    course_id: int
):
    logger.info(
        f"Deleting course {course_id}"
    )

    deleted = crud.delete_course(
        db,
        course_id
    )

    if deleted is None:
        raise CourseNotFoundException()

    logger.info(
        f"Course {course_id} deleted successfully."
    )

    return deleted