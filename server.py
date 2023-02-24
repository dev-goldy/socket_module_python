#check for free port numbers if your using in termux 

import socket 
s = socket.socket()                #creating server socket 
s.bind(("localhost", 9999))        #you change port number use free one  
s.listen(4)                        #will listen to 4 connections
while True:
  c, addr = s.accept()
  print("connected with client >> ", addr)
  c.send(bytes("messages from server >> hello friend ", "utf-8"))
  c.close()
