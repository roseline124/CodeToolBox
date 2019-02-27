import socket
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('IP주소', 8080))
sock.send('Hello'.encode())
