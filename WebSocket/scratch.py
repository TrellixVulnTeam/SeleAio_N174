import socketserver
import http.server

class ReqHeader(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/admin/":
            self.wfile.write(b"Permission denied")
            b = bytes(self.headers)
            self.wfile.write(b)
        else:
            http.server.SimpleHTTPRequestHandler.do_GET(self)

ip, port = ("", 773)
httpServer = socketserver.TCPServer((ip, port), ReqHeader)
httpServer.serve_forever()