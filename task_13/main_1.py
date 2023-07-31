#!/usr/bin/env python3
from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

#GLOBAL VARIABLES FOR CONFIGURATION
SECRET_KEY = "b918a4fc2fde1f2c67a59048fd7cd3ef247b70358efc82550828db3b323e4bd0"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 301


fake_users_db = {
        "johndoe": {
            'username': 'johndoe',
            'full_name': 'John Doe',
            'email': 'johndoe@example.com',
            'hashed_password': '$2b$12$rVY5eVI761H4MkY7XNMsROkNujgykF87VbfbkSUNAUeJnwq87CbJu',
            'disabled': False,
            },
        }

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
app = FastAPI()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def get_user(db, username: str):
    user_dict = db.get(username)
    if not user_dict:
        return None
    return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

