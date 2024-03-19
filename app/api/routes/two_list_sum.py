from fastapi import APIRouter

from app.models.models import TwoListTarget, SuccessfulResponse
from app.internal.two_list_sum import two_list_sum

router = APIRouter()


@router.post("/")
def two_list_sum_endpoint(
    two_list_target: TwoListTarget, response_model=SuccessfulResponse
) -> bool:
    """
    This function has a time complexity of O(n+m)
    """
    result = two_list_sum(two_list_target)
    return result
