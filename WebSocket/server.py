import socket
import time

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_ip= "192.168.43.103"
socket_port = 773

server_time = time.time()

socket.bind((socket_ip, socket_port))
socket.listen(10)


while True:
    client, (ip, port) = socket.accept()
    print("one client is connected")
    print(client)
    print(port)
    print(ip)
    client.send(b"man payam az server hastam siyamak")
    # c.send(b"server time is : {}", server_time)
    client.close()
