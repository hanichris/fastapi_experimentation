#!/usr/bin/env python3
"""Creating nested models.

This is the case when the type of a Pydantic model attribute is itself a Pydantic
Model."""
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    name: str
    url: HttpUrl


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: list[Image] | None = None

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, 'item': item}

