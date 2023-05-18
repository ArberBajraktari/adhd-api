from fastapi import APIRouter, Request, Depends
from ...crud.db import get_crud_db
from ...tasks.models import TaskCreate, Task, TaskRead
from ...users.models import User
from ...users.manager import current_active_user

router = APIRouter()


@router.post("/tasks")
async def create_task(
    request: Request, task_create: TaskCreate, db=Depends(get_crud_db), user: User = Depends(current_active_user)
):
    task_model_obj = Task(**task_create.dict())
    task = await db.create(task_model_obj)
    return task


@router.get("/tasks/{task_id}", response_model=TaskRead)
async def get_task(
    request: Request, task_id: int, db=Depends(get_crud_db), user: User = Depends(current_active_user)
):
    task = await db.get_task_by_id(Task, task_id)
    if (task == None):
        return {"name":"ID_NOT_VALID"}
    else:
        return task


@router.get("/tasks")
async def get_tasks(
    request: Request, db=Depends(get_crud_db), user: User = Depends(current_active_user)
):
    tasks = await db.get_all_tasks(Task, user.id)
    return tasks