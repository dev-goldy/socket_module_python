#will update more that file in future 

import socket 
a = socket.socket()
a.connect(("localhost", 9999))
message = input("send message >> ")
a.send(bytes(message, "utf-8"))
print(a.recv(1024).decode())
