from pydantic import BaseModel, ConfigDict


class SubjectResult(BaseModel):
    subject: str
    internal_marks: float
    external_marks: float
    practical_marks: float
    total_marks: float
    grade: str
    result: str

    model_config = ConfigDict(
        from_attributes=True
    )


class StudentResultResponse(BaseModel):

    student: str

    department: str

    course: str

    gpa: float

    subjects: list[SubjectResult]

    model_config = ConfigDict(
        from_attributes=True
    )