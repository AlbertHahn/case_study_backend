from fastapi import APIRouter

from app.api.routes import subset_sum

api_router = APIRouter()
api_router.include_router(subset_sum.router, prefix="/calculate", tags=["calculate"])
