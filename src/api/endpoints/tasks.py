from fastapi import APIRouter, Request, Depends
from ...crud.db import get_crud_db
from ...tasks.models import TaskCreate, Task, TaskRead

router = APIRouter()


@router.post("/tasks")
async def create_task(
    request: Request, task_create: TaskCreate, db=Depends(get_crud_db), 
):
    task_model_obj = Task(**task_create.dict())
    task = await db.create(task_model_obj)
    return task


@router.get("/tasks/{task_id}", response_model=TaskRead)
async def get_task(
    request: Request, task_id: int, db=Depends(get_crud_db)
):
    task = await db.get_by_id(Task, task_id)
    if (task == None):
        return {"name":"ID_NOT_VALID"}
    else:
        return task


@router.get("/tasks")
async def get_tasks(request: Request, db=Depends(get_crud_db)):
    tasks = await db.get_all_tasks(Task)
    return tasks
