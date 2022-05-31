#!/usr/bin/python3
import socketserver,time

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)#####request 和conn用法一样
        msg = self.request.recv(1024)
        print(msg)
        self.request.sendall(b"ok")
        time.sleep(0.1)
        self.request.sendall(b"ok")
    
        


server = socketserver.ThreadingTCPServer(('',12800),Myserver)
'''
其中myserver 会被阻塞循环调用'''
server.serve_forever()
