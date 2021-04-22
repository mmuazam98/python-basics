import socket

def server091():
    # get the hostname
    host091 = socket.gethostname()
    port091 = 60  # initiate port no above 1024
    s091 = socket.socket()  # get instance
    #  The bind() function takes tuple as argument
    s091.bind((host091, port091))  # bind host address and port together
    # configure how many client the server can listen simultaneously
    s091.listen(2)
    conn091, address091 = s091.accept()  # accept new connection
    print("Connection from: " + str(address091))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data091 = conn091.recv(1024).decode()
        if not data091:
            # if data is not received break
            break
        print("from connected user: " + str(data091))
        data091 = input(' -> ')
        conn091.send(data091.encode())  # send data to the client

    conn091.close()  # close the connection

if __name__ == '__main__':
    server091()
