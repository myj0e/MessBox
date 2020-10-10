# -*- coding: UTF-8 -*-
#文件名：client.py
#项目：TCP/IP直连对话系统


import socket
import threading
import time

def sed(s):
    while True:
        try:
            cmd = input().encode()
        except Exception as e:
            pass
        if(not cmd):
            continue
        s.send(cmd)
        print((time.strftime("%Y-%m-%d %X",time.localtime())+"你输入:\n "+cmd.decode()).center(60,' '))
            


def rcv(conn):
    while True:
        data = conn.recv(1024)
        print ((time.strftime("%Y-%m-%d %X",time.localtime())+"对方输入:\n "+data.decode()).center(60,' '))



#客户端socket
HOST = '127.0.0.1'
PORT = 8001

print("正在与%s 取得联系...."%(HOST,))
print("*".center(60,'*'))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("TCP连接成功！")


t1=threading.Thread(target=sed,args=(s,))
t1.start()
#接受信息
rcv(s)
