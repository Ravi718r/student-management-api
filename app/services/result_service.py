from sqlalchemy.orm import Session

import app.models
from app.core.exceptions import StudentNotFoundException


# =====================================================
# Student Result Card
# =====================================================
def get_student_result(
    db: Session,
    student_id: int
):

    student = (
        db.query(app.models.Student)
        .filter(
            app.models.Student.id == student_id
        )
        .first()
    )

    if student is None:
        raise StudentNotFoundException()

    enrollments = (
        db.query(app.models.Enrollment)
        .filter(
            app.models.Enrollment.student_id == student_id
        )
        .all()
    )

    subject_results = []

    for enrollment in enrollments:

        mark = enrollment.marks

        if mark is None:
            continue

        subject = enrollment.subject

        subject_results.append(
            {
                "subject": subject.name,
                "internal_marks": mark.internal_marks,
                "external_marks": mark.external_marks,
                "practical_marks": mark.practical_marks,
                "total_marks": mark.total_marks,
                "grade": mark.grade,
                "result": mark.result
            }
        )
    gpa = calculate_gpa(subject_results)

    return {
        "student": student.name,
        "department": student.department.name,
        "course": student.course.name,
        "gpa": gpa,
        "subjects": subject_results
    }

# ==========================================
# Grade Point
# ==========================================
def grade_point(grade: str):

    mapping = {
        "A+": 10,
        "A": 9,
        "B": 8,
        "C": 7,
        "D": 6,
        "E": 5,
        "F": 0
    }

    return mapping.get(grade, 0)


# ==========================================
# GPA Calculator
# ==========================================
def calculate_gpa(subjects):

    if len(subjects) == 0:
        return 0

    total = 0

    for subject in subjects:
        total += grade_point(subject["grade"])

    return round(total / len(subjects), 2)