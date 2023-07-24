#!/usr/bin/env python3
from fastapi import FastAPI, Header

from typing import Annotated

app = FastAPI()

@app.get('/items/')
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {'User-Agent': user_agent}

