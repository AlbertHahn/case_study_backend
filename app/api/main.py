from fastapi import APIRouter

from app.api.routes import multiple_subset_sum

api_router = APIRouter()
api_router.include_router(multiple_subset_sum.router, prefix="/multiple-subset-sum", tags=["calculate"])
