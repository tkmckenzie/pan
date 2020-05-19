import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 6011))
while 1:
    data = b'123'
    client_socket.send(data)
	   
    data = client_socket.recv(5000)
    print("Your upper cased text:  " , data)

