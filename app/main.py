from fastapi import FastAPI

from app.routers import students, users, department, course, subject, enrollment, marks, result, fee, faculty, faculty_subject, timetable
from app.bootstrap import create_default_admin
from app.core import logging_config
from app.core.handler import registere_exception_handlers
from app.routers import attendance

from app import models


app = FastAPI(
    title="Student Management API",
    description="Professional FastAPI Project",
    version="1.0.0"
)

registere_exception_handlers(app)

create_default_admin()


@app.get("/")
def home():
    return {
        "message": "Welcome to Student Management API"
    }


app.include_router(students.router)
app.include_router(users.router)
app.include_router(department.router)
app.include_router(attendance.router)
app.include_router(course.router)
app.include_router(subject.router)
app.include_router(enrollment.router)
app.include_router(marks.router)
app.include_router(result.router)
app.include_router(fee.router)
app.include_router(faculty.router)
app.include_router(faculty_subject.router)
app.include_router(timetable.router)