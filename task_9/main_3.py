#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

from typing import Any

app = FastAPI()


class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

@app.post('/user/', response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user

