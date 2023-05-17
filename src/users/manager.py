import requests
import uuid
from typing import Optional

from fastapi import Depends, Request, Response
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)
from fastapi_users.db import SQLAlchemyUserDatabase
from .models import User
from ..db.session import get_user_db
from ..config import settings


SECRET = settings.API_SECRET_KEY


async def send_token_email(email: str, token: str):
    response = requests.post(
        "https://api.mailgun.net/v3/sandbox44afde8c6015448691905acff7f412b0.mailgun.org/messages",
        auth=("api", "4fc8d6545157f151ff0cf4c86559700d-db4df449-afea4493"),
        data={
            "from": "Mailgun Sandbox <postmaster@sandbox44afde8c6015448691905acff7f412b0.mailgun.org>",
            "to": ["arberbajraktari02@gmail.com"],
            "subject": "ADHD Planner - Reset password",
            "text": "Hello. \n\nThis is your token to reset your password! \nToken: " + token
        }
    )
    return response

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET
    # default 1h
    reset_password_token_lifetime_seconds: int = settings.ACCESS_TOKEN_EXPIRE_SECONDS
    verification_token_lifetime_seconds: int = settings.ACCESS_TOKEN_EXPIRE_SECONDS

    
    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        await send_token_email(user.email, token)

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


cookie_transport = CookieTransport("u")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
current_verified_user = fastapi_users.current_user(active=True, verified=True)
