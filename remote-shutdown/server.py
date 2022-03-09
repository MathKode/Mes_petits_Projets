import os
import socket

Host="192.168.1.18"
Port=15151

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind((Host,Port))
socket.listen(1)

client, ip = socket.accept()

print("shutdown")

client.close()
socket.close()
os.system("sudo shutdown")


