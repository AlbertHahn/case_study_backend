from fastapi import APIRouter

from app.models.models import InputPayload
from app.internal.two_list_sum import two_list_sum

router = APIRouter()


@router.post("/")
def unoptimized_endpoint(inputpayload: InputPayload):
    """
    This function has a time complexity of O(n*m)
    """
    result = two_list_sum(inputpayload)
    return result
