import http.server
import socketserver
import os

PORT = 5678
os.chdir(os.path.join(os.path.dirname(__file__), '..', 'face-a-photos'))
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
