#!/usr/bin/env python3
"""Providing usage example within a Pydantic model."""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "name": "Foo",
                        "description": "A very nice item",
                        "price": 35.4,
                        "tax": 3.2,
                    }
                ]
            }
        }

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, 'item': item}

