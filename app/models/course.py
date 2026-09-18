from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Course(Base):
    __tablename__ ="courses"

    id= Column(
        Integer,
        primary_key=True,
        index= True
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

    duration = Column(
        Integer,
        nullable=False
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable= False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    department= relationship(
        "Department",
        back_populates="courses"
    )

    students= relationship(
        "Student",
        back_populates="course",
        cascade="all, delete"
    )

    subjects= relationship(
        "Subject",
        back_populates="course",
        cascade="all, delete"
    )

    timetables = relationship(
        "Timetable",
        back_populates="course",
        cascade="all, delete-orphan",
    )