import socketserver


class ClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
       print("New Client connected", self.client_address)
       data = "predifine value"
       while len(data):
           data = self.request.recv(1024)
           print("new message has been recieved from : ", self.client_address)
           self.request.send(b""" we have recieved your message %s""" %data)

ip, port = ("192.168.43.103", 773)
httpServer = socketserver.TCPServer((ip, port), ClientHandler)
httpServer.serve_forever()