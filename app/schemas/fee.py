from datetime import date, datetime

from pydantic import BaseModel, Field, ConfigDict

from app.models.fee import FeeStatus


class FeeCreate(BaseModel):

    student_id: int = Field(gt=0)

    total_amount: float = Field(gt=0)

    due_date: date


class FeeUpdate(BaseModel):

    total_amount: float = Field(gt=0)

    due_date: date


class FeePayment(BaseModel):

    amount: float = Field(gt=0)


class FeeResponse(BaseModel):

    id: int

    student_id: int

    total_amount: float

    paid_amount: float

    due_date: date

    status: FeeStatus

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )