#!/usr/bin/env python3
"""Treating singular values as a part of a Request Body."""
from typing import Annotated

from fastapi import FastAPI, Body
from pydantic import BaseModel

class User(BaseModel):
    username: str
    full_name: str | None = None

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.put('/items/{item_id}')
async def update_item(
        item_id: int,
        user: User,
        item: Item,
        importance: Annotated[int, Body()]):
    return {'item_id': item_id, 'item': item, 'user': user, 'importance': importance}

