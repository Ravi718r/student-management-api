from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from  sqlalchemy.orm import relationship

from app.database import Base

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    ) 

    code = Column(
        String(20),
        unique=True,
        nullable=False
    )

    credits = Column(
        Integer,
        nullable=False
    )

    semester = Column(
        Integer,
        nullable=False
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.id"),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    course = relationship(
        "Course",
        back_populates="subjects"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="subject",
        cascade="all, delete"
    )


    faculty_subjects = relationship(
        "FacultySubject",
        back_populates="subject",
        cascade="all, delete-orphan"
    )

    timetables = relationship(
        "Timetable",
        back_populates="subject",
        cascade="all, delete-orphan",
    )
