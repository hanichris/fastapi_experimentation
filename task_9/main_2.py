#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: str | None = None


@app.post('/user/')
async def create_user(user: UserIn) -> UserIn:
    return user

