from fastapi import APIRouter, Depends
from .endpoints import dashboard

router = APIRouter()

router.include_router(dashboard.router)