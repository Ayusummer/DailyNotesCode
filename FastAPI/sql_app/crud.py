'''
Author: 咸鱼型233
Date: 2022-04-25 16:35:15
LastEditors: 咸鱼型233
LastEditTime: 2022-04-25 21:04:58
FilePath: \VbenBackend\sql_app\curd.py
Description: 
Copyright (c) 2022 by 咸鱼型233, All Rights Reserved.
'''
'''
-*- encoding: utf-8 -*-
@文件    :curd.py
@时间    :2022/04/18 21:07:48
@作者    :咸鱼型233
@说明    :
'''
from sqlalchemy.orm import Session

from . import models, schemas

# 通过 id 读取 Staff
def get_staff(db: Session, id: int):
    return db.query(models.Staff).filter(models.Staff.id == id).first()

# 通过 staffNo 读取 Staff
def get_staff_by_staffNo(db: Session, staffNo: str):
    return db.query(models.Staff).filter(models.Staff.staffNo == staffNo).first()

# 获取所有 Staff
def get_staffs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Staff).offset(skip).limit(limit).all()

# 创建 Staff
def create_staff(db: Session, staff: schemas.StaffCreate):
    db_staff = models.Staff(**staff.dict())
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff

# 更新 staff(直接全覆盖)
def update_staff(db: Session,  db_staff:models.Staff , staff: schemas.Staff):
    db_staff.staffNo = staff.staffNo
    db_staff.name = staff.name
    db_staff.sex = staff.sex
    db_staff.birthday = staff.birthday
    db_staff.phone = staff.phone
    db_staff.education = staff.education
    db_staff.namePinyin = staff.namePinyin
    db.commit()

# 更新 staffNo
def update_staff_staffNo(db: Session, id: int, staffNo: str):
    db_staff = db.query(models.Staff).filter(models.Staff.id == id).first()
    db_staff.staffNo = staffNo
    db.commit()
    return db_staff

# 更新 name
def update_staff_name(db: Session, id: int, name: str):
    db_staff = db.query(models.Staff).filter(models.Staff.id == id).first()
    db_staff.name = name
    db.commit()
    return db_staff

# 更新 sex
def update_staff_sex(db:Session, id: int, sex:str):
    db_staff = db.query(models.Staff).filter(models.Staff.id == id).first()
    db_staff.sex = sex
    db.commit
    return db_staff

# 更新 birthday
def update_staff_birthday(db:Session, id: int, birthday:str):
    db_staff = db.query(models.Staff).filter(models.Staff.id == id).first()
    db_staff.birthday = birthday
    db.commit
    return db_staff

# 更新 phone
def update_staff_phone(db:Session, id: int, phone:str):
    db_staff = db.query(models.Staff).filter(models.Staff.id == id).first()
    db_staff.phone = phone
    db.commit
    return db_staff

# 更新 education
def update_staff_education(db:Session, id: int, education:str):
    db_staff = db.query(models.Staff).filter(models.Staff.id == id).first()
    db_staff.education = education
    db.commit
    return db_staff

# 更新 namePinyin
def update_staff_namePinyin(db:Session, id: int, namePinyin:str):
    db_staff = db.query(models.Staff).filter(models.Staff.id == id).first()
    db_staff.namePinyin = namePinyin
    db.commit
    return db_staff


# 删除 Staff
def delete_staff(db: Session, id: int):
    db_staff = db.query(models.Staff).filter(models.Staff.id == id).first()
    db.delete(db_staff)
    db.commit()
    return db_staff