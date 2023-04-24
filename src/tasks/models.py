from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from ..db.base import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(50), unique=True, nullable=False)


class TaskCreate(BaseModel):
    name: str
    description: str



class TaskRead(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True
