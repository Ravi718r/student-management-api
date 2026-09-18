from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field
)

from app.schemas.department import DepartmentResponse


# =====================================================
# Base Schema
# =====================================================
class FacultyBase(BaseModel):

    employee_id: str = Field(
        min_length=3,
        max_length=20
    )

    first_name: str = Field(
        min_length=2,
        max_length=50
    )

    last_name: str = Field(
        min_length=2,
        max_length=50
    )

    email: EmailStr

    phone: str = Field(
        min_length=10,
        max_length=15
    )

    designation: str = Field(
        min_length=2,
        max_length=100
    )

    qualification: str = Field(
        min_length=2,
        max_length=100
    )

    experience_years: int = Field(
        ge=0,
        le=60
    )

    department_id: int = Field(
        gt=0
    )


# =====================================================
# Create Faculty
# =====================================================
class FacultyCreate(FacultyBase):
    pass


# =====================================================
# Update Faculty
# =====================================================
class FacultyUpdate(BaseModel):

    employee_id: str | None = Field(
        default=None,
        min_length=3,
        max_length=20
    )

    first_name: str | None = Field(
        default=None,
        min_length=2,
        max_length=50
    )

    last_name: str | None = Field(
        default=None,
        min_length=2,
        max_length=50
    )

    email: EmailStr | None = None

    phone: str | None = Field(
        default=None,
        min_length=10,
        max_length=15
    )

    designation: str | None = None

    qualification: str | None = None

    experience_years: int | None = Field(
        default=None,
        ge=0,
        le=60
    )

    department_id: int | None = Field(
        default=None,
        gt=0
    )


# =====================================================
# Faculty Response
# =====================================================
class FacultyResponse(FacultyBase):

    id: int

    model_config = ConfigDict(
        from_attributes=True
    )


# =====================================================
# Faculty With Department
# =====================================================
class FacultyWithDepartment(BaseModel):

    id: int

    employee_id: str

    first_name: str

    last_name: str

    email: EmailStr

    phone: str

    designation: str

    qualification: str

    experience_years: int

    department: DepartmentResponse

    model_config = ConfigDict(
        from_attributes=True
    )