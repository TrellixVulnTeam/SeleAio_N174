import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_ip = " localhost"
socket_port = 9999

socket.connect((socket_ip,socket_port))
print(socket.recv(1024))