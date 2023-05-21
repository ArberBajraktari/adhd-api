from fastapi import APIRouter, HTTPException, Request, Depends
from ...crud.db import get_crud_db
from ...tasks.models import TaskCreate, Task, TaskRead, TaskUpdate
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

@router.delete("/tasks/{task_id}")
async def delete_task(
    task_id: int, db=Depends(get_crud_db), user: User = Depends(current_active_user)
):
    deleted_task = await db.delete_task(task_id)
    if deleted_task:
        return {"message": "Task deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")

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

@router.get("/tasks_full")
async def get_tasks_full(
    request: Request, db=Depends(get_crud_db), user: User = Depends(current_active_user)
):
    tasks = await db.get_all_tasks_full(Task, user.id)
    return tasks



@router.put("/tasks/{task_id}")
async def update_task_item(
    task_id: int, task_update: TaskUpdate, db=Depends(get_crud_db), user: User = Depends(current_active_user)
):
    await db.update_task(task_update, task_id)
