from async_timeout import timeout
from gevent import monkey; monkey.patch_all()
import gevent,time
import socket
import random
from ftplib import FTP
def ftp_login(ip):

    ftp = FTP()

    timeout = 30

    port = 21

    ftp.connect(ip,port,timeout) 
    ftp.login('anonymous','admin') # 登录

    print(ftp.getwelcome()) # 获得欢迎信息

def rand_port():
    ports=[i for i in range(30000,65000)]
    def inner():
        port_choice = random.choice(ports)
        ports.remove(port_choice)
        return int(port_choice)
    return inner


def ssh_ack(ip):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    port=rand_port()
    client.bind(("",port()))
    client.settimeout(3)
    # ip=f"42.225.46.{ip}"
    ip='192.168.2.33'
    try:
        client.connect((ip,8291))
        
       
        
    except:
        return
    try:
       
        client.send(b"fasdf")
        client.close()
        return
        # recv=client.recv(1024)
    except:
        return
    if recv:
        # ftp_login(ip)
        print(ip,recv)
    

        
        

    client.close()

while True:
    tasks=[gevent.spawn(ssh_ack,i)for i in range(1,5500)]


    gevent.joinall(tasks)