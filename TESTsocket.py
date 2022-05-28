import socket,time

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

server_socket.bind(('',7891))
server_socket.listen(8)
new_socket,addr = server_socket.accept()
new_socket.setblocking(False)
print("Start")
while True:
    try:
        time.sleep(2)
        recv=new_socket.recv(1024).decode()
    except Exception as e:
        print(e)
    else:
          if recv:
            print("fasdfasdfasdfasdfasdf",recv)
          else:
              print("00000000000000000")
  
        
    