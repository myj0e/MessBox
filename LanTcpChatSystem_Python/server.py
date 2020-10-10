# -*- coding: UTF-8 -*-
#文件名：server.py
#项目：TCP/IP直连对话系统

import socket
import threading
import time


def rcv(conn):
    while True:
        data = conn.recv(1024)
        print ((time.strftime("%Y-%m-%d %X ",time.localtime())+"对方输入:\n"+data.decode()).center(60,' '))

def sed(s):
    while True:
        try:
            cmd = input().encode()
        except Exception as e:
            pass
        if((not cmd)):
            continue
        s.send(cmd)
        print((time.strftime("%Y-%m-%d %X", time.localtime())+"你输入:\n "+cmd.decode()).center(60,' '))
            
#服务器socket
HOST = '127.0.0.1'
PORT = 8001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)


print ('服务运行于: %s:%s' %(HOST, PORT))
print ('等待TCP连接....')
print("*".center(60,'*'))
conn, addr = s.accept()
print ('已与 ', addr,'建立TCP连接')


t1=threading.Thread(target=sed,args=(conn,))
t1.start()
#接受信息
rcv(conn)
