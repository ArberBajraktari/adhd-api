import uuid
from enum import Enum
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from fastapi_users import schemas
from sqlalchemy import Column, Boolean, String
from ..db.base import Base


class GenderEnum(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class UserCreate(schemas.BaseUserCreate):
    # gender: str
    pass


class UserUpdate(schemas.BaseUserUpdate):
    # gender: str
    pass

class UserRead(schemas.BaseUser[uuid.UUID]):
    # gender: str
    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass


