from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.models.attendance import AttendanceStatus

class AttendanceBase(BaseModel):
    student_id: int
    date: date
    status: AttendanceStatus
    remarks: Optional[str] = None


class AttendanceCreate(AttendanceBase):
    pass

class AttendanceUpdate(BaseModel):
    status: AttendanceStatus
    remarks: Optional[str] = None

class AttendanceResponse(AttendanceBase):
    id: int
    created_at: datetime

    model_config= ConfigDict(
        from_attributes=True
    )