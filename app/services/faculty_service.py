from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.exceptions import (
    FacultyNotFoundException,
    FacultyEmployeeIdAlreadyExistsException,
    FacultyEmailAlreadyExistsException,
    FacultyPhoneAlreadyExistsException,
    DepartmentNotFoundException
)

import logging

logger = logging.getLogger(__name__)


# =====================================================
# Create Faculty
# =====================================================
def create_faculty(
    db: Session,
    faculty: schemas.FacultyCreate
):

    logger.info(
        f"Creating Faculty {faculty.employee_id}"
    )

    existing_employee = crud.get_faculty_by_employee_id(
        db,
        faculty.employee_id
    )

    if existing_employee:
        logger.warning(
            f"Employee ID {faculty.employee_id} already exists."
        )
        raise FacultyEmployeeIdAlreadyExistsException()

    existing_email = crud.get_faculty_by_email(
        db,
        faculty.email
    )

    if existing_email:
        logger.warning(
            f"Email {faculty.email} already exists."
        )
        raise FacultyEmailAlreadyExistsException()

    existing_phone = crud.get_faculty_by_phone(
        db,
        faculty.phone
    )

    if existing_phone:
        logger.warning(
            f"Phone {faculty.phone} already exists."
        )
        raise FacultyPhoneAlreadyExistsException()

    department = crud.get_department(
        db,
        faculty.department_id
    )

    if department is None:
        logger.warning(
            f"Department {faculty.department_id} not found."
        )
        raise DepartmentNotFoundException()

    new_faculty = crud.create_faculty(
        db,
        faculty
    )

    logger.info(
        f"Faculty {new_faculty.employee_id} created successfully."
    )

    return new_faculty


# =====================================================
# Get Faculty By ID
# =====================================================
def get_faculty(
    db: Session,
    faculty_id: int
):

    logger.info(
        f"Fetching Faculty {faculty_id}"
    )

    faculty = crud.get_faculty(
        db,
        faculty_id
    )

    if faculty is None:
        logger.warning(
            f"Faculty {faculty_id} not found."
        )
        raise FacultyNotFoundException()

    return faculty


# =====================================================
# Get All Faculty
# =====================================================
def get_faculties(
    db: Session
):

    logger.info(
        "Fetching all faculty."
    )

    return crud.get_faculties(db)


# =====================================================
# Update Faculty
# =====================================================
def update_faculty(
    faculty_id: int,
    updated_faculty: schemas.FacultyUpdate,
    db: Session
):

    logger.info(
        f"Updating Faculty {faculty_id}"
    )

    faculty = crud.get_faculty(
        db,
        faculty_id
    )

    if faculty is None:
        logger.warning(
            f"Faculty {faculty_id} not found."
        )
        raise FacultyNotFoundException()

    if updated_faculty.department_id is not None:

        department = crud.get_department(
            db,
            updated_faculty.department_id
        )

        if department is None:
            logger.warning(
                f"Department {updated_faculty.department_id} not found."
            )
            raise DepartmentNotFoundException()

    if (
        updated_faculty.employee_id
        and
        updated_faculty.employee_id != faculty.employee_id
    ):

        existing = crud.get_faculty_by_employee_id(
            db,
            updated_faculty.employee_id
        )

        if existing:
            raise FacultyEmployeeIdAlreadyExistsException()

    if (
        updated_faculty.email
        and
        updated_faculty.email != faculty.email
    ):

        existing = crud.get_faculty_by_email(
            db,
            updated_faculty.email
        )

        if existing:
            raise FacultyEmailAlreadyExistsException()

    if (
        updated_faculty.phone
        and
        updated_faculty.phone != faculty.phone
    ):

        existing = crud.get_faculty_by_phone(
            db,
            updated_faculty.phone
        )

        if existing:
            raise FacultyPhoneAlreadyExistsException()

    updated = crud.update_faculty(
        db,
        faculty,
        updated_faculty
    )

    logger.info(
        f"Faculty {faculty_id} updated successfully."
    )

    return updated


# =====================================================
# Delete Faculty
# =====================================================
def delete_faculty(
    faculty_id: int,
    db: Session
):

    logger.info(
        f"Deleting Faculty {faculty_id}"
    )

    faculty = crud.get_faculty(
        db,
        faculty_id
    )

    if faculty is None:
        logger.warning(
            f"Faculty {faculty_id} not found."
        )
        raise FacultyNotFoundException()

    crud.delete_faculty(
        db,
        faculty
    )

    logger.info(
        f"Faculty {faculty_id} deleted successfully."
    )

    return faculty


# =====================================================
# Get Faculty By Department
# =====================================================
def get_faculty_by_department(
    db: Session,
    department_id: int
):

    logger.info(
        f"Fetching faculty for department {department_id}"
    )

    department = crud.get_department(
        db,
        department_id
    )

    if department is None:
        raise DepartmentNotFoundException()

    return crud.get_faculty_by_department(
        db,
        department_id
    )