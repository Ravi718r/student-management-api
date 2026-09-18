from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
    UniqueConstraint
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class FacultySubject(Base):
    __tablename__ = "faculty_subjects"

    __table_args__ = (
        UniqueConstraint(
            "faculty_id",
            "subject_id",
            name="uq_faculty_subject"
        ),
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    faculty_id = Column(
        Integer,
        ForeignKey("faculty.id"),
        nullable=False
    )

    subject_id = Column(
        Integer,
        ForeignKey("subjects.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    faculty = relationship(
        "Faculty",
        back_populates="faculty_subjects"
    )

    subject = relationship(
        "Subject",
        back_populates="faculty_subjects"
    )