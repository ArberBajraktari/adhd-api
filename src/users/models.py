import uuid
from enum import Enum
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from fastapi_users import schemas
from ..db.base import Base


class GenderEnum(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class UserRead(schemas.BaseUser[uuid.UUID]):
    # gender: GenderEnum
    pass


class UserCreate(schemas.BaseUserCreate):
    # gender: GenderEnum
    #shto edhe tjerat
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass

class User(SQLAlchemyBaseUserTableUUID, Base):
    pass