from sqlalchemy.orm import Session

import app.models

from .base import BaseCRUD


fee_crud = BaseCRUD(app.models.Fee)


def get_student_fees(
    db: Session,
    student_id: int
):
    return (
        db.query(app.models.Fee)
        .filter(
            app.models.Fee.student_id == student_id
        )
        .all()
    )


def get_pending_fees(
    db: Session
):
    return (
        db.query(app.models.Fee)
        .filter(
            app.models.Fee.status ==
            app.models.FeeStatus.PENDING
        )
        .all()
    )


def get_partial_fees(
    db: Session
):
    return (
        db.query(app.models.Fee)
        .filter(
            app.models.Fee.status ==
            app.models.FeeStatus.PARTIAL
        )
        .all()
    )


def get_paid_fees(
    db: Session
):
    return (
        db.query(app.models.Fee)
        .filter(
            app.models.Fee.status ==
            app.models.FeeStatus.PAID
        )
        .all()
    )