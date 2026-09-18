from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base


class Marks(Base):
    __tablename__ = "marks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    enrollment_id = Column(
        Integer,
        ForeignKey("enrollments.id"),
        nullable=False,
        unique=True
    )

    internal_marks = Column(
        Float,
        nullable=False
    )

    external_marks = Column(
        Float,
        nullable=False
    )

    practical_marks = Column(
        Float,
        nullable=False
    )

    total_marks = Column(
        Float,
        nullable=False
    )

    grade = Column(
        String(5),
        nullable=False
    )

    result = Column(
        String(10),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    enrollment = relationship(
        "Enrollment",
        back_populates="marks"
    )