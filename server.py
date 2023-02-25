#check for free port numbers if your using in termux 
import socket 
s = socket.socket() 
IP = "localhost" # input("enter ip addr > ") 
PORT = 9999 # int(input("enter port num > ")) 
s.bind((IP, PORT)) 
s.listen(3) 
print("listening...:") 

while True: 
    a, addr = s.accept()
    c, addr = s.accept() 
    message = c.recv(1024).decode() 
    while True:
        if a.recv(1024).decode() == "hello": 
            c.send(bytes("hello", 'utf-8'))
        elif c.recv(1024).decode() == "hello":
            a.send(bytes("bie bie :) ", 'utf-8'))
        # else:
        #     c.send(bytes("bye",'utf-8'))
        print("connected with client >> ", addr, "message >> ", message) 
        c.close() 
