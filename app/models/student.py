from sqlalchemy import Column, Integer, String
from app.database import Base 
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=False
    ) 

    course_id = Column(
        Integer,
        ForeignKey("courses.id"),
        nullable=True
    )

    department = relationship(
        "Department",
        back_populates="students" 
    )

    attendance = relationship(
        "Attendance",
        back_populates="student",
        cascade = "all, delete"
    )

    course = relationship(
        "Course",
        back_populates="students"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="student",
        cascade="all, delete"
    )


    fees = relationship(
        "Fee",
        back_populates="student",
        cascade="all, delete"
    )