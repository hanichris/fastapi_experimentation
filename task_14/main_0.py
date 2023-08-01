#!/usr/bin/env python3
import time

from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


app = FastAPI()
app.add_middleware(HTTPSRedirectMiddleware)

@app.get('/')
async def main():
    return {'message': 'Hello World'}

