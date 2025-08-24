# ----------------------------------------------------------------------------------------------------
# Title          : Python program for two way communication using socket programming
# File Name      : gdgzlzd.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=5001

server_socket.bind((host,port))
server_socket.listen(5)
client_socket,address=server_socket.accept()

while True:
    client=client_socket.recv(2048)
    print("Client> ",client)
    client_socket.sendall(bytearray(input("You> "),"utf-8"))
client_socket.close()   
server_socket.close()
