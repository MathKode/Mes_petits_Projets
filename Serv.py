import socket

host, port = ('',5566)

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((host,port))
print("Le Serveur est démarré !")

while True:
    socket.listen(5)
    connectin, address = socket.accept()
    print('En écoute...')

connectin.close()
socket.close()