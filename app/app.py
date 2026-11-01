from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json

APP_VERSION = os.getenv("APP_VERSION", "v1")

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        response = {
            "application": "My Python API",
            "version": APP_VERSION,
            "message": "Hello from Minikube!"
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

server = HTTPServer(("0.0.0.0", 8000), Handler)
print("My Python API running on port 8000")

server.serve_forever()