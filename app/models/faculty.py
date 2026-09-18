from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Faculty(Base):
    __tablename__ = "faculty"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_id = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    first_name = Column(
        String,
        nullable=False
    )

    last_name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    phone = Column(
        String,
        unique=True,
        nullable=False
    )

    designation = Column(
        String,
        nullable=False
    )

    qualification = Column(
        String,
        nullable=False
    )

    experience_years = Column(
        Integer,
        nullable=False,
        default=0
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    department = relationship(
        "Department",
        back_populates="faculty"
    )

    faculty_subjects = relationship(
        "FacultySubject",
        back_populates="faculty",
        cascade="all, delete-orphan"
    )

    timetables = relationship(
        "Timetable",
        back_populates="faculty",
        cascade="all, delete-orphan",
    )