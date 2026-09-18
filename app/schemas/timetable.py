from datetime import datetime
from datetime import time

from pydantic import BaseModel, ConfigDict

from app.schemas.course import CourseResponse
from app.schemas.subject import SubjectResponse
from app.schemas.faculty import FacultyResponse


class TimetableBase(BaseModel):
    course_id: int
    subject_id: int
    faculty_id: int
    day_of_week: str
    start_time: time
    end_time: time
    room_number: str
    section: str


class TimetableCreate(TimetableBase):
    pass


class TimetableUpdate(BaseModel):
    course_id: int | None = None
    subject_id: int | None = None
    faculty_id: int | None = None
    day_of_week: str | None = None
    start_time: time | None = None
    end_time: time | None = None
    room_number: str | None = None
    section: str | None = None


class TimetableResponse(TimetableBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TimetableWithDetails(TimetableResponse):
    course: CourseResponse
    subject: SubjectResponse
    faculty: FacultyResponse