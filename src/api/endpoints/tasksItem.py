from fastapi import APIRouter, Request, Depends
from ...crud.db import get_crud_db
from ...tasks.models import TaskCreate, Task, TaskRead
from ...task_item.models import TaskItem, TaskItemCreate, TaskItemRead
from ...users.models import User
from ...users.manager import current_active_user

router = APIRouter()


@router.post("/tasks_item")
async def create_task_item(
    request: Request, task_create: TaskItemCreate, db=Depends(get_crud_db), user: User = Depends(current_active_user)
):
    task_model_obj = TaskItem(**task_create.dict())
    task = await db.create(task_model_obj)
    return task


@router.get("/task_item")
async def get_task_items(
    request: Request, task_id: int, db=Depends(get_crud_db)
):
    tasks = await db.get_items_for_task(TaskItem, task_id)
    return tasks