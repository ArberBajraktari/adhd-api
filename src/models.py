from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel



engine = create_engine('postgresql://arber:password@localhost:54320/adhd_helper')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    pwd = Column(String(255), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)
    gender = Column(String(25), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, pwd={self.pwd}, first_name={self.first_name}, last_name={self.last_name}, gender={self.gender})>"


class UserCreate(BaseModel):
    username: str
    email: str
    pwd: str
    date_of_birth: str
    first_name: str
    last_name: str
    gender: str


class UserUpdate(BaseModel):
    username: str = None
    email: str = None
    pwd: str = None
    date_of_birth: str = None
    first_name: str = None
    last_name: str = None
    gender: str = None


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


def create_user(db, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        update_data = user.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user


def delete_user(db, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user


def get_all_users(db):
    return db.query(User).all()
