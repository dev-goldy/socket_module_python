#client B 
import socket
c = socket.socket()
c.connect(("localhost", 9999))
hello = input("send message >> ")
c.send(bytes(hello,'utf-8'))
p = c.recv(1024).decode()
print("recieved >> ", p)
