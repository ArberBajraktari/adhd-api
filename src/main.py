from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .api import api 
from .config import settings
from .db.session import create_db_and_tables

# Set up the FastAPI application
app = FastAPI(
    title=settings.API_NAME
)
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
#     allow_credentials=settings.ALLOW_CREDENTIALS,
#     allow_methods=settings.ALLOW_METHODS,
#     allow_headers=settings.ALLOW_HEADERS,
# )

app.include_router(api.router)

@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()