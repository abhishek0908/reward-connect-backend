from fastapi import APIRouter

from app.api.endpoints import login
api_router = APIRouter()
api_router.include_router(login.router, prefix="/api")