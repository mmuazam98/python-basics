import socket
def client_program():
    host = socket.gethostname()  
    port = 5000  

    client_socket = socket.socket()  
    client_socket.connect((host, port))

    message = "Please send your message"  

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  
        data = client_socket.recv(1024).decode()  

        print('Received from server: ' + data)  

        if data == "ping":
            print("Pong")
        else:
            print("Dropped")
            break

    client_socket.close()  


if __name__ == '__main__':
    client_program()
