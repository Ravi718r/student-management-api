from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.faculty import FacultyResponse
from app.schemas.subject import SubjectResponse


class FacultySubjectBase(BaseModel):
    faculty_id: int
    subject_id: int


class FacultySubjectCreate(FacultySubjectBase):
    pass


class FacultySubjectResponse(FacultySubjectBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class FacultySubjectWithDetails(FacultySubjectResponse):
    faculty: FacultyResponse
    subject: SubjectResponse