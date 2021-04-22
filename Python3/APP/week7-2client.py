import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1245

# s.bind((host,port))
s.connect((host, port))
con = True
while con:
    msg = s.recv(1024)
    msg = msg.decode("utf-8")
    print(msg)
    if(msg == "quit"):
        con = False
        s.close()
