#!/usr/bin/env python3
"""Providing multiple examples of use of the api."""
from typing import Annotated

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put('/items/{item_id}')
async def update_item(
        *,
        item_id: int,
        item: Annotated[
            Item,
            Body(
                examples=[
                    {
                        "name": "Foo",
                        "description": "A very nice item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                    {
                        "name": "Bar",
                        "price": "35.4",
                    },
                    {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                 ],
            ),
        ]
    ):
    return {'item_id': item_id, 'item': item}

