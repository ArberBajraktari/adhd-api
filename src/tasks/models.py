from typing import Optional
from sqlalchemy import CHAR, UUID, Column, ForeignKey, Integer, String, Text
from pydantic import BaseModel
from sqlalchemy.orm import relationship
from ..db.base import Base
from ..users.models import User

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=False, nullable=False)
    description = Column(Text)
    user_id = Column(CHAR(36), ForeignKey("user.id"))
    user = relationship("User", back_populates="tasks")

    class Config:
        orm_mode = True


class TaskCreate(BaseModel):
    name: str
    description: str
    userId: str
    class Config:
        orm_mode = True


class TaskRead(BaseModel):
    name: str
    description: Optional[str]
    userId: Optional[str]
    class Config:
        orm_mode = True

    
