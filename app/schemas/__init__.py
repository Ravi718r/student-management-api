from .student import (
    StudentBase,
    StudentCreate,
    StudentResponse
)

from .user import (
    UserBase,
    UserCreate,
    UserLogin,
    UserResponse
)  

from .department import(
    DepartmentBase,
    DepartmentCreate,
    DepartmentResponse,
    
)

from .student import StudentWithDepartment

from .common import SuccessResponse

from .attendance import(
    AttendanceCreate,
    AttendanceBase,
    AttendanceResponse,
    AttendanceUpdate
)

from .course import *
from .subject import *
from .enrollment import *
from .marks import *
from .result import *
from .fee import *
from .faculty import *
from .faculty_subject import *
from .timetable import *
