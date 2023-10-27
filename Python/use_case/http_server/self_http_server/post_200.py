# 允许接收 post 数据, 存入当前文件所在目录下的 post_data.txt 文件中
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from pathlib import Path

current_file_path = Path(__file__).parent
os.chdir(current_file_path)

POST_DATA_FILE_PATH = Path(__file__).parent / "post_data.txt"
SERVER_ADDRESS = ("0.0.0.0", 80)


class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        return super().do_GET()

    def do_POST(self) -> None:
        # 获取 post 数据的长度
        content_length = int(self.headers["Content-Length"])
        # 获取 post 数据
        post_data = self.rfile.read(content_length)
        # 将 post 数据写入当前文件所在目录下的 post_data.txt 文件中
        with open(POST_DATA_FILE_PATH, "wb") as f:
            f.write(post_data)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"success": true,  "code": 200,}')


httpd = HTTPServer(SERVER_ADDRESS, CustomHTTPRequestHandler)
httpd.serve_forever()
