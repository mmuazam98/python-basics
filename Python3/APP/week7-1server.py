import time
import socket
import sys
s066 = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080
s066.bind((host_name, port))
print("Binding successful!")
print("This is your IP: ", s_ip)
name = input('Enter name: ')
s066.listen(1)
conn, add = s066.accept()
print("Received connection from ", add[0])
print('Connection Established. Connected From: ', add[0])
client = (conn.recv(1024)).decode()
print(client + ' has connected.')
conn.send(name.encode())
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
