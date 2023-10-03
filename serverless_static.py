import os
import urllib.parse
import urllib.request
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the directory where your static files are located
STATIC_DIR = "staticfiles"

class StaticFileHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Get the requested URL path
            file_path = urllib.parse.unquote(self.path)

            # Combine the requested path with the static directory
            file_path = os.path.join(STATIC_DIR, file_path.lstrip('/'))

            # Check if the file exists
            if not os.path.exists(file_path):
                self.send_response(HTTPStatus.NOT_FOUND)
                self.end_headers()
                self.wfile.write(b"File not found")
                return

            # Read and serve the static file
            with open(file_path, "rb") as file:
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-type", "application/octet-stream")
                self.end_headers()
                self.wfile.write(file.read())
        except Exception as e:
            self.send_response(HTTPStatus.INTERNAL_SERVER_ERROR)
            self.end_headers()
            self.wfile.write(f"Internal Server Error: {str(e)}".encode())

def run_server():
    server = HTTPServer(("0.0.0.0", 3000), StaticFileHandler)
    print("Server is running at http://localhost:3000")
    server.serve_forever()

if __name__ == "__main__":
    run_server()