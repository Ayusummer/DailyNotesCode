from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from pathlib import Path


class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def version_string(self) -> str:
        # 自定义的响应头的 Server 字段, 如需更改直接改下面返回的字符串即可
        return "Apache/2.4.18 (Ubuntu)"

    def do_GET(self) -> None:
        return super().do_GET()


# 在主机 9300 端口起一个 Simple http 服务, 挂在所有网卡上
# 如需指定网卡, 请将 0.0.0.0 改为对应网卡的 ip
httpd = HTTPServer(("0.0.0.0", 9300), CustomHTTPRequestHandler)
# os.chdir(os.getcwd())
current_file_path = Path(__file__).parent
os.chdir(current_file_path)
httpd.serve_forever()
