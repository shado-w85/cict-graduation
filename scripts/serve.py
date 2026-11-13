"""
serve.py  -  runs the website on your own computer for testing.

PURPOSE
    Opening the HTML files by double-clicking can block some browser features.
    This starts a tiny local web server so you can test at http://localhost:8000
    (the camera works on localhost even without HTTPS).

RUN:
    python scripts/serve.py
    then open  http://localhost:8000/index.html   (attendee page)
         and   http://localhost:8000/admin.html   (scanner page)
    Stop the server with Ctrl + C.
"""
import functools
import http.server
import socketserver
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent.parent / "site"
PORT = 8000


def main() -> None:
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SITE_DIR))
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving {SITE_DIR}")
        print(f"Attendee page: http://localhost:{PORT}/index.html")
        print(f"Admin scanner: http://localhost:{PORT}/admin.html")
        print("Press Ctrl + C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    main()
