import http.server
import socketserver

PORT = 8010
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server is running on port", PORT)
    httpd.serve_forever()
