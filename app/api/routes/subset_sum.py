from fastapi import APIRouter

from app.models.inputpayload import InputPayload
from app.internal.subset_sum_recursion import subset_sum_recursive


router = APIRouter()

@router.post(
    "subset-sum"
)
def subset_sum_recursive(inputpayload : InputPayload):
    """
    Subset sum endpoint
    """
    return True#subset_sum_recursive(inputpayload)