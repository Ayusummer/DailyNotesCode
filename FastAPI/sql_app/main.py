'''
Author: 咸鱼型233
Date: 2022-04-25 20:39:39
LastEditors: 咸鱼型233
LastEditTime: 2022-04-26 16:58:02
FilePath: \VbenBackend\sql_app\main.py
Description: Main FasrAPI app
Copyright (c) 2022 by 咸鱼型233, All Rights Reserved.
'''
'''
-*- encoding: utf-8 -*-
@文件: sql_app\main.py
@时间: 2022/04/25 20:39:43
@作者: 咸鱼型233
@说明: Main FasrAPI app
'''


from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
# create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 创建 Staff
@app.post("/staffs/", response_model=schemas.Staff)
def create_staff(staff: schemas.StaffCreate, db: Session = Depends(get_db)):
    # 检查是否已存在, 不存在则创建, 存在则返回错误信息
    db_staff = crud.getStaffByStaffNo(db, staff.staffNo)
    if db_staff:
        raise HTTPException(status_code=400, detail="Staff already exists")
    return crud.create_staff(db=db, staff=staff)

# 获取所有 Staff
@app.get("/getAllStaffs/", response_model=List[schemas.Staff])
def read_staffs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    staffs = crud.get_staffs(db, skip=skip, limit=limit)
    return staffs

# 通过 id 读取 Staff
@app.get("/staffs/{id}", response_model=schemas.Staff)
def read_staff(id: int, db: Session = Depends(get_db)):
    db_staff = crud.get_staff(db, id=id)
    if db_staff is None:
        raise HTTPException(status_code=404, detail="Staff not found")
    return db_staff

# 通过 staffNo 读取 Staff
@app.get("/staffs/staffNo/{staffNo}", response_model=schemas.Staff)
def read_staff_by_staffNo(staffNo: str, db: Session = Depends(get_db)):
    db_staff = crud.get_staff_by_staffNo(db, staffNo=staffNo)
    if db_staff is None:
        raise HTTPException(status_code=404, detail="Staff not found")
    return db_staff

# 更新 Staff.
@app.put("/staffs/{id}", response_model=schemas.Staff)
def update_staff(id: int, staff: schemas.StaffBase, db: Session = Depends(get_db)):
    db_staff = crud.get_staff(db, id=id)
    if db_staff is None:
        raise HTTPException(status_code=404, detail="Staff not found")
    return crud.update_staff(db=db, db_staff=db_staff, staff=staff)