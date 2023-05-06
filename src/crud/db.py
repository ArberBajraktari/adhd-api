from ..users.models import User
from fastapi import Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.future import select
from ..db.session import get_async_session
from ..db.base import Base


class DBCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, model_obj: Base):
        self.session.add(model_obj)
        await self.session.commit()
        await self.session.refresh(model_obj)
        return model_obj
    
    async def get_all_tasks(self, model_cls: type[Base]) -> List[Base]:
        result = await self.session.execute(select(model_cls))
        return result.scalars().all()
    
    async def get_by_id(self, model: Base, id: int):
        result = await self.session.execute(select(model).filter(model.id == id))
        return result.scalars().first()
    
    async def checkUsername(self, username: str):
        result = await self.session.execute(select(User).filter(User.username == username))
        user = result.scalars().first()
        await self.session.close()
        return {'status': user}


async def get_crud_db(session: AsyncSession = Depends(get_async_session)):
    yield DBCRUD(session)
