# pip install fastapi hypercorn
from fastapi import FastAPI
from hypercorn.config import Config
from hypercorn.asyncio import serve
import asyncio
from pathlib import Path

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    key_path = Path(__file__).parent / "key/summer-py-server.key"
    cert_path = Path(__file__).parent / "key/summer-py-server.crt"
    config = Config()
    config.bind = ["10.231.3.168:9092"]  # HTTP/2.0 绑定地址
    config.certfile = cert_path  # SSL 证书文件路径
    config.keyfile = key_path  # SSL 私钥文件路径
    # config.quic_bind = ["127.0.0.1:9093"]  # QUIC 绑定地址
    # config.quic_version = "h3-29"  # 使用的 QUIC 版本

    asyncio.run(serve(app, config))
