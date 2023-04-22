# # Database connection details
# db_host = 'localhost'  # replace with your database host
# #db_host = 'localhost'  # replace with your database host
# db_port = 54320  # replace with your database port
# db_name = 'adhd_helper'  # replace with your database name
# db_user = 'arber'  # replace with your database username
# db_password = 'password'  # replace with your database password




from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import asyncpg
from datetime import date
from .models import UserCreate, create_user, get_db, update_user, User, UserUpdate
from .api import api 
from .config import settings



# Set up the FastAPI application
app = FastAPI(
    title=settings.API_NAME
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=settings.ALLOW_CREDENTIALS,
    allow_methods=settings.ALLOW_METHODS,
    allow_headers=settings.ALLOW_HEADERS,
)

app.include_router(api.router)

# Set up the database connection
SQLALCHEMY_DATABASE_URL = "postgresql://arber:password@localhost:54320/adhd_helper"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# # Define the API endpoints
# @app.post("/create_user")
# def create_users(user: UserCreate):
#     db = get_db()
#     create_user(db, user)
#     return {"a": "b"}
#     #create_user(user)

# # Endpoint to delete a user by their id
# @app.delete("/users/{user_id}")
# def delete_user(user_id: int):
#     db = get_db()
#     user = db.query(User).filter(User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     # Delete the user
#     db.delete(user)
#     db.commit()
#     return {"message": "User deleted"}

# # Endpoint to update a user by their id
# @app.put("/users/{user_id}")
# def update_user(user_id: int, user: UserUpdate):
#     # Check if the user exists
#     db = get_db()
#     db_user = db.query(User).filter(User.id == user_id).first()
#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     for attr, value in user.dict(exclude_unset=True).items():
#         setattr(db_user, attr, value)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user