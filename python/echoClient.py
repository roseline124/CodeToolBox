import socket
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('IP주소', 8080))

whoAreYou = sock.recv(65535)
print("Server :", whoAreYou.decode())

sock.send('옥냥이'.encode())

greeting = sock.recv(65535)
print("Server :", greeting.decode())
