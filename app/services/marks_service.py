from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.exceptions import (
    EnrollmentNotFoundException,
    MarksNotFoundException,
    MarksAlreadyExistsException
)

import logging
import app.models

logger = logging.getLogger(__name__)


# ==========================================
# Grade Calculator
# ==========================================
def calculate_grade(total: float):

    if total >= 90:
        return "A+"
    elif total >= 80:
        return "A"
    elif total >= 70:
        return "B"
    elif total >= 60:
        return "C"
    elif total >= 50:
        return "D"
    elif total >= 40:
        return "E"

    return "F"


# ==========================================
# Result Calculator
# ==========================================
def calculate_result(total: float):

    if total >= 40:
        return "PASS"

    return "FAIL"


# ==========================================
# Create Marks
# ==========================================
def create_mark(
    db: Session,
    mark: schemas.MarksCreate
):

    logger.info(
        f"Creating marks for enrollment {mark.enrollment_id}"
    )

    enrollment = crud.get_enrollment(
        db,
        mark.enrollment_id
    )

    if enrollment is None:
        raise EnrollmentNotFoundException()

    existing = crud.get_marks_by_enrollment(
        db,
        mark.enrollment_id
    )

    if existing:
        raise MarksAlreadyExistsException()

    total = (
        mark.internal_marks
        + mark.external_marks
        + mark.practical_marks
    )

    grade = calculate_grade(total)

    result = calculate_result(total)

    mark_data = schemas.MarksCreate(
        enrollment_id=mark.enrollment_id,
        internal_marks=mark.internal_marks,
        external_marks=mark.external_marks,
        practical_marks=mark.practical_marks
    )

    db_mark = app.models.Marks(
        enrollment_id=mark.enrollment_id,
        internal_marks=mark.internal_marks,
        external_marks=mark.external_marks,
        practical_marks=mark.practical_marks,
        total_marks=total,
        grade=grade,
        result=result
    )

    db.add(db_mark)

    db.commit()

    db.refresh(db_mark)

    logger.info(
        f"Marks created successfully for enrollment {mark.enrollment_id}"
    )
    return db_mark

    

# ==========================================
# Get All Marks
# ==========================================
def get_marks(
    db: Session
):
    return crud.get_marks(db)


# ==========================================
# Get Mark By ID
# ==========================================
def get_mark(
    db: Session,
    mark_id: int
):

    mark = crud.get_mark(
        db,
        mark_id
    )

    if mark is None:
        raise MarksNotFoundException()

    return mark


# ==========================================
# Update Marks
# ==========================================
def update_mark(
    db: Session,
    mark_id: int,
    updated_mark: schemas.MarksUpdate
):

    mark = crud.get_mark(
        db,
        mark_id
    )

    if mark is None:
        raise MarksNotFoundException()

    total = (
        updated_mark.internal_marks
        + updated_mark.external_marks
        + updated_mark.practical_marks
    )

    grade = calculate_grade(total)

    result = calculate_result(total)

    mark.internal_marks = updated_mark.internal_marks
    mark.external_marks = updated_mark.external_marks
    mark.practical_marks = updated_mark.practical_marks

    mark.total_marks = total
    mark.grade = grade
    mark.result = result

    db.commit()
    db.refresh(mark)

    logger.info(
        f"Marks {mark_id} updated successfully."
    )

    return mark


# ==========================================
# Delete Marks
# ==========================================
def delete_mark(
    db: Session,
    mark_id: int
):

    deleted = crud.delete_mark(
        db,
        mark_id
    )

    if deleted is None:
        raise MarksNotFoundException()

    logger.info(
        f"Marks {mark_id} deleted successfully."
    )

    return deleted
    return deleted