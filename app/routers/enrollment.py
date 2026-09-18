from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import schemas
from app.dependencies import get_db
from app.auth import get_current_user, admin_required
from app.services import enrollment_service


router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)


# ==========================================
# Get All Enrollments
# ==========================================
@router.get(
    "/",
    response_model=list[schemas.EnrollmentResponse],
    status_code=status.HTTP_200_OK
)
def get_enrollments(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return enrollment_service.get_enrollments(db)


# ==========================================
# Get Enrollment By ID
# ==========================================
@router.get(
    "/{enrollment_id}",
    response_model=schemas.EnrollmentResponse,
    status_code=status.HTTP_200_OK
)
def get_enrollment(
    enrollment_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return enrollment_service.get_enrollment(
        db,
        enrollment_id
    )


# ==========================================
# Create Enrollment
# ==========================================
@router.post(
    "/",
    response_model=schemas.EnrollmentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_enrollment(
    enrollment: schemas.EnrollmentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return enrollment_service.create_enrollment(
        db,
        enrollment
    )


# ==========================================
# Delete Enrollment
# ==========================================
@router.delete(
    "/{enrollment_id}",
    response_model=schemas.EnrollmentResponse,
    status_code=status.HTTP_200_OK
)
def delete_enrollment(
    enrollment_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return enrollment_service.delete_enrollment(
        db,
        enrollment_id
    )