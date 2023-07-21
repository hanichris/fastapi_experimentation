#!/usr/bin/env python3
"""Providing additional information and validation for parameters.

`Annotated` - Enables addition of metadata to the parameters.
"""
from fastapi import FastAPI, Query, Path
from typing import Annotated

app = FastAPI()

@app.get('/items/{item_id}')
async def read_items(
        item_id: Annotated[int, Path(title='The ID of the item to get')],
        q: Annotated[str | None, Query(alias='item-query')] = None):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results

