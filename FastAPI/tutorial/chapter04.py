#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from typing import Optional, List

from fastapi import (
    APIRouter,  # 路由
    status,  # HTTP status codes
    Form,  # 用于处理表单数据
    File,  # 文件处理
    UploadFile,  # 用于处理文件上传
    HTTPException,  # 用于处理HTTP异常
)
from pydantic import BaseModel, EmailStr

app04 = APIRouter()

"""Response Model 响应模型"""


class UserBase(BaseModel):
    username: str
    email: EmailStr
    mobile: str = "10086"
    address: str = None
    full_name: Optional[str] = None


class UserIn(UserBase):
    """用于创建 User 对象
    用户创建时需要给出 password
    但是访问用户时不应当返回 password
    """

    password: str


class UserOut(UserBase):
    pass


users = {
    "user01": {
        "username": "user01",
        "password": "123123",
        "email": "user01@example.com",
    },
    "user02": {
        "username": "user02",
        "password": "123456",
        "email": "user02@example.com",
        "mobile": "110",
    },
}


# 使用响应模型
@app04.post(
    "/response_model/", response_model=UserOut, response_model_exclude_unset=True
)
async def response_model(user: UserIn):
    """使用响应模型
    response_model_exclude_unset=True 表示默认值不包含在响应中, 仅包含实际给的值,
    如果实际给的值与默认值相同也会包含在响应中
    """
    print(user.password)  # password不会被返回
    # return user
    return users["user02"]


@app04.post(
    "/response_model/attributes",
    # response_model=UserOut,
    # response_model=Union[UserIn, UserOut],    # 取并集(也就是两个类的属性都有)
    response_model=List[UserOut],
    # 包含某些字段, 这里的 mobile 会被下面 exclude 覆盖掉
    # response_model_include=["username", "email", "mobile"],
    response_model_include=["username", "email"],  # 包含某些字段
    response_model_exclude=["mobile"],  # 排除掉某些字段
)
async def response_model_attributes(user: UserIn):
    """response_model_include列出需要在返回结果中包含的字段
    response_model_exclude列出需要在返回结果中排除的字段
    """
    # del user.password  # Union[UserIn, UserOut]后，删除password属性也能返回成功
    # return user
    return [user, user]


####### Response Status Code 响应状态码 #######


@app04.post("/status_code", status_code=200)
async def status_code():
    """返回status_code: 200"""
    return {"status_code": 200}


@app04.post("/status_attribute", status_code=status.HTTP_200_OK)
async def status_attribute():
    """返回 status.HTTP_200_OK"""
    print(type(status.HTTP_200_OK))
    return {"status_code": status.HTTP_200_OK}


"""Form Data 表单数据处理"""
# from fastapi import Form   # 用于处理表单数据


@app04.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):  # 定义表单参数
    """
    Form(...) 表示参数为必填项
    用Form类需要pip install python-multipart;
    Form类的元数据和校验方法类似Body/Query/Path/Cookie
    """
    return {"username": username}


"""Request Files 单文件、多文件上传及参数详解"""
# from fastapi import (
#     File,   # 文件处理
#     UploadFile,     # 用于处理文件上传
# )


@app04.post("/file")
async def file_(file: bytes = File(...)):
    """
    如果要上传多个文件 files: List[bytes] = File(...)
    使用File类 文件内容会以bytes的形式读入内存
    适合于上传小文件
    """
    return {"file_size": len(file)}


@app04.post("/upload_files")
async def upload_files(files: List[UploadFile] = File(...)):
    """
    如果要上传单个文件 file: UploadFile = File(...)
    使用 UploadFile 类的优势:
    1.文件存储在内存中，使用的内存达到阈值后，将被保存在磁盘中
    2.适合于图片、视频大文件
    3.可以获取上传的文件的元数据，如文件名，创建时间等
    4.有文件对象的异步接口
    5.上传的文件是Python文件对象, 可以使用write(), read(), seek(), close()操作
    """
    for file in files:
        contents = await file.read()
        print(contents)
    return {"filename": files[0].filename, "content_type": files[0].content_type}


"""【见run.py】FastAPI项目的静态文件配置"""

"""Path Operation Configuration 路径操作配置"""
# 响应的状态码, 标签, 相应的描述符, 参数类型, 参数名称, 参数描述等等


@app04.post(
    "/path_operation_configuration",  # URL 地址
    response_model=UserOut,  # 响应的结果类型
    # tags=["Path", "Operation", "Configuration"],    # 标签, 在 doc 中会按照标签进行分类展示
    summary="This is summary",  # 接口描述, 在 doc 中会在路径后面显示
    description="This is description",  # 描述, 在 doc 中会在接口描述下面显示
    response_description="This is response description",  # 响应描述, 在 doc 中会在响应结果下面显示
    # deprecated=True,    # 是否弃用
    status_code=status.HTTP_200_OK,  # 响应状态码
)
async def path_operation_configuration(user: UserIn):
    """
    Path Operation Configuration 路径操作配置
    :param user: 用户信息
    :return: 返回结果
    """
    return user.dict()


"""【见run.py】FastAPI 应用的常见配置项"""

####### Handling Errors 错误处理 #######
# HTTP Exception 以及自定义异常处理器
# from fastapi import HTTPException   # 用于处理HTTP异常


@app04.get("/http_exception")
async def http_exception(city: str):
    """默认的异常处理测试
    :param city: 城市名称
    :return: 返回城市名称
    若 city 不是 Beijing 则抛出 404 错误
    """
    if city != "Beijing":
        raise HTTPException(
            status_code=404, detail="City not found!", headers={"X-Error": "Error"}
        )
    return {"city": city}


@app04.get("/http_exception/{city_id}")
async def override_http_exception(city_id: int):
    if city_id == 1:
        raise HTTPException(status_code=418, detail="Nope! I don't like 1.")
    return {"city_id": city_id}
