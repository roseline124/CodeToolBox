import socket
 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('IP주소', 8080))
server_socket.listen(0)
client_socket, addr = server_socket.accept()

client_socket.send("이름이 뭐에요?".encode()) # client에게 echo

name = client_socket.recv(65535) 
greeting =  "오홍홍 ^0^ 반가워요, "+name.decode()+" 님"
client_socket.send(greeting.encode()) # client에게 echo

print("Client :",name.decode())

