from sqlalchemy.orm import Session

import app.models
import app.schemas

from app.crud.base import BaseCRUD


marks_crud = BaseCRUD(
    app.models.Marks
)


# ==========================================
# Get All
# ==========================================
def get_marks(db: Session):
    return marks_crud.get_all(db)


# ==========================================
# Get By ID
# ==========================================
def get_mark(
    db: Session,
    mark_id: int
):
    return marks_crud.get(
        db,
        mark_id
    )


# ==========================================
# Create
# ==========================================
def create_mark(
    db: Session,
    mark: app.schemas.MarksCreate
):
    return marks_crud.create(
        db,
        mark
    )


# ==========================================
# Update
# ==========================================
def update_mark(
    db: Session,
    mark_id: int,
    updated_mark: app.schemas.MarksUpdate
):

    mark = get_mark(
        db,
        mark_id
    )

    if mark is None:
        return None

    return marks_crud.update(
        db,
        mark,
        updated_mark
    )


# ==========================================
# Delete
# ==========================================
def delete_mark(
    db: Session,
    mark_id: int
):

    mark = get_mark(
        db,
        mark_id
    )

    if mark is None:
        return None

    return marks_crud.delete(
        db,
        mark
    )


# ==========================================
# Check Existing Enrollment
# ==========================================
def get_mark_by_enrollment(
    db: Session,
    enrollment_id: int
):
    return (
        db.query(app.models.Marks)
        .filter(
            app.models.Marks.enrollment_id == enrollment_id
        )
        .first()
    )


# # Calculate Grade 
# def calculate_grade(total):

#     if total >= 90:
#         return "A+"

#     elif total >= 80:
#         return "A"

#     elif total >= 70:
#         return "B"

#     elif total >= 60:
#         return "C"

#     elif total >= 50:
#         return "D"

#     elif total >= 40:
#         return "E"

#     return "F"


# # Result Logic 
# def calculate_result(total):

#     if total >= 40:
#         return "PASS"

#     return "FAIL"