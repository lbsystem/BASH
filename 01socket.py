import socket
import time

from pip import main

g=[]

def main():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('',7890))
    server_socket.listen(8)

    server_socket.setblocking(False)

    while True:
        try:
            new_socket,new_addr = server_socket.accept()
        except Exception as e:
            print('-----1----',e)
        else:
            new_socket.setblocking(False)
            g.append(new_socket)
        
        print(g)

        time.sleep(0.5)
        for client_socket in g:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
               
            except Exception as e:
                print("-----2-----",e)
            else:
                if recv_data:
                    print("%s>>>>>>>%s" % (str(client_socket.getpeername()),recv_data))
                else: 
                    print("%s" % (str(client_socket.getpeername())))
                    client_socket.close()


if __name__ == "__main__":
    main()