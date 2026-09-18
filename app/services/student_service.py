from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.exceptions import(
    StudentAlreadyExistsException,
    DepartmentNotFoundException,
    StudentNotFoundException
)

import logging
logger = logging.getLogger(__name__)


# =====================================================
# Create Student Service
# =====================================================
def create_student(
        db: Session,
        student: schemas.StudentCreate
):
    logger.info(
        f"Creating student {student.id}"
    )

    existing_student = crud.get_student(
        db,
        student.id
    )

    if existing_student: 
        logger.warning(
            f"Student ID {student.id} already exists"
        )
        raise StudentAlreadyExistsException()
    
    department = crud.get_department(
        db,
        student.department_id
    )

    if department is None:
        logger.warning(
            f"Department {student.department_id} not found"
        )
        raise DepartmentNotFoundException() 

    new_student = crud.create_student(db,student )

    logger.info(
        f"Student {new_student.id} created successfully"
    )

    return new_student


# =====================================================
# Get Student By ID Service
# =====================================================
def get_student(
       db: Session,
       student_id: int 
):
    logger.info(f"Fetching student {student_id}")

    student = crud.get_student(db, student_id)

    if student is None:
        logger.warning(
            f"Student ID {student_id} not found"
        )
        raise StudentNotFoundException()
    
    return student


# =====================================================
# Get All Student Service
# =====================================================
def get_students(
    db: Session
):
    logger.info("Fetching all students")
    return crud.get_students(db)


# =====================================================
# Serch Student Service
# =====================================================
def search_student(
        db: Session,
        name: str
):
    logger.info(
        f"Searching students with name={name}"
    )

    return crud.search_student(
        db,
        name
    )


# =====================================================
# Filter By Age Service
# =====================================================
def filter_by_age(
        db: Session,
        age: int
):
    logger.info(
        f"Filtering students are={age}"
    )

    return crud.filter_by_age(
        db, 
        age
    )


# =====================================================
# Filter By Branch Service
# =====================================================
def filter_by_branch(
        db: Session,
        branch: str
):
    logger.info(
        f"Filtering students are={branch}"
    )

    return crud.filter_by_branch(
        db, 
        branch
    )

# =====================================================
# Sort Student Service
# =====================================================
def sort_students(
        db: Session,
        order: str = "asc"
):
    logger.info(
        f"Sorting students in {order} order"
    )

    return crud.sort_students(
        db, 
        order
    )


# =====================================================
# Pagination Service
# =====================================================
def paginate_students(
        db : Session,
        page: int = 1,
        limit: int = 5
):
    logger.info(
        f"Pagination page={page} limit={limit}"
    )

    return crud.paginate_students(
        db, 
        page,
        limit
    )


# =====================================================
# Delete Student
# =====================================================
def delete_student(
    student_id: int,
    db: Session 
):

    logger.info(
        f"Deleting student {student_id}"
    )

    student = crud.delete_student(
        db,
        student_id
    )

    if student is None:
        logger.warning(
            f"Student {student_id} not found"
        )
        raise StudentNotFoundException()

    logger.info(
        f"Student {student_id} deleted successfully"
    )

    return student


# =====================================================
# Update Student
# =====================================================
def update_student(
    student_id: int,
    updated_student: schemas.StudentCreate,
    db: Session
):
    logger.info(
        f"Updating student ID {student_id}"
    )

    student = crud.get_student(
        db,
        student_id
    )

    if student is None:
        logger.warning(
            f"Student ID {student.id} not found."
        )
        raise StudentNotFoundException()
    
    #check if department exists
    department = crud.get_department(
        db,
        updated_student.department_id
    )

    if department is None:
        logger.warning(
            f"Department ID {updated_student.department_id} not found"
        )
        raise DepartmentNotFoundException()
    
    updated= crud.update_student(
        db,
        student_id,
        updated_student
    )
    logger.info(
        f"Student ID {student_id} updated successfully"
    )

    return updated