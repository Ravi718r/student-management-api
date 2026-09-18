from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.exceptions import (
    StudentNotFoundException,
    AttendanceAlreadyMarkedException
    )

from app.models.attendance import AttendanceStatus


def create_attendance(
        db: Session,
        attendance: schemas.AttendanceCreate
):
    existing = crud.get_attendance_by_student_and_date(
        db,
        attendance.student_id,
        attendance.date
    )

    if existing:
        raise AttendanceAlreadyMarkedException()
    
    
    student = crud.get_student(
        db,
        attendance.student_id
    )

    if student is None:
        raise StudentNotFoundException()
    
    return crud.create_attendance(
        db,
        attendance
    )



def get_all_attendance(
        db: Session
):
    return crud.get_all_attendance(db)



def get_attendance(
        db: Session,
        attendance_id: int
):
    return crud.get_attendance(
        db,
        attendance_id
    )


def update_attendance(
        db: Session,
        attendance_id: int,
        update_attendance: schemas.AttendanceUpdate
):
    return crud.update_attendance(
        db,
        attendance_id,
        update_attendance
    )


def delete_attendance(
        db: Session,
        attendance_id: int
):
    return crud.delete_attendance(
        db,
        attendance_id
    )


def get_student_attendance(
    db: Session,
    student_id: int
):
    return crud.get_student_attendance(
        db,
        student_id
    )


def get_attendance_percentage(
    db: Session,
    student_id: int
):
    student = crud.get_student(
        db,
        student_id
    )

    if student is None:
        raise StudentNotFoundException()

    total = crud.get_total_attendance(
        db,
        student_id
    )

    present = crud.get_present_attendance(
        db,
        student_id
    )

    if total == 0:
        percentage = 0
    else:
        percentage = round(
            (present / total) * 100,
            2
        )

    return {
        "student_id": student_id,
        "total_classes": total,
        "present": present,
        "attendance_percentage": percentage
    }


def get_monthly_report(
    db: Session,
    student_id: int,
    month: int,
    year: int
):
    student = crud.get_student(
        db,
        student_id
    )

    if student is None:
        raise StudentNotFoundException()

    attendance = crud.get_monthly_attendance(
        db,
        student_id,
        month,
        year
    )

    total = len(attendance)

    present = sum(
        1 for a in attendance
        if a.status == AttendanceStatus.PRESENT
    )

    absent = sum(
        1 for a in attendance
        if a.status == AttendanceStatus.ABSENT
    )

    late = sum(
        1 for a in attendance
        if a.status == AttendanceStatus.LATE
    )

    leave = sum(
        1 for a in attendance
        if a.status == AttendanceStatus.LEAVE
    )

    percentage = 0

    if total > 0:
        percentage = round(
            (present / total) * 100,
            2
        )

    return {
        "student_id": student_id,
        "month": month,
        "year": year,
        "total_classes": total,
        "present": present,
        "absent": absent,
        "late": late,
        "leave": leave,
        "attendance_percentage": percentage
    }


def attendance_dashboard(
        db: Session
):
    return crud.attendance_dashboard(db)