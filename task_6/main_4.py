#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    name: str
    url: HttpUrl

@app.post('/images/multiple')
async def create_multiple_images(images: list[Image]):
    return images

