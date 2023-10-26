from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
from pathlib import Path
from os import chdir

# curent_file_path, https server 的根目录放在当前文件夹下
current_file_path = Path(__file__).parent
chdir(current_file_path)

server_address = ("0.0.0.0", 443)
PEM_PATH = Path(__file__).parent / "key/py-server/summer-py-server.crt"
KEY_PATH = Path(__file__).parent / "key/py-server/summer-py-server.key"

httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(
    httpd.socket,
    certfile=PEM_PATH,
    keyfile=KEY_PATH,
    server_side=True,
    ssl_version=ssl.PROTOCOL_TLS,
)

httpd.serve_forever()
