import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('IP주소', 8080)) 

while 1 : 
    data = input()
    socket.send(data.encode())
    data2 = socket.recv(65535)
    print('received data : ', data2.decode())

