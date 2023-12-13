import socket


cSocket = socket.socket(family=socket_AF_INET, type=socket.SOCK_STREAM)
print("Socket successfully created")

serverAddress = "192.168.0.109"