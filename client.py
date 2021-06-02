import socket

host, port = ('localhost',5566)

try :
    socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.connect((host,port))
    print("Client Connecté")
except :
    print('Serveur Non connecté')
finally:
    socket.close()
    