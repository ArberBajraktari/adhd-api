import uuid
from enum import Enum
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from fastapi_users import schemas
from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship
from typing import Optional
from datetime import date
from ..db.base import Base


class GenderEnum(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class UserCreate(schemas.BaseUserCreate):
    username: str
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    class Config:
        orm_mode = True


class UserUpdate(schemas.BaseUserUpdate):
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]

class UserRead(schemas.BaseUser[uuid.UUID]):
    id: uuid.UUID
    username: str
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date


class User(SQLAlchemyBaseUserTableUUID, Base):
    username = Column(String(50), nullable=False, unique=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    tasks = relationship("Task", back_populates="user") 
    class Config:
        orm_mode = True
