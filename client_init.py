from socket import *

# CREATING SOCKET
socket = socket(AF_INET,SOCK_STREAM)

# define the port you wish to connect
PORT = 2020

# CONNECTING TO LOCAL SERVER
socket.connect(('127.0.0.1',PORT))

# recieve data from server
print(socket.recv(1024))

socket.close()
