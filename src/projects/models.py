from typing import Optional
from sqlalchemy import CHAR, UUID, Column, ForeignKey, Integer, String, Text
from pydantic import BaseModel
from sqlalchemy.orm import relationship
from typing import List
from ..db.base import Base
from ..users.models import User
from ..task_item.models import TaskItem

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=False, nullable=False)
    description = Column(Text)
    user_id = Column(CHAR(36), ForeignKey('user.id'))
    user = relationship(User, backref='projects')
    
    class Config:
        orm_mode = True
        


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str]
    user_id: Optional[str]
    class Config:
        orm_mode = True


class ProjectRead(BaseModel):
    name: str
    description: str
    task_items: List
    class Config:
        orm_mode = True

