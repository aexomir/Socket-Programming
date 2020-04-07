# all this codes are learned from GeeksForgeeks site
# from "socket programming in Python" section
# thanks from GFG
# this is my learnings from that

# this files are gonna get updated and followed by more complex codes and connections









# importing phase...
from socket import *
import sys

# SOCKET CREATION
try:
    socket = socket(AF_INET,SOCK_STREAM)
    print('Socket Created Successfully')
except error as err:
    print('Socket Creation Failed with following error(s):\n',err)

# default port and host
PORT = 80
HOST = 'www.google.com'

# GETTING HOST IP
try:
    host_ip = gethostbyname(HOST)
except gaierror:
    print('There was an error resolving the host')
    sys.exit()

# CONNECTING TO HOST
create_connection((host_ip,PORT))
print(f'The Socket Successfully Connected to the Host on Socket: {host_ip}:{PORT}')
