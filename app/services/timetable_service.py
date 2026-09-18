import logging

from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.exceptions import (
    CourseNotFoundException,
    SubjectNotFoundException,
    FacultyNotFoundException,
    TimetableNotFoundException,
    FacultyTimeConflictException,
    RoomTimeConflictException,
    SubjectCourseMismatchException,
    InvalidTimeRangeException,
    SectionTimeConflictException,
    FacultyDepartmentMismatchException
)
from app.crud.subject import subject_belongs_to_course 

logger = logging.getLogger(__name__)


def create_timetable(db: Session, timetable: schemas.TimetableCreate):

    if not crud.get_course(db, timetable.course_id):
        raise CourseNotFoundException()

    if not crud.get_subject(db, timetable.subject_id):
        raise SubjectNotFoundException()

    if not crud.get_faculty(db, timetable.faculty_id):
        raise FacultyNotFoundException()
    
    conflict = crud.faculty_time_conflict(
        db,
        timetable.faculty_id,
        timetable.day_of_week,
        timetable.start_time,
        timetable.end_time,
    )

    if conflict:
        raise FacultyTimeConflictException()
    

    room_conflict = crud.room_time_conflict(
        db,
        timetable.room_number,
        timetable.day_of_week,
        timetable.start_time,
        timetable.end_time,
    )

    if room_conflict:
        raise RoomTimeConflictException()
    
    subject_course =subject_belongs_to_course(
        db,
        timetable.subject_id,
        timetable.course_id,
    )

    if not subject_course:
        raise SubjectCourseMismatchException()
    
    if timetable.end_time <= timetable.start_time:
        raise InvalidTimeRangeException()
    

    section_conflict = crud.section_time_conflict(
        db=db,
        course_id=timetable.course_id,
        section=timetable.section,
        day_of_week=timetable.day_of_week,
        start_time=timetable.start_time,
        end_time=timetable.end_time,
    )

    if section_conflict:
        raise SectionTimeConflictException()
    
    department_match = crud.faculty_matches_course_department(
        db,
        timetable.faculty_id,
        timetable.course_id,
    )

    if not department_match:
        raise FacultyDepartmentMismatchException()

    return crud.create_timetable(db, timetable)


def get_timetable(db: Session, timetable_id: int):

    timetable = crud.get_timetable(db, timetable_id)

    if not timetable:
        raise TimetableNotFoundException()

    return timetable


def get_timetables(db: Session):
    return crud.get_timetables(db)


def update_timetable(
    db: Session,
    timetable_id: int,
    updated: schemas.TimetableUpdate,
):

    timetable = crud.get_timetable(db, timetable_id)

    if not timetable:
        raise TimetableNotFoundException()

    return crud.update_timetable(db, timetable, updated)


def delete_timetable(db: Session, timetable_id: int):

    timetable = crud.get_timetable(db, timetable_id)

    if not timetable:
        raise TimetableNotFoundException()

    return crud.delete_timetable(db, timetable)


def get_course_timetable(db: Session, course_id: int):
    return crud.get_by_course(db, course_id)


def get_faculty_timetable(db: Session, faculty_id: int):
    return crud.get_by_faculty(db, faculty_id)