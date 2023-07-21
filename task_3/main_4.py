#!/usr/bin/env python3
"""Providing additional information and validation for parameters.

`Annotated` - Enables addition of metadata to the parameters.
Possible to declare additional metadata.
"""
from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/items/')
async def read_items(
        q: Annotated[
            str | None,
            Query(
                alias='item-query',
                title='Query string',
                description='Query string for the items to search in the database',
                min_length=3,
                max_lenght=5,
                deprecated=True
                )] = None):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results

