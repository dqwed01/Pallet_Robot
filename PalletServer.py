import socket
import queue

commandQueue = queue.Queue()
sSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print("Socket successfully created")

serverAddress = socket.gethostbyname(socket.gethostname()) #IT NEEDS TO BE PRIVATE IPV4 ADDRESS
port = 3005

sSocket.bind((serverAddress, port))
print(f"Server created at {serverAddress}:{port}")

sSocket.listen(1)

while True:
    comm_sSocket, address = sSocket.accept()
    