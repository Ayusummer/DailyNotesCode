from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
from pathlib import Path

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
