from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import schemas
from app.dependencies import get_db
from app.auth import get_current_user, admin_required
from app.services import subject_service


router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"]
)


# ==========================================
# Get All Subjects
# ==========================================
@router.get(
    "/",
    response_model=list[schemas.SubjectResponse],
    status_code=status.HTTP_200_OK
)
def get_subjects(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return subject_service.get_subjects(db)


# ==========================================
# Get Subject By ID
# ==========================================
@router.get(
    "/{subject_id}",
    response_model=schemas.SubjectResponse,
    status_code=status.HTTP_200_OK
)
def get_subject(
    subject_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return subject_service.get_subject(
        db,
        subject_id
    )


# ==========================================
# Create Subject
# ==========================================
@router.post(
    "/",
    response_model=schemas.SubjectResponse,
    status_code=status.HTTP_201_CREATED
)
def create_subject(
    subject: schemas.SubjectCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return subject_service.create_subject(
        db,
        subject
    )


# ==========================================
# Update Subject
# ==========================================
@router.put(
    "/{subject_id}",
    response_model=schemas.SubjectResponse,
    status_code=status.HTTP_200_OK
)
def update_subject(
    subject_id: int,
    updated_subject: schemas.SubjectUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return subject_service.update_subject(
        db,
        subject_id,
        updated_subject
    )


# ==========================================
# Delete Subject
# ==========================================
@router.delete(
    "/{subject_id}",
    response_model=schemas.SubjectResponse,
    status_code=status.HTTP_200_OK
)
def delete_subject(
    subject_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return subject_service.delete_subject(
        db,
        subject_id
    )