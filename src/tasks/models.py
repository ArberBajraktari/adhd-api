from typing import Optional
from sqlalchemy import CHAR, UUID, Column, ForeignKey, Integer, String, Text
from pydantic import BaseModel
from sqlalchemy.orm import relationship
from typing import List
from ..db.base import Base
from ..users.models import User
from ..task_item.models import TaskItem

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=False, nullable=False)
    description = Column(Text)
    user_id = Column(CHAR(36), ForeignKey('user.id'))  # Assuming UUID is in the format XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    user = relationship(User, backref='tasks')
    task_items = relationship("TaskItem", back_populates="task")
    class Config:
        orm_mode = True


class TaskCreate(BaseModel):
    name: str
    description: str
    user_id: str
    class Config:
        orm_mode = True


class TaskRead(BaseModel):
    name: str
    description: str
    user_id: str
    task_items: List
    class Config:
        orm_mode = True

