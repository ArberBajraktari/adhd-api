from fastapi import APIRouter, Depends
from .endpoints import dashboard, users


router = APIRouter()

router.include_router(dashboard.router)
router.include_router(users.router)