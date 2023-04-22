from fastapi import APIRouter, Request, Depends
from ...crud.db import get_crud_db
from ...tasks.models import TaskCreate, Task

router = APIRouter()


@router.post("/tasks")
async def create_task(
    request: Request, task_create: TaskCreate, db=Depends(get_crud_db)
):
    task_model_obj = Task(**task_create.dict())
    task = await db.create(task_model_obj)
    return task
