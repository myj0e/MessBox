from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import time
import re
from threading import Thread, BoundedSemaphore
import socket
import os
import sys



root="C:/SEScanner/"

#------------------------------------------------------
def clear():
    scr.delete(1.0, END)
    scr.update()
    v1.set("")
    v2.set("")
    v3.set("")
def clear_test():
    f1 = open('scan_record.txt', 'w')
    f1.write("")
    f1.close()
def inset(dst,port):
    dst = dst
    port = port
    vi = test_port(dst,port)
    b = (str(dst) + "  " + str(port)+  "  " + vi + str("\n"))
    scr.insert(END, b)
    scr.update()


def test_port(dst, port):
    # os.system('title ' + str(port))
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_sock.settimeout(2)
    try:
        # 使用socket模块进行尝试连接
        indicator = cli_sock.connect_ex((dst, int(port)))
        if indicator == 0:  # 如果连接成功，输入连接信息，并将结果写入文件中
            b = (str(dst) + "  " + str(port) + " Open" + str("\n"))
            f1 = open('scan_record.txt', 'a+')
            f1.write(b)
            f1.close()
            semlock.release()
            return ("open")
        else:  # 如果连接失败，输入连接信息
            semlock.release()
            return ("close")
        cli_sock.close()
    except:
        pass
def ip():
    #检查IP输是否正确
    def ipcheak(inputip):
        if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                    inputip):
            #print("IP 正确")
            return True
        else:
            #print("IP 错误")
            return False

    def item():
        ip1 = e1.get()
        ip2 = e2.get()
        port = e3.get()
        if ipcheak(ip1) and ipcheak(ip2):
            #print("检查正常")
            ip_ite0 = list((re.search("([0-9]*).([0-9]*).([0-9]*).([0-9]*)", ip1).group(1,2,3)))
            ip_ite0 = "%s.%s.%s." %(ip_ite0[0],ip_ite0[1],ip_ite0[2])
            ip_ite1 = (re.search("([0-9]*).([0-9]*).([0-9]*).([0-9]*)", ip1).group(4))
            ip_ite2 = (re.search("([0-9]*).([0-9]*).([0-9]*).([0-9]*)", ip2).group(4))
            #print(ip_ite0,)
            return (ip_ite0,ip_ite1,ip_ite2,port)

        else:
            r = messagebox.showerror('错误', '输入错误,请检查！')
            goBtn.config(state=NORMAL)
            quit.config(state=NORMAL)
            return False


    def onGo():
        b = item()
        if b == False:
            pass
        else:
            statip=int(b[1])
            endip=int(b[2])+1
            port=b[3]
            maxconnections = 70
            global semlock
            semlock = BoundedSemaphore(maxconnections)
            listtt = []
            for i in range(statip,endip):
                ip_as = str(b[0])+str(i)
                semlock.acquire()
                t = Thread(target=inset, args=(ip_as, port))
                listtt.append(t)
                t.start()
                scr.update()
            goBtn.config(state=NORMAL)
            quit.config(state=NORMAL)
    goBtn.config(state=DISABLED)
    quit.config(state=DISABLED)
    onGo()

def windowquit():
    window.destroy()


#------------------------------------------------------
def main():
    global window
    window=Tk()
    window.title(string='快乐软工scanner')
    window.geometry('400x500')
    window.iconbitmap(root+"src/scanner.ico")
    global v1,v2,v3
    v1 = StringVar()
    v1.set('1.1.1.1')
    v2 = StringVar()
    v2.set('1.1.1.255')
    v3 = StringVar()
    v3.set(22)

    Label(window,text="开始IP:",font = ('Arial',10),).place(x=20,y=20)
    global e1
    e1 = Entry(window,textvariable=v1)
    e1.place(x=80,y=20)
    global e2
    e2 = Entry(window,textvariable=v2)
    e2.place(x=80,y=50)
    Label(window,text="结束IP:",font = ('Arial',10),).place(x=20,y=50)
    Label(window,text="端口:",font = ('Arial',10),).place(x=31,y=80)
    global e3
    e3 = Entry(window,textvariable=v3)
    e3.place(x=80,y=80)
    global goBtn 
    goBtn = Button(window,text="开始扫描",width=8,height=1,command=ip)
    goBtn.place(x=250,y=15)
    Button(window,text="清除输入-输出信息",width=18,height=1,command=clear).place(x=250,y=50)
    Button(window,text="清除桌面文档信息",width=18,height=0,command=clear_test).place(x=250,y=85)
    global quit
    quit = Button(window,text="退出",width=8,height=1,command= windowquit)
    quit.place(x=320,y=15)
    #滚动文本窗口
    global scr
    scr = scrolledtext.ScrolledText(window, width=50, height=28)
    scr.insert(END,"***********************************\n*  欢迎使用快乐软工端口扫描工具!  *\n***********************************\n")
    scr.place(x=22,y=120)
    # scr = scrolledtext(window, width=50, height=28,)
    # scr.place(x=22,y=120)
    window.mainloop()
