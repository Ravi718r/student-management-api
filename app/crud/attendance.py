from sqlalchemy.orm import Session

import app.models
import app.schemas

from datetime import date 
from app.crud.base import BaseCRUD

from sqlalchemy import func,extract
from app.models.attendance import AttendanceStatus


attendance_curd = BaseCRUD(
    app.models.Attendance
)


def get_attendance(
        db: Session,
        attendance_id: int
):
    return attendance_curd.get(
        db,
        attendance_id
    )


def get_all_attendance(
        db: Session
):
    return attendance_curd.get_all(db)


def create_attendance(
        db: Session,
        attendance: app.schemas.AttendanceCreate
):
    return attendance_curd.create(
        db,
        attendance
    )


def update_attendance(
        db: Session,
        attendance_id: int,
        update_attendance: app.schemas.AttendanceUpdate
):
    attendance= get_attendance(
        db,
        attendance_id
    )

    return attendance_curd.update(
        db,
        attendance,
        update_attendance
    )

def delete_attendance(
        db: Session,
        attendance_id: int
):
    attendance = get_attendance(
        db,
        attendance_id
    )

    return attendance_curd.delete(
        db,
        attendance
    )


def get_student_attendance(
        db: Session,
        student_id: int
):
    return(
        db.query(app.models.Attendance)
        .filter(
            app.models.Attendance.student_id == student_id
        )
        .all()
    )


def get_attendance_by_student_and_date(
    db: Session,
    student_id: int,
    attendance_date: date
):
    return (
        db.query(app.models.Attendance)
        .filter(
            app.models.Attendance.student_id == student_id,
            app.models.Attendance.date == attendance_date
        )
        .first()
    )


# ==========================================
# Total Attendance Records
# ==========================================
def get_total_attendance(
    db: Session,
    student_id: int
):
    return (
        db.query(app.models.Attendance)
        .filter(
            app.models.Attendance.student_id == student_id
        )
        .count()
    )


# ==========================================
# Present Attendance Count
# ==========================================
def get_present_attendance(
    db: Session,
    student_id: int
):
    return (
        db.query(app.models.Attendance)
        .filter(
            app.models.Attendance.student_id == student_id,
            app.models.Attendance.status == AttendanceStatus.PRESENT
        )
        .count()
    )


# Get Monthly status
def get_monthly_attendance(
    db: Session,
    student_id: int,
    month: int,
    year: int
):
    return (
        db.query(app.models.Attendance)
        .filter(
            app.models.Attendance.student_id == student_id,
            extract("month", app.models.Attendance.date) == month,
            extract("year", app.models.Attendance.date) == year
        )
        .all()
    )


# Dashboard 
def attendance_dashboard(
        db: Session
):
    today = date.today()

    total_students = db.query(
        app.models.Student
    ).count()

    present = db.query(
        app.models.Attendance
    ).filter(
        app.models.Attendance.date == today,

        app.models.Attendance.status == AttendanceStatus.PRESENT
    ).count()

    absent = db.query(
        app.models.Attendance
    ).filter(
        app.models.Attendance.date == today,
        app.models.Attendance.status == AttendanceStatus.ABSENT
    ).count()

    late = db.query(
        app.models.Attendance
    ).filter(
        app.models.Attendance.date == today,
        app.models.Attendance.status == AttendanceStatus.LEAVE
    ).count()

    leave = db.query(
        app.models.Attendance
    ).filter(
        app.models.Attendance.date == today,
        app.models.Attendance.status == AttendanceStatus.LEAVE
    ).count()

    return {
        "total_students": total_students,
        "present_today": present,
        "absent_today": absent,
        "late_today": late,
        "leave_today": leave
    }
