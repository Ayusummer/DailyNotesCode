'''
Author: 咸鱼型233
Date: 2022-04-25 16:35:15
LastEditors: 咸鱼型233
LastEditTime: 2022-04-28 14:39:30
FilePath: \VbenBackend\sql_app\models.py
Description: 创建 database models
Copyright (c) 2022 by 咸鱼型233, All Rights Reserved.
'''
'''
-*- encoding: utf-8 -*-
@文件: models.py
@时间: 2022/04/19 08:45:45
@作者: 咸鱼型233
@说明: 创建 database models
'''
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, FLOAT
from .database import Base
class Staff(Base):
    """员工类
    """
    __tablename__ = "Staff"

    id = Column(Integer, primary_key=True, index=True)
    staffNo = Column(String)
    name = Column(String)
    sex = Column(String)
    birthday = Column(String)
    phone = Column(String)
    education = Column(String)
    namePinyin = Column(String)
