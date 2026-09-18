from datetime import datetime
from enum import Enum

from sqlalchemy import Column, Integer, Date, DateTime, ForeignKey, Enum as SqlEnum, String
from sqlalchemy.orm import relationship

from app.database import Base

class AttendanceStatus(str, Enum):
    PRESENT = "Present"
    ABSENT = "Absent"
    LATE = "Late"
    LEAVE = "Leave"


class Attendance(Base):
    __tablename__ ="attendance"

    id = Column(
        Integer,
        primary_key= True,
        index= True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        nullable= False
    )

    date = Column(
        Date,
        nullable=False
    )

    status = Column(
        SqlEnum(AttendanceStatus),
        nullable= False
    )

    remarks = Column(
        String(255),
        nullable= True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    student = relationship(
        "Student",
        back_populates="attendance"
    )