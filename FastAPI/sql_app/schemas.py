'''
Author: 咸鱼型233
Date: 2022-04-25 16:35:15
LastEditors: 咸鱼型233
LastEditTime: 2022-04-25 19:23:33
FilePath: \VbenBackend\sql_app\schemas.py
Description: 创建 Pydantic models
Copyright (c) 2022 by 咸鱼型233, All Rights Reserved.
'''
'''
-*- encoding: utf-8 -*-
@文件: sql_app\schemas.py
@时间: 2022/04/25 19:13:54
@作者: 咸鱼型233
@说明: 创建 schemas
'''
from typing import List, Optional

from pydantic import BaseModel

class StaffBase(BaseModel):
    staffNo: str
    name: str
    sex: str
    birthday: str
    phone: str
    education: str
    namePinyin: str

class StaffCreate(StaffBase):
    pass

class Staff(StaffBase):
    id: int

    class Config:
        orm_mode = True