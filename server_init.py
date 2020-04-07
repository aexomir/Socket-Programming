from socket import *

# CREATING SOCKET
socket = socket(AF_INET,SOCK_STREAM)
print('Socket Created Succesfully')



# defining listen() port
PORT = 2020

# BINDING SOCKET TO THE PORT
# GFG NOTE:
# Next bind to the port
# # we have not typed any ip in the ip field
# # instead we have inputted an empty string
# # this makes the server listen to requests
# # coming from other computers on the network
socket.bind(('',PORT))

# LISTENING TO INCOMING PACKETS TO THE PORT
# GFG NOTE:
#we put the server into listen mode.5
# here means that 5 connections are kept
# waiting if the server is busy and if
# a 6th socket trys to connect then the
# connection is refused.
socket.listen(5)

# a forever loop which continues until error() or interrupt()
while True:
    conn,addr = socket.accept()
    print(f'Got Connection From {addr}\n')

    conn.send(b'Thank You For Connecting to this Port\n')

    conn.close()

