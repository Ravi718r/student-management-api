from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import schemas
from app.dependencies import get_db
from app.auth import get_current_user, admin_required
from app.services import attendance_service

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


# Get All Dependencies
@router.get(
    "/",
    response_model=list[schemas.AttendanceResponse],
    status_code=status.HTTP_200_OK
)
def get_all_attendance(
        db: Session = Depends(get_db),
        current_user= Depends(get_current_user)
):
    return attendance_service.get_all_attendance(db)




# Create Attendance
@router.post(
    "/",
    response_model=schemas.AttendanceResponse,
    status_code=status.HTTP_201_CREATED
)
def create_attendance(
    attendance: schemas.AttendanceCreate,
    db:Session= Depends(get_db),
    current_user = Depends(admin_required)
):
    return attendance_service.create_attendance(
        db,
        attendance
    )



# Get Attendance BY student
@router.get(
    "/student/{student_id}",
    response_model=list[schemas.AttendanceResponse]
)
def get_student_attendance(
    student_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return attendance_service.get_student_attendance(
        db,student_id
    )


# GEt student attendance percentage
@router.get(
    "/student/{student_id}/percentage"
)
def attendance_percentage(
    student_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return attendance_service.get_attendance_percentage(
        db,
        student_id
    )



@router.get(
    "/student/{student_id}/month/{month}/year/{year}"
)
def monthly_report(
    student_id: int,
    month: int,
    year: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return attendance_service.get_monthly_report(
        db,
        student_id,
        month,
        year
    )


# dashboard 
@router.get(
        "/dashboard"
)
def dashboard(
    db: Session = Depends(get_db),
    cuurent_user = Depends(admin_required)
):
    return attendance_service.attendance_dashboard(db)



# Update Attendance
@router.post(
    "/{attendance_id}",
    response_model=schemas.AttendanceResponse
)
def update_attendance(
    attendance_id: int,
    updated_attendance: schemas.AttendanceUpdate,
    db:Session= Depends(get_db),
    current_user = Depends(admin_required)
):
    return attendance_service.update_attendance(
        db,
        attendance_id,
        update_attendance
    )



# Delete Attendance
@router.delete(
    "/{attendance_id}",
    status_code=status.HTTP_200_OK
)
def delete_attendance(
    attendance_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):
    attendance_service.delete_attendance(
        db,
        attendance_id
    )

    return {
        "message": "Attendance Deleted Successfully."
    }

# Get Attendance By ID
@router.get(
    "/{attendance_id}",
    response_model=schemas.AttendanceResponse,
    status_code=status.HTTP_200_OK
)
def get_attendance(
    attendance_id: int,
    db: Session = Depends(get_db),
    current_user= Depends(get_current_user)
):
    return attendance_service.get_attendance(
        db,
        attendance_id
    )