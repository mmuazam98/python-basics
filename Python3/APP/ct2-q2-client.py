import socket

def client091():
    host091 = socket.gethostname()  # as both code is running on same pc
    port091 = 60   # socket server port number

    s091 = socket.socket()  # instantiate
    s091.connect((host091, port091))  # connect to the server

    message091 = input(" -> ")  # take input

    while message091.lower().strip() != 'bye':
        s091.send(message091.encode())  # send message
        data091 = s091.recv(1024).decode()  # receive response

        print('Received from server: ' + data091)  # show in terminal

        message091 = input(" -> ")  # again take input

    s091.close()  # close the connection

if __name__ == '__main__':
    client091()
