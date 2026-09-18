from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.auth import get_current_user

from app.services import result_service
from app.schemas import StudentResultResponse


router = APIRouter(
    prefix="/results",
    tags=["Results"]
)


# =====================================================
# Student Result
# =====================================================
@router.get(
    "/student/{student_id}",
    response_model=StudentResultResponse
)
def get_student_result(
    student_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return result_service.get_student_result(
        db,
        student_id
    )