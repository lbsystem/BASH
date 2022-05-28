import socket,time

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

server_socket.bind(('',7890))
server_socket.listen(8)
new_socket,addr = server_socket.accept()
print("Start")
while True:
    
    print(new_socket)
    recv=new_socket.recv(1024).decode()
    print(recv)
    