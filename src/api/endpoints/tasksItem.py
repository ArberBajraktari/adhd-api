from fastapi import APIRouter, HTTPException, Request, Depends
from ...crud.db import get_crud_db
from ...tasks.models import TaskCreate, Task, TaskRead
from ...task_item.models import TaskItem, TaskItemCreate, TaskItemRead, TaskItemUpdate
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
    tasks = await db.get_items_for_task(Task, task_id)
    return tasks

@router.put("/tasks_item/{task_item_id}")
async def update_task_item(
    task_item_id: int, task_update: TaskItemUpdate, db=Depends(get_crud_db), user: User = Depends(current_active_user)
):
    await db.update_task_item(task_update, task_item_id)


@router.delete("/tasks_item")
async def delete_task_item(
    item_id: int, db=Depends(get_crud_db), user: User = Depends(current_active_user)
):
    deleted_task = await db.delete_item(item_id)
    if deleted_task:
        return {"message": "Task deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")