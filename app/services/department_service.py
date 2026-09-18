import logging

from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.exceptions import (
    DepartmentNotFoundException,
    DepartmentAlreadyExistsException
)

logger = logging.getLogger(__name__)


# =====================================================
# Get All Departments
# =====================================================
def get_departments(
    db: Session
):
    logger.info("Fetching all departments")

    return crud.get_departments(db)


# =====================================================
# Get Department By ID
# =====================================================
def get_department(
    db: Session,
    department_id: int
):
    logger.info(
        f"Fetching department ID {department_id}"
    )

    department = crud.get_department(
        db,
        department_id
    )

    if department is None:
        logger.warning(
            f"Department ID {department_id} not found"
        )
        raise DepartmentNotFoundException()

    return department


# =====================================================
# Create Department
# =====================================================
def create_department(
    db: Session,
    department: schemas.DepartmentCreate
):
    logger.info(
        f"Creating department {department.code}"
    )

    existing_department = crud.get_department_by_code(
        db,
        department.code
    )

    if existing_department:
        logger.warning(
            f"Department code {department.code} already exists"
        )
        raise DepartmentAlreadyExistsException()

    created_department = crud.create_department(
        db,
        department
    )

    logger.info(
        f"Department {created_department.code} created successfully"
    )

    return created_department


# =====================================================
# Update Department
# =====================================================
def update_department(
    db: Session,
    department_id: int,
    updated_department: schemas.DepartmentCreate
):
    logger.info(
        f"Updating department ID {department_id}"
    )

    department = crud.get_department(
        db,
        department_id
    )

    if department is None:
        logger.warning(
            f"Department ID {department_id} not found"
        )
        raise DepartmentNotFoundException()

    existing_department = crud.get_department_by_code(
        db,
        updated_department.code
    )

    if (
        existing_department
        and existing_department.id != department_id
    ):
        logger.warning(
            f"Department code {updated_department.code} already exists"
        )
        raise DepartmentAlreadyExistsException()

    updated = crud.update_department(
        db,
        department_id,
        updated_department
    )

    logger.info(
        f"Department ID {department_id} updated successfully"
    )

    return updated


# =====================================================
# Delete Department
# =====================================================
def delete_department(
    db: Session,
    department_id: int
):
    logger.info(
        f"Deleting department ID {department_id}"
    )

    department = crud.delete_department(
        db,
        department_id
    )

    if department is None:
        logger.warning(
            f"Department ID {department_id} not found"
        )
        raise DepartmentNotFoundException()

    logger.info(
        f"Department ID {department_id} deleted successfully"
    )

    return department