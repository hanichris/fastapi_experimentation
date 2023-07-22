#!/usr/bin/env python3
"""Working with the Request Body having multiple parameters."""
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel

from typing import Annotated

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put('/items/{item_id}')
async def update_item(
        item_id: Annotated[int, Path(title='The ID of the item to get', ge=0, le=1000)],
        q: str | None = None,
        item: Annotated[Item | None, Body(embed=True)] = None):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    if item:
        results.update({'item': item})
    return results

