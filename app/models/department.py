from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        unique=True,
        nullable=False
    )

    code = Column(
        String(10),
        unique=True,
        nullable=False
    )

    description= Column(
        String(255),
        nullable=True
    )

    created_at= Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at= Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    students = relationship(
        "Student",
        back_populates="department"
    )

    courses= relationship(
        "Course",
        back_populates="department",
        cascade="all, delete"
    )


    faculty = relationship(
        "Faculty",
        back_populates="department",
        cascade="all, delete-orphan"
    )