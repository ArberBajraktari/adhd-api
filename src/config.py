import logging
from functools import lru_cache
from typing import List
from pydantic import BaseSettings, AnyHttpUrl, RedisDsn, PostgresDsn, EmailStr


class Settings(BaseSettings):
    ENVIRONMENT: str = "dev"
    DOMAIN: str = "adhd-planner.localhost"
    API_NAME: str = "adhd-api"
    API_VERSION: str = "1.0.0"
    API_URL_PREFIX: str = "/api/v1"
    API_SECRET_KEY: str = "changeme"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 3600
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:8009"
    ]
    ALLOW_CREDENTIALS = True
    ALLOW_METHODS = ["*"]
    ALLOW_HEADERS = ["Content-Type", "Set-Cookie"]


logger = logging.getLogger("uvicorn")


@lru_cache()
def get_settings() -> BaseSettings:
    settings = Settings()
    logger.info(f"Loading config settings from environment.")
    return settings


settings = get_settings()
