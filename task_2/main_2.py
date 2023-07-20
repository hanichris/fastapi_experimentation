#!/usr/bin/env python3
"""Defining request body, query and path parameters simultaneously."""
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.put('/items/{item_id}')
async def create_item(item_id: int, item: Item, q: str | None = None):
    response = {'item_id': item_id, **item.dict()}
    if q:
        response.update({'q': q})
    return response

