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
    project_id = Column(Integer, ForeignKey('projects.id'))  # Foreign key referencing the Project's id
    project = relationship("Project", backref='tasks')  # Establishing the relationship
    user = relationship(User, backref='tasks')
    task_items = relationship("TaskItem", cascade="all, delete", back_populates="task")
    class Config:
        orm_mode = True
        


class TaskCreate(BaseModel):
    name: str
    description: str
    user_id: str
    project_id: int
    class Config:
        orm_mode = True


class TaskRead(BaseModel):
    name: str
    description: str
    user_id: str
    project_id: int
    task_items: List
    class Config:
        orm_mode = True

