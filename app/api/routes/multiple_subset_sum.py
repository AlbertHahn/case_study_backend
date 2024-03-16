from fastapi import APIRouter

from app.models.inputpayload import InputPayload
from app.internal.multiple_subset_sum import subset_sum_recursive


router = APIRouter()

@router.post("/recursive")
def recursive_endpoint(inputpayload: InputPayload):
    """
    Subset sum recursive
    """
    return subset_sum_recursive(inputpayload)

@router.post("/memoization")
def memoization_endpoint(inputpayload: InputPayload):
    """
    Subset sum memoization
    """
    return subset_sum_recursive(inputpayload)