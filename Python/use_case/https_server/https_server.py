import http.server
import ssl

server_address = ("0.0.0.0", 443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    server_side=True,
    certfile="key/py-server/summer-py-server.crt",
    keyfile="key/py-server/summer-py-server.key",
    ssl_version=ssl.PROTOCOL_TLS,
)
httpd.serve_forever()
