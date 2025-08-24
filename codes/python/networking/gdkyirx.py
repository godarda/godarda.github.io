# ----------------------------------------------------------------------------------------------------
# Title          : Python program for file sharing using socket programming
# File Name      : gdkyirx.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

import socket,os

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
server_socket.bind(("192.168.122.1",5000))
server_socket.listen(5)
print("TCP server waiting for client on port 5000")

while 1:
    client_socket,address=server_socket.accept()
    print("Connection established at",address)
    name=input("Enter text-file name to send ")
    path=os.path.join(os.getcwd(),name)
    file1=open(path,'rb')
    data=file1.read(1024)
    while data:
        client_socket.send(data)
        data=file1.read(1024)
        client_socket.close()
    print("File sent!")
    break;
