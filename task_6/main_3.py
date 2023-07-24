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


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.post('/offers/')
async def create_offer(offer: Offer):
    return offer

