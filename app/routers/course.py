from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import schemas
from app.dependencies import get_db
from app.auth import get_current_user, admin_required
from app.services import course_service


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


# ==========================================
# Get All Courses
# ==========================================
@router.get(
    "/",
    response_model=list[schemas.CourseResponse],
    status_code=status.HTTP_200_OK
)
def get_courses(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return course_service.get_courses(db)


# ==========================================
# Get Course By ID
# ==========================================
@router.get(
    "/{course_id}",
    response_model=schemas.CourseResponse
)
def get_course(
    course_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return course_service.get_course(
        db,
        course_id
    )


# ==========================================
# Create Course
# ==========================================
@router.post(
    "/",
    response_model=schemas.CourseResponse,
    status_code=status.HTTP_201_CREATED
)
def create_course(
    course: schemas.CourseCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return course_service.create_course(
        db,
        course
    )


# ==========================================
# Update Course
# ==========================================
@router.put(
    "/{course_id}",
    response_model=schemas.CourseResponse
)
def update_course(
    course_id: int,
    updated_course: schemas.CourseUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return course_service.update_course(
        db,
        course_id,
        updated_course
    )


# ==========================================
# Delete Course
# ==========================================
@router.delete(
    "/{course_id}",
    status_code=status.HTTP_200_OK
)
def delete_course(
    course_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    course_service.delete_course(
        db,
        course_id
    )

    return {
        "message": "Course deleted successfully."
    }