'''
Author: 咸鱼型233
Date: 2022-04-26 20:10:30
LastEditors: 咸鱼型233
LastEditTime: 2022-04-26 20:33:02
FilePath: \VbenBackend\app\internal\admin.py
Description: 
Copyright (c) 2022 by 咸鱼型233, All Rights Reserved.
'''
from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}
