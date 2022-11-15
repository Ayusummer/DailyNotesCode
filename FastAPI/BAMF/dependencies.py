'''
Author: 咸鱼型233
Date: 2022-04-26 19:04:35
LastEditors: 咸鱼型233
LastEditTime: 2022-04-26 20:21:57
FilePath: \VbenBackend\app\dependencies.py
Description: 
Copyright (c) 2022 by 咸鱼型233, All Rights Reserved.
'''
from fastapi import Header, HTTPException


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
