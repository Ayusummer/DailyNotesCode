from os import chdir
from pathlib import Path
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

CURRENT_FILE_PATH = Path(__file__).parent
chdir(CURRENT_FILE_PATH)
SERVER_ADDRESS = ("0.0.0.0", 9300)


class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        return super().do_GET()


def main():
    httpd = ThreadingHTTPServer(SERVER_ADDRESS, CustomHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
