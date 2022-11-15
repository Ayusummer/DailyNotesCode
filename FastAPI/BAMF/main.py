'''
Author: 咸鱼型233
Date: 2022-04-25 15:16:57
LastEditors: 咸鱼型233
LastEditTime: 2022-04-26 21:15:15
FilePath: \VbenBackend\app\main.py
Description: 
Copyright (c) 2022 by 咸鱼型233, All Rights Reserved.
'''
from fastapi import Depends, FastAPI
import uvicorn
from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)