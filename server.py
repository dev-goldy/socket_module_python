#check for free port numbers if your using in termux 
import socket

s = socket.socket()
IP = "localhost"
PORT = 9999
s.bind((IP, PORT))
s.listen(2)
print("Listening...")

while True:
    a, addr1 = s.accept()
    print("Connected with client 1:", addr1)
    
    c, addr2 = s.accept()
    print("Connected with client 2:", addr2)

    while True:
        message = a.recv(1024).decode()
        if message == "hello":
            print("Client 1 says hello")
            c.send(bytes("hello", 'utf-8'))
        else:
            print("Client 1 disconnected")
            c.send(bytes("bye", 'utf-8'))
            break

        message = c.recv(1024).decode()
        if message == "hello":
            print("Client 2 says hello")
            a.send(bytes("bye", 'utf-8'))
            break
        else:
            print("Client 2 disconnected")
            a.send(bytes("bye", 'utf-8'))
            break

    a.close()
    c.close()

