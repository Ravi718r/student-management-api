"""
Fee Router

This router handles all Fee Management APIs.

Available APIs:
1. Create Fee
2. Get All Fees
3. Get Pending Fees
4. Get Partial Fees
5. Get Paid Fees
6. Get Student Fees
7. Get Fee By ID
8. Update Fee
9. Delete Fee
10. Pay Fee
"""

from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.auth import (
    get_current_user,
    admin_required
)

from app.schemas import (
    FeeCreate,
    FeeUpdate,
    FeePayment,
    FeeResponse
)

from app.services import fee_service

router = APIRouter(
    prefix="/fees",
    tags=["Fees"]
)

# ==========================================================
# Create Fee
# ==========================================================
@router.post(
    "/",
    response_model=FeeResponse,
    summary="Create Fee"
)
def create_fee(
    fee: FeeCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    """
    Create a new fee record.
    Only Admin can create fee records.
    """
    return fee_service.create_fee(db, fee)


# ==========================================================
# Get All Fees
# ==========================================================
@router.get(
    "/",
    response_model=List[FeeResponse],
    summary="Get All Fees"
)
def get_fees(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Retrieve all fee records.
    """
    return fee_service.get_fees(db)


# ==========================================================
# Get Pending Fees
# ==========================================================
@router.get(
    "/pending",
    response_model=List[FeeResponse],
    summary="Get Pending Fees"
)
def get_pending_fees(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Retrieve all pending fee records.
    """
    return fee_service.get_pending_fees(db)


# ==========================================================
# Get Partial Fees
# ==========================================================
@router.get(
    "/partial",
    response_model=List[FeeResponse],
    summary="Get Partial Fees"
)
def get_partial_fees(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Retrieve all partially paid fee records.
    """
    return fee_service.get_partial_fees(db)


# ==========================================================
# Get Paid Fees
# ==========================================================
@router.get(
    "/paid",
    response_model=List[FeeResponse],
    summary="Get Paid Fees"
)
def get_paid_fees(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Retrieve all fully paid fee records.
    """
    return fee_service.get_paid_fees(db)


# ==========================================================
# Get Fees By Student
# ==========================================================
@router.get(
    "/student/{student_id}",
    response_model=List[FeeResponse],
    summary="Get Student Fees"
)
def get_student_fees(
    student_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Retrieve all fee records of a particular student.
    """
    return fee_service.get_student_fees(
        db,
        student_id
    )


# ==========================================================
# Get Fee By ID
# ==========================================================
@router.get(
    "/{fee_id}",
    response_model=FeeResponse,
    summary="Get Fee By ID"
)
def get_fee(
    fee_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Retrieve a fee record using its ID.
    """
    return fee_service.get_fee(
        db,
        fee_id
    )


# ==========================================================
# Update Fee
# ==========================================================
@router.put(
    "/{fee_id}",
    response_model=FeeResponse,
    summary="Update Fee"
)
def update_fee(
    fee_id: int,
    fee: FeeUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    """
    Update fee details.
    Only Admin can update fee records.
    """
    return fee_service.update_fee(
        db,
        fee_id,
        fee
    )


# ==========================================================
# Delete Fee
# ==========================================================
@router.delete(
    "/{fee_id}",
    summary="Delete Fee"
)
def delete_fee(
    fee_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    """
    Delete a fee record.
    Only Admin can delete fee records.
    """
    fee_service.delete_fee(
        db,
        fee_id
    )

    return {
        "message": "Fee deleted successfully."
    }


# ==========================================================
# Pay Fee
# ==========================================================
@router.post(
    "/{fee_id}/pay",
    response_model=FeeResponse,
    summary="Pay Fee"
)
def pay_fee(
    fee_id: int,
    payment: FeePayment,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    """
    Record a fee payment.

    Fee Status Flow:
    PENDING -> PARTIAL -> PAID
    """
    return fee_service.pay_fee(
        db,
        fee_id,
        payment
    )