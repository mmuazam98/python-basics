import time
import socket
import sys
s066 = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
sport = 8080
print('Your IP address: ', ip)
host = input("Friend's IP address:")
name = input("Enter Friend's name: ")
s066.connect((host, sport))
s066.send(name.encode())
server_name = s066.recv(1024)
server_name = server_name.decode()
print(server_name, ' has joined...')
while True:
    message = (s066.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me : ")
    s066.send(message.encode())
