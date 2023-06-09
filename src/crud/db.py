from ..users.models import User
from fastapi import Depends
from sqlalchemy import update
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.future import select
from ..db.session import get_async_session
from ..db.base import Base
from ..task_item.models import TaskItem
from ..tasks.models import Task
from ..projects.models import Project
from sqlalchemy import delete


class DBCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, model_obj: Base):
        self.session.add(model_obj)
        await self.session.commit()
        await self.session.refresh(model_obj)
        return model_obj
    
    async def get_all_tasks(self, model_cls: type[Base], id_uuid: any) -> List[Base]:
        result = await self.session.execute(select(model_cls).filter(model_cls.user_id == str(id_uuid)))
        return result.scalars().all()
    
    async def get_all_projects(self, model_cls: type[Base], user_id: any) -> List[Base]:
        result = await self.session.execute(select(model_cls).filter(model_cls.user_id == str(user_id)))
        return result.scalars().all()
    
    async def get_all_tasks_full(self, model_cls: type[Base], id_uuid: any) -> List[Base]:
        query = select(model_cls).options(joinedload(model_cls.task_items)).filter(model_cls.user_id == str(id_uuid))
        result = await self.session.execute(query)
        return result.scalars().unique().all()
    
    async def get_task_by_id(self, model: Base, id: int):
        result = await self.session.execute(select(model).filter(model.id == id))
        entity = result.scalars().first()
        if entity is None:
            return None
        return entity
    
    async def update_task_item(self, model: Base, task_item_id: int) -> TaskItem:
        update_statement = (
            update(TaskItem)
            .where(TaskItem.id == task_item_id)
        )

        if model.done is not None:
            update_statement = update_statement.values(done=model.done)

        if model.name is not None:
            update_statement = update_statement.values(name=model.name)

        await self.session.execute(update_statement)
        await self.session.commit()

    async def update_task(self, model: Base, task_id: int) -> Task:
        update_statement = (
            update(Task)
            .where(Task.id == task_id)
        )

        if model.name is not None:
            update_statement = update_statement.values(name=model.name)

        if model.description is not None:
            update_statement = update_statement.values(description=model.description)

        if model.project_id is not None:
            update_statement = update_statement.values(project_id=model.project_id)

        await self.session.execute(update_statement)
        await self.session.commit()

    async def update_project(self, model: Base, project_id: int) -> Project:
        update_statement = (
            update(Project)
            .where(Project.id == project_id)
        )
        update_statement = update_statement.values(name=model.name)

        await self.session.execute(update_statement)
        await self.session.commit()
    
    async def get_items_for_task(self, model_cls: type[Base], task_id: int) -> List[Base]:
        result = await self.session.execute(select(model_cls).filter(model_cls.task_id == task_id))
        return result.scalars().all()
    
    async def delete_task(self, task_id: int):
        task = await self.session.execute(select(Task).where(Task.id == task_id))
        task_obj = task.scalar_one_or_none()
        if task_obj:
            await self.session.delete(task_obj)
            await self.session.commit()
            return True
        
    async def delete_project(self, project_id: int):
        task = await self.session.execute(select(Project).where(Project.id == project_id))
        task_obj = task.scalar_one_or_none()
        if task_obj:
            await self.session.delete(task_obj)
            await self.session.commit()
            return True
    
        
    async def delete_item(self, item_id: int):
        task = await self.session.execute(select(TaskItem).where(TaskItem.id == item_id))
        task_obj = task.scalar_one_or_none()
        if task_obj:
            await self.session.delete(task_obj)
            await self.session.commit()
            return True
    
    async def checkUsername(self, username: str):
        result = await self.session.execute(select(User).filter(User.username == username))
        user = result.scalars().first()
        await self.session.close()
        return {'status': user}


async def get_crud_db(session: AsyncSession = Depends(get_async_session)):
    yield DBCRUD(session)
