#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

import time
import uvicorn
from fastapi import FastAPI, Request, Depends  # 引入依赖
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles  # 静态文件

# from coronavirus import application
from . import app03, app04, app05, app06, app07, app08

# from fastapi.exceptions import RequestValidationError # 请求校验错误处理
# from fastapi.responses import PlainTextResponse       # 文本形式返回 response
# from starlette.exceptions import HTTPException as StarletteHTTPException  # HTTP 异常处理

# 引入 chapter05 中的全剧依赖 verify_token 和 verify_key
# from .chapter05 import verify_token, verify_key

import os  # 用于拼接路径

# FastAPI 配置项
app = FastAPI(
    # 标题
    title="FastAPI Tutorial and Coronavirus Tracker API Docs",
    # 描述
    description="FastAPI教程 \
        新冠病毒疫情跟踪器API接口文档, \
        项目代码:https://github.com/liaogx/fastapi-tutorial",
    # 版本
    version="1.0.0",
    # Swagger UI 文档地址
    docs_url="/docs",
    # ReDoc 文档地址
    redoc_url="/redocs",
    # 全剧依赖
    # dependencies = [Depends(verify_token), Depends(verify_key)]
)

# mount表示将某个目录下一个完全独立的应用挂载过来，这个不会在API交互文档中显示
static_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "./coronavirus/static")
)
# .mount()不要在分路由APIRouter().mount()调用，模板会报错
app.mount(path="/static", app=StaticFiles(directory=static_path), name="static")


# @app.exception_handler(StarletteHTTPException)  # 重写HTTPException异常处理器
# async def http_exception_handler(request, exc):
#     """
#     使用文本形式返回异常信息
#     :param request: request 请求      (这个参数不能省)
#     :param exc: 错误
#     :return:
#     """
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
#
#
# @app.exception_handler(RequestValidationError)  # 重写请求验证异常处理器
# async def validation_exception_handler(request, exc):
#     """
#     :param request: 这个参数不能省
#     :param exc:
#     :return:
#     """
#     return PlainTextResponse(str(exc), status_code=400)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """拦截所有 request 请求, 计算其在框架中的处理时间并把结果加载 response header 中
    :param request: request 请求
    :param call_next: 将接收request请求做为参数
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)  # 添加自定义的以“X-”开头的请求头
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1", "http://127.0.0.1:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(app03, prefix="/chapter03", tags=["第三章 请求参数和验证"])
app.include_router(app04, prefix="/chapter04", tags=["第四章 响应处理和FastAPI配置"])
app.include_router(app05, prefix="/chapter05", tags=["第五章 FastAPI的依赖注入系统"])
app.include_router(app06, prefix="/chapter06", tags=["第六章 安全、认证和授权"])
app.include_router(app07, prefix="/chapter07", tags=["第七章 FastAPI的数据库操作和多应用的目录结构设计"])
app.include_router(app08, prefix="/chapter08", tags=["第八章 中间件、CORS、后台任务、测试用例"])
# app.include_router(application, prefix='/coronavirus', tags=['新冠病毒疫情跟踪器API'])

if __name__ == "__main__":
    uvicorn.run(
        "run:app", host="0.0.0.0", port=8000, reload=True, debug=True, workers=1
    )
