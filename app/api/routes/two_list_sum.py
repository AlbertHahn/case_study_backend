from fastapi import APIRouter

from app.models.inputpayload import InputPayload
from app.internal.two_list_sum import two_list_sum, two_list_sum_optimized

router = APIRouter()


@router.post("/unoptimized")
def unoptimized_endpoint(inputpayload: InputPayload):
    """
    This function has a time complexity of O(n*m)
    """
    result = two_list_sum(inputpayload)
    return result


@router.post("/optimized")
def optimized_endpoint(inputpayload: InputPayload):
    """
    This function has a time complexity of O(n+m)
    """
    result = two_list_sum_optimized(inputpayload)
    return result
