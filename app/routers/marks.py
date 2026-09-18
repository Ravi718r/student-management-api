from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db
from app import schemas
from app.services import marks_service

from app.auth import (
    get_current_user,
    admin_required
)

router = APIRouter(
    prefix="/marks",
    tags=["Marks"]
)


# ==========================================
# Get All Marks
# ==========================================
@router.get(
    "/",
    response_model=list[schemas.MarksResponse]
)
def get_marks(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return marks_service.get_marks(db)


# ==========================================
# Get Marks By ID
# ==========================================
@router.get(
    "/{mark_id}",
    response_model=schemas.MarksResponse
)
def get_mark(
    mark_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return marks_service.get_mark(
        db,
        mark_id
    )


# ==========================================
# Create Marks
# ==========================================
@router.post(
    "/",
    response_model=schemas.MarksResponse
)
def create_mark(
    mark: schemas.MarksCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return marks_service.create_mark(
        db,
        mark
    )


# ==========================================
# Update Marks
# ==========================================
@router.put(
    "/{mark_id}",
    response_model=schemas.MarksResponse
)
def update_mark(
    mark_id: int,
    updated_mark: schemas.MarksUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return marks_service.update_mark(
        db,
        mark_id,
        updated_mark
    )


# ==========================================
# Delete Marks
# ==========================================
@router.delete(
    "/{mark_id}",
    response_model=schemas.SuccessResponse
)
def delete_mark(
    mark_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    marks_service.delete_mark(
        db,
        mark_id
    )

    return {
        "message": "Marks deleted successfully."
    }