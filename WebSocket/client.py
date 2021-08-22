import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_ip = "192.168.43.1"
socket_port = 773

socket.connect((socket_ip,socket_port))
print(socket.recv(1024))

print("this is a message from client to se")