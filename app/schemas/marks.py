from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


# ==========================================
# Base Schema
# ==========================================
class MarksBase(BaseModel):

    enrollment_id: int = Field(gt=0)

    internal_marks: float = Field(ge=0, le=30)

    external_marks: float = Field(ge=0, le=60)

    practical_marks: float = Field(ge=0, le=10)


# ==========================================
# Create
# ==========================================
class MarksCreate(MarksBase):
    pass


# ==========================================
# Update
# ==========================================
class MarksUpdate(MarksBase):
    pass


# ==========================================
# Response
# ==========================================
class MarksResponse(MarksBase):

    id: int

    total_marks: float

    grade: str

    result: str

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )