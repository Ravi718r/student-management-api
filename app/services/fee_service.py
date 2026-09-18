from sqlalchemy.orm import Session

import app.models
import app.crud

from app.schemas import (
    FeeCreate,
    FeeUpdate,
    FeePayment
)

from app.core.exceptions import (
    StudentNotFoundException,
    FeeNotFoundException
)


# Get Fee
def get_fee(
    db: Session,
    fee_id: int
):
    fee = app.crud.fee.fee_crud.get(
        db,
        fee_id
    )

    if fee is None:
        raise FeeNotFoundException()

    return fee


# Get all Fees
def get_fees(
    db: Session
):
    return app.crud.fee.fee_crud.get_all(db)


# Create Fee
def create_fee(
    db: Session,
    fee: FeeCreate
):

    student = app.crud.student.student_crud.get(
        db,
        fee.student_id
    )

    if student is None:
        raise StudentNotFoundException()

    db_fee = app.models.Fee(
        student_id=fee.student_id,
        total_amount=fee.total_amount,
        paid_amount=0,
        due_date=fee.due_date,
        status=app.models.FeeStatus.PENDING
    )

    db.add(db_fee)
    db.commit()
    db.refresh(db_fee)

    return db_fee


# Update fee
def update_fee(
    db: Session,
    fee_id: int,
    fee: FeeUpdate
):

    db_fee = get_fee(
        db,
        fee_id
    )

    return app.crud.fee.fee_crud.update(
        db,
        db_fee,
        fee
    )


# Delete Fee
def delete_fee(
    db: Session,
    fee_id: int
):

    db_fee = get_fee(
        db,
        fee_id
    )

    app.crud.fee.fee_crud.delete(
        db,
        db_fee
    )


# Pay fee
def pay_fee(
    db: Session,
    fee_id: int,
    payment: FeePayment
):

    fee = get_fee(
        db,
        fee_id
    )

    new_paid_amount = fee.paid_amount + payment.amount

    if new_paid_amount > fee.total_amount:
        raise ValueError(
            "Payment exceeds total fee amount."
        )

    fee.paid_amount = new_paid_amount

    if fee.paid_amount == 0:
        fee.status = app.models.FeeStatus.PENDING

    elif fee.paid_amount < fee.total_amount:
        fee.status = app.models.FeeStatus.PARTIAL

    else:
        fee.status = app.models.FeeStatus.PAID

    db.commit()

    db.refresh(fee)

    return fee



# Student Fees
def get_student_fees(
    db: Session,
    student_id: int
):
    return app.crud.fee.get_student_fees(
        db,
        student_id
    )


#Pending fees
def get_pending_fees(
    db: Session
):
    return app.crud.fee.get_pending_fees(db)


# Partial fees
def get_partial_fees(
    db: Session
):
    return app.crud.fee.get_partial_fees(db)


#Paid Fees
def get_paid_fees(
    db: Session
):
    return app.crud.fee.get_paid_fees(db)