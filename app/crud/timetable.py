from sqlalchemy.orm import Session
from sqlalchemy import and_

from app import models
from app.crud.base import BaseCRUD

timetable_crud = BaseCRUD(models.Timetable)


def create_timetable(db: Session, timetable):
    return timetable_crud.create(db, timetable)


def get_timetable(db: Session, timetable_id: int):
    return timetable_crud.get(db, timetable_id)


def get_timetables(db: Session):
    return timetable_crud.get_all(db)


def update_timetable(db: Session, timetable, updated):
    return timetable_crud.update(db, timetable, updated)


def delete_timetable(db: Session, timetable):
    return timetable_crud.delete(db, timetable)


def get_by_course(db: Session, course_id: int):
    return (
        db.query(models.Timetable)
        .filter(models.Timetable.course_id == course_id)
        .all()
    )


def get_by_faculty(db: Session, faculty_id: int):
    return (
        db.query(models.Timetable)
        .filter(models.Timetable.faculty_id == faculty_id)
        .all()
    )


def faculty_time_conflict(
    db: Session,
    faculty_id: int,
    day_of_week: str,
    start_time,
    end_time,
):
    return (
        db.query(models.Timetable)
        .filter(
            models.Timetable.faculty_id == faculty_id,
            models.Timetable.day_of_week == day_of_week,
            models.Timetable.start_time < end_time,
            models.Timetable.end_time > start_time,
        )
        .first()
    )

def room_time_conflict(
    db: Session,
    room_number: str,
    day_of_week: str,
    start_time,
    end_time,
):
    return (
        db.query(models.Timetable)
        .filter(
            models.Timetable.room_number == room_number,
            models.Timetable.day_of_week == day_of_week,
            models.Timetable.start_time < end_time,
            models.Timetable.end_time > start_time,
        )
        .first()
    )



def duplicate_timetable(
    db: Session,
    course_id: int,
    subject_id: int,
    faculty_id: int,
    day_of_week: str,
    start_time,
    end_time,
    room_number: str,
    section: str,
):
    return (
        db.query(models.Timetable)
        .filter(
            models.Timetable.course_id == course_id,
            models.Timetable.subject_id == subject_id,
            models.Timetable.faculty_id == faculty_id,
            models.Timetable.day_of_week == day_of_week,
            models.Timetable.start_time == start_time,
            models.Timetable.end_time == end_time,
            models.Timetable.room_number == room_number,
            models.Timetable.section == section,
        )
        .first()
    )


def faculty_matches_course_department(
    db: Session,
    faculty_id: int,
    course_id: int,
):
    faculty = (
        db.query(models.Faculty)
        .filter(models.Faculty.id == faculty_id)
        .first()
    )

    course = (
        db.query(models.Course)
        .filter(models.Course.id == course_id)
        .first()
    )

    if not faculty or not course:
        return False

    return faculty.department_id == course.department_id