from datetime import datetime

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    StudentNotFoundException,
    StudentAlreadyExistsException,
    DepartmentNotFoundException,
    DepartmentAlreadyExistsException,
    AttendanceAlreadyMarkedException,
    CourseAlreadyExistsException,
    CourseNotFoundException
    )


def registere_exception_handlers(app: FastAPI):

    # =====================================================
    # HTTP Exceptions
    # =====================================================
    @app.exception_handler(HTTPException)
    async def http_exception_handler(
        request: Request,
        exc: HTTPException
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "message": exc.detail,
                "status_code": exc.status_code,
                "path": request.url.path,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    # =====================================================
    # Student Not Found
    # =====================================================
    @app.exception_handler(StudentNotFoundException)
    async def student_not_found_handler(
        request: Request,
        exc: StudentNotFoundException
    ):
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": "Student not found.",
                "status_code": 404,
                "path": request.url.path,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    # =====================================================
    # Student Already Exists
    # =====================================================
    @app.exception_handler(StudentAlreadyExistsException)
    async def student_exists_handler(
        request: Request,
        exc: StudentAlreadyExistsException
    ):
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": "Student ID already exists.",
                "status_code": 400,
                "path": request.url.path,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    # =====================================================
    # Department Not Found
    # =====================================================
    @app.exception_handler(DepartmentNotFoundException)
    async def department_not_found_handler(
        request: Request,
        exc: DepartmentNotFoundException
    ):
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": "Department not found.",
                "status_code": 404,
                "path": request.url.path,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    # =====================================================
    # Department Already Exists
    # =====================================================
    @app.exception_handler(DepartmentAlreadyExistsException)
    async def department_exists_handler(
        request: Request,
        exc: DepartmentAlreadyExistsException
    ):
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": "Department code already exists.",
                "status_code": 400,
                "path": request.url.path,
                "timestamp": datetime.utcnow().isoformat()
            }
        )
    
    @app.exception_handler(
        AttendanceAlreadyMarkedException
    )
    async def attendance_already_marked_handler(
        request: Request,
        exc: AttendanceAlreadyMarkedException
    ):
        return JSONResponse(
            status_code=400,
            content={
                "message": "Attendance already marked for this student on this date."
            }
        )
    
    @app.exception_handler(
        CourseNotFoundException
    )
    async def course_not_found_handler(
        request: Request,
        exc: CourseNotFoundException
    ):
        return JSONResponse(
            status_code=404,
            content={
                "message": "Course not found."
            }
        )


    @app.exception_handler(
        CourseAlreadyExistsException
    )
    async def course_exists_handler(
        request: Request,
        exc: CourseAlreadyExistsException
    ):
        return JSONResponse(
            status_code=400,
            content={
                "message": "Course code already exists."
            }
        )