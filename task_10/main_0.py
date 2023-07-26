#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None


class UserDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None


def fake_password_hasher(raw_password: str):
    return f'supersecret{raw_password}'

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_db = UserDB(**user_in.dict(), hashed_password=hashed_password)
    print(f'User Input: {user_in.dict()}\tUser in DB: {user_db}')
    print('User saved! ...not really')
    return user_db

@app.post('/user/', response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

