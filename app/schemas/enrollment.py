from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


# ==========================================
# Base Schema
# ==========================================
class EnrollmentBase(BaseModel):

    student_id: int = Field(gt=0)

    subject_id: int = Field(gt=0)


# ==========================================
# Create Schema
# ==========================================
class EnrollmentCreate(EnrollmentBase):
    pass


# ==========================================
# Response Schema
# ==========================================
class EnrollmentResponse(EnrollmentBase):

    id: int

    enrolled_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )