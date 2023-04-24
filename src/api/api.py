from fastapi import APIRouter, Depends
from .endpoints import dashboard, users, tasks
from ..users.manager import current_active_user


router = APIRouter()

router.include_router(
    dashboard.router, dependencies=[Depends(current_active_user)], tags=["dashboard"]
)
router.include_router(users.router)
router.include_router(tasks.router, tags=["tasks"])
