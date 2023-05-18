from typing import Optional
from sqlalchemy import CHAR, UUID, Column, ForeignKey, Integer, String, Text, Boolean
from pydantic import BaseModel
from sqlalchemy.orm import relationship
from ..db.base import Base

class TaskItem(Base):
    __tablename__ = "task_item"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, unique=False, nullable=False)
    done = Column(Boolean, nullable=False)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    task = relationship("Task", back_populates="task_items")

    class Config:
        orm_mode = True

class TaskItemUpdate(BaseModel):
    name: Optional[str]
    done: Optional[bool]

class TaskItemCreate(BaseModel):
    name: str
    task_id: int
    done: bool
    class Config:
        orm_mode = True


class TaskItemRead(BaseModel):
    name: str
    task_id: int
    done: bool
    
    class Config:
        orm_mode = True

    
