import asyncio
import random
import time
from fastapi import FastAPI

app = FastAPI()


@app.get("/foobar")
async def foobar():
    return {"message": "hello world"}


@app.get("/hello")
async def hello():
    return {"message": "world"}


@app.get("/invalid")
async def invalid():
    raise ValueError("Invalid ")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/ping")
async def health_check():
    return "pong"


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    if item_id % 2 == 0:
        # mock io - wait for x seconds
        seconds = random.uniform(0, 3)
        await asyncio.sleep(seconds)
    return {"item_id": item_id, "q": q}


@app.get("/exception")
async def exception():
    time.sleep(random.uniform(0, 3))
    raise Exception("exception")
