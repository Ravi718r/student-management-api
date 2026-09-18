from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class DepartmentBase(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=100
    )

    code: str = Field(
        min_length=2,
        max_length=10
    )

    description: str | None = Field(
        default=None,
        max_length=255
    )

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):

    id: int

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
