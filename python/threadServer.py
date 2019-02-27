import socket
import threading 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('IP주소',8080))
server_socket.listen(0)

def when() : 
    client_socket, addr = server_socket.accept() #if server linked with client, 
    t = threading.Thread(target=when) # create another thread
    t.start() #thread starts, and implements another when() 
            # and another accept().
            # then, server can receive another client's link

    while 1: 
        data = client_socket.recv(65535)
        client_socket.send(data)
        print('received data :', data.decode())
        print('connected client : ', addr[0], addr[1])

when()
