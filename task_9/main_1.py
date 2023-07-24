#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel

from typing import Any

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()

@app.post('/items/', response_model=Item)
async def create_item(item: Item) -> Any:
    return item

@app.get('/items/', response_model=list[Item])
async def read_items() -> Any:
    return [
            Item(name='Portal Gun', price=42.0),
            Item(name='Plumbus', price=32.0),
        ]

