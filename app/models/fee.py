from enum import Enum

from sqlalchemy import (
    Column,
    Integer,
    Float,
    Date,
    DateTime,
    ForeignKey,
    Enum as SqlEnum
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class FeeStatus(str, Enum):
    PENDING = "PENDING"
    PARTIAL = "PARTIAL"
    PAID = "PAID"


class Fee(Base):

    __tablename__ = "fees"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        nullable=False
    )

    total_amount = Column(
        Float,
        nullable=False
    )

    paid_amount = Column(
        Float,
        default=0,
        nullable=False
    )

    due_date = Column(
        Date,
        nullable=False
    )

    status = Column(
        SqlEnum(FeeStatus),
        nullable=False,
        default=FeeStatus.PENDING
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    student = relationship(
        "Student",
        back_populates="fees"
    )