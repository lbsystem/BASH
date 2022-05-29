import select
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("",7890))
s.listen(8)
#listen是在系统后台进程运行和程序进程没关系
epoll=select.epoll()

epoll.register(s.fileno(),select.EPOLLIN|select.EPOLLET)
#服务器初始socket 注册到epoll里
print("server socket",s.fileno())
header="HTTP/1.1 404 not found\r\nContent_length: 0\r\n\r\nfasdfasdfasdf".encode()
connections={}
#client第一次来的新连接会连接到服务器初始socket 并由epoll.poll通知有新连接到来
#然后释放阻塞 然后由accept 产生一个新的socket 来和client进行正式的通讯
while True:
    epoll_list = epoll.poll()
    #epoll.poll 会阻塞 有新数据的情况下回返回 fd值 和 epollin值 或者epollet值 也就是events值
    print("start",epoll_list)

    for fd, events in epoll_list:
        #fd 值为系统socket文件描述符的值
        
        if fd == s.fileno():
            #fd 值等于服务器初始fd值 证明为初始连接 进入accept模式
            new_socket,new_addr = s.accept()
            # print("accept",new_socket)

            #socket三次握手是在listen中完成，accept只从完成连接的队列中拿出一个连接
            #用服务器初始的socket 进行阻塞 等待连接到来并产生新的socket
            new_conn = new_socket.fileno()
            #拿出一个fd值
            connections[new_conn]=[]
            # print("have a new client%s" % str(new_addr))
            connections[new_conn].append(new_socket)
            #对应fd值保存一个新的套接字
            connections[new_conn].append(new_addr)
            #保存一个连接地址信息
            epoll.register(new_socket.fileno(),select.EPOLLIN|select.EPOLLET)
            #把新的socket 加入到epoll池
        elif events == select.EPOLLIN:
            #当epoll 通知有新的收取事件
            recvData = connections[fd][0].recv(1024).decode("utf-8")
            connections[fd][0].send(header)
            if recvData:
                print('recv:%s' % recvData)
            else:
                epoll.unregister(fd)
                #取消对应的套接字在epoll 的注册
                connections[fd][0].close()
                #关闭对应的套件字
                print("%s---offline---" % str(connections[fd][1]))
                del connections[fd]
                
