from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


# ==========================================
# Base Schema
# ==========================================
class SubjectBase(BaseModel):

    name: str = Field(
        min_length=3,
        max_length=100
    )

    code: str = Field(
        min_length=2,
        max_length=20
    )

    credits: int = Field(
        ge=1,
        le=10
    )

    semester: int = Field(
        ge=1,
        le=8
    )

    course_id: int = Field(
        gt=0
    )


# ==========================================
# Create Schema
# ==========================================
class SubjectCreate(SubjectBase):
    pass


# ==========================================
# Update Schema
# ==========================================
class SubjectUpdate(SubjectBase):
    pass


# ==========================================
# Response Schema
# ==========================================
class SubjectResponse(SubjectBase):

    id: int

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )