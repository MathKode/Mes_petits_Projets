import socket

Host="192.168.1.18"
Port=15151

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.connect((Host,Port))

socket.close()
