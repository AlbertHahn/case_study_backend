from fastapi import APIRouter

from app.api.routes import two_list_sum

api_router = APIRouter()
api_router.include_router(
    two_list_sum.router, prefix="/two-list-sum", tags=["calculate"]
)
