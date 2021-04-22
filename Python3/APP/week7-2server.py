import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1245
s.bind((host, port))
s.listen(5)
socketclient, address = s.accept()
print("got connection from ", address)
con = True
while con:
    msg = input("Enter Your Move:")
    socketclient.send(msg.encode("utf-8"))
    print(msg)
    if(msg == "quit"):
        con = False
        s.close()
