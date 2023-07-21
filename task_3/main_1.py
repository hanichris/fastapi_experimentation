#!/usr/bin/env python3
"""Providing additional information and validation for parameters.

`Annotated` - Enables addition of metadata to the parameters.
"""
from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/items/')
async def read_items(
        q: Annotated[
            str | None, Query(min_length=3, max_length=50, pattern='^fixedquery$')
            ] = None):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results

