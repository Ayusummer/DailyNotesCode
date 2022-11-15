# """
# Author: 咸鱼型233
# Date: 2022-04-26 20:05:47
# LastEditors: 咸鱼型233
# LastEditTime: 2022-04-26 20:20:50
# FilePath: \VbenBackend\app\routers\users.py
# Description: 
# Copyright (c) 2022 by 咸鱼型233, All Rights Reserved.
# """
from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
