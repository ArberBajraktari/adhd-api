from fastapi import APIRouter, HTTPException, Request, Depends
from ...crud.db import get_crud_db
from ...tasks.models import TaskCreate, Task, TaskRead
from ...projects.models import Project, ProjectCreate, ProjectRead
from ...users.models import User
from ...users.manager import current_active_user

router = APIRouter()


@router.post("/projects")
async def create_project(
    request: Request, task_create: ProjectCreate, db=Depends(get_crud_db), user: User = Depends(current_active_user)
):
    task_model_obj = Project(**task_create.dict())
    task = await db.create(task_model_obj)
    return task

@router.delete("/project")
async def delete_project(
    task_id: int, db=Depends(get_crud_db), user: User = Depends(current_active_user)
):
    deleted_task = await db.delete_project(task_id)
    if deleted_task:
        return {"message": "Task deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@router.get("/projects")
async def get_projects(
    request: Request, db=Depends(get_crud_db), user: User = Depends(current_active_user)
):
    tasks = await db.get_all_projects(Project, user.id)
    return tasks

@router.put("/projects")
async def update_projects(
    project_id: int, project_update: ProjectCreate, db=Depends(get_crud_db), user: User = Depends(current_active_user)
):
    await db.update_project(project_update, project_id)