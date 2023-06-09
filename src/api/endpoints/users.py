import requests
from fastapi import Depends, Request, Response
#from ...db import create_db_and_tables
from ...users.models import UserCreate, UserRead, UserUpdate, User
from ...users.manager import auth_backend, current_active_user, fastapi_users
from fastapi import APIRouter
from ...crud.db import get_crud_db

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

@router.get("/checkUsername")
async def get_tasks(username: str, db = Depends(get_crud_db)):
    tasks = await db.checkUsername(username)
    return tasks

@router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}