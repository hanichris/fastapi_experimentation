#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

from typing import Any

app = FastAPI()


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(BaseUser):
    password: str

@app.post('/user/')
async def create_user(user: UserIn) -> BaseUser:
    return user

