import socketserver
import http.server

ip, port = ("192.168.43.103", 773)
def new_func():
    return http.server.SimpleHTTPRequestHandler

httpServer = socketserver.TCPServer((ip,port), new_func())
httpServer.serve_forever()