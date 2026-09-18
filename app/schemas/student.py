from pydantic import BaseModel, ConfigDict, EmailStr, Field
from enum import Enum
from app.schemas.department import DepartmentResponse


class Branch(str, Enum):
    CSE = "CSE"
    ECE = "ECE"
    IT = "IT"
    ME = "ME"
    CE = "CE"


class StudentBase(BaseModel):

    id: int = Field(gt=0)

    name: str = Field(
        min_length=3,
        max_length=50
    )

    age: int = Field(
        ge=18,
        le=100
    )

    department_id: int = Field(
        gt=0
    )
    
    course_id: int = Field(
        gt=0
    )

class StudentCreate(StudentBase):
    pass


class StudentResponse(StudentBase):
    model_config = ConfigDict(from_attributes=True)

class StudentWithDepartment(BaseModel):
    id: int 
    name: str
    age: int

    department: DepartmentResponse

    model_config = ConfigDict(
        from_attributes= True
    )