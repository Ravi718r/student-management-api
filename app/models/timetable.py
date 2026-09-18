from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Time,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.database import Base


class Timetable(Base):
    __tablename__ = "timetables"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.id"),
        nullable=False,
    )

    subject_id = Column(
        Integer,
        ForeignKey("subjects.id"),
        nullable=False,
    )

    faculty_id = Column(
        Integer,
        ForeignKey("faculty.id"),
        nullable=False,
    )

    day_of_week = Column(
        String(15),
        nullable=False,
    )

    start_time = Column(
        Time,
        nullable=False,
    )

    end_time = Column(
        Time,
        nullable=False,
    )

    room_number = Column(
        String(20),
        nullable=False,
    )

    section = Column(
        String(5),
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    course = relationship(
        "Course",
        back_populates="timetables",
    )

    subject = relationship(
        "Subject",
        back_populates="timetables",
    )

    faculty = relationship(
        "Faculty",
        back_populates="timetables",
    )