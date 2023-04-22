from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
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


async def get_crud_db(session: AsyncSession = Depends(get_async_session)):
    yield DBCRUD(session)
