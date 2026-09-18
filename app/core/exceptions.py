from fastapi import HTTPException, status

class StudentNotFoundException(HTTPException):

    def __init__(self):

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student Not Found"
        )

class StudentAlreadyExistsException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Student ID Already Exists"
        )
        
class UserAlreadyExistsException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Emial Already Registered"
        )

class InvalidCredentialsException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Email or Password"
        )


class UnauthorizedException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to perform this action"
        )

class DepartmentNotFoundException(HTTPException):

    def __init__(self):

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department Not Found"
        ) 


class DepartmentAlreadyExistsException(Exception):
    def __init__(self):
        self.message = "Department code already exists."
        super().__init__(self.message)


class AttendanceAlreadyMarkedException(Exception):
    pass

class CourseNotFoundException(Exception):
    pass


class CourseAlreadyExistsException(Exception):
    pass



class SubjectNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail="Subject not found."
        )


class SubjectAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Subject code already exists."
        )



class EnrollmentNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail="Enrollment not found."
        )


class EnrollmentAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Student is already enrolled in this subject."
        )

class MarksNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail="Marks not found."
        )


class MarksAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Marks already exist for this enrollment."
        )


class FeeOverPaymentException(
    HTTPException
):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Payment exceeds total fee amount."
        )




class FeeNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail="Fee not found."
        )


class FacultyNotFoundException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=404,
            detail="Faculty not found."
        )


class FacultyEmployeeIdAlreadyExistsException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Employee ID already exists."
        )


class FacultyEmailAlreadyExistsException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Faculty email already exists."
        )


class FacultyPhoneAlreadyExistsException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Faculty phone number already exists."
        )


class FacultySubjectNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail="Faculty Subject mapping not found."
        )


class FacultySubjectAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Faculty is already assigned to this subject."
        )


class FacultySubjectAssignmentException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Faculty is not assigned to this subject."
        )


class TimetableNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail="Timetable not found."
        )


class TimetableConflictException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Faculty or room already has a class during this time."
        )


class FacultyTimeConflictException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Faculty already has another class during this time."
        )



class RoomTimeConflictException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Room is already occupied during this time."
        )


class SubjectCourseMismatchException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Selected subject does not belong to the selected course."
        )


class InvalidTimeRangeException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="End time must be later than start time."
        )

class SectionTimeConflictException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Section already has another class during this time."
        )


class FacultyDepartmentMismatchException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Faculty does not belong to the course's department."
        )