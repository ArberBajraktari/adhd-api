from typing import Optional
from sqlalchemy import CHAR, UUID, Column, ForeignKey, Integer, String, Text
from pydantic import BaseModel
from sqlalchemy.orm import relationship
from ..db.base import Base
from ..tasks.models import Task

class TaskItem(Base):
    __tablename__ = "task_item"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, unique=False, nullable=False)
    task_id = Column(Integer, ForeignKey('tasks.id'))  # Assuming UUID is in the format XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    task = relationship(Task, backref='task_item')

    class Config:
        orm_mode = True


class TaskItemCreate(BaseModel):
    name: str
    task_id: int
    class Config:
        orm_mode = True


class TaskItemRead(BaseModel):
    name: str
    task_id: int
    class Config:
        orm_mode = True

    
