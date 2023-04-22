from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from ..db.base import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(50), unique=False, nullable=False)


class TaskCreate(BaseModel):
    name: str


class TaskRead(BaseModel):
    name: str
