from fastapi import APIRouter, Depends
from .endpoints import dashboard, users, tasks, tasksItem, projects
from ..users.manager import current_active_user


router = APIRouter()

router.include_router(
    dashboard.router, dependencies=[Depends(current_active_user)], tags=["dashboard"]
)
router.include_router(users.router)
router.include_router(tasks.router, tags=["tasks"])
router.include_router(tasksItem.router, tags=["tasks_item"])
router.include_router(projects.router, tags=["tasks_item"])
