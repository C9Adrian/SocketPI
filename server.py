#192.168.1.27
import socket
import pickle

HOST = '192.168.1.27'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been established!")
	clientsocket.send(bytes("Welcome to the server!", "utf-8"))
