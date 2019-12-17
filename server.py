import socket
import time

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_ip= "localhost"
socket_port = 9999

server_time = time.time()

socket.bind((socket_ip, socket_port))
socket.listen(10)


while True:
    c, addr = socket.accept()
    print("one client is connected")
    c.send(b"man payam az server hastam siyamak")
    # c.send(b"server time is : {}", server_time)
    c.close()
