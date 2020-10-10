#导入python相关模块包
from threading import Thread, BoundedSemaphore
import socket
import re
import socket
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

root="C:/SEScanner/"

# 检查IP输是否正确
def ipcheak(inputip):
    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                inputip):
        # print("IP 正确")
        return True
    else:
        # print("IP 错误")
        return False


#清除e1/e2/e3输入框内容
def clear():
    v3.set("")
#清除scr输出文本内容
def clear_scr():
    scr.delete(1.0, END)
    scr.update()
#清除输出记录文件
def clear_scan_record():
    f1 = open('scan_record.txt', 'w')
    f1.write("")
    f1.close()
#清除源文件
def clear_scan_ip():
    f1 = open('scan_ip.txt', 'w')
    f1.write("")
    f1.close()
#将连接记录写入UI文本
def inset(dst,port):
    dst = dst
    port = port
    vi = test_port(dst,port)
    b = (str(dst) + "  " + str(port)+  "  " + str(vi) + str("\n"))
    scr.insert(END, b)
    scr.update()


#测试ip和端口是否开放
def test_port(dst,port):
    #os.system('title '+str(port))
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_sock.settimeout(2)
    try:
        #使用socket模块进行尝试连接
        indicator = cli_sock.connect_ex((dst,int(port)))
        if indicator == 0:   #如果连接成功，输入连接信息，并将结果写入文件中
            print("[+]" + str(dst) + "  " + str(port) + " Open")
            b = (str(dst) + "  " + str(port) + " Open" + str("\n"))
            f1 = open('scan_record.txt', 'a+')
            f1.write(b)
            f1.close()
            return ("open")
        else:
            return ("close")
        cli_sock.close()
    except:
        pass
    semlock.release()
def ip():
    #读取文件内容
    with open("scan_ip.txt", "r") as f:
        ftextlist = f.readlines()
    #循环遍历IP
    for dst in ftextlist:
        dst = dst.strip()
        a = dst.split(":")
        try:
            ip = a[0]
            port = a[1]
        except Exception as e:
            messagebox.showerror('错误',  'scan_ip.txt格式错误,请检查！' + dst)
        thread = int(e3.get())
        maxconnections = thread
        global semlock
        semlock = BoundedSemaphore(maxconnections)
        list = []
        if ipcheak(ip):
            semlock.acquire()
            t = Thread(target=inset, args=(ip, port))
            list.append(t)
            t.start()
        else:
            messagebox.showerror('错误',  'scan_ip.txt格式错误,请检查！' + dst)


def windowquit():
    window.destroy()

def main():
    global window
    window=Tk()
    window.title(string='快乐软工scanner')
    window.geometry('400x500')
    window.iconbitmap(root+"src/scanner.ico")
    global v3
    v3 = StringVar()
    v3.set(120)
    Label(window,text="输入IP地址到文件:scan_ip.txt",font = ('Arial',10),).place(x=20,y=30)
    global e3
    e3 = Entry(window,textvariable=v3,width=5)
    e3.place(x=80,y=70)
    Label(window,text="线程数:",font = ('Arial',10),).place(x=20,y=70)
    goBtn=Button(window,text="开始扫描",width=10,height=1,command=ip)
    goBtn.place(x=230,y=20)
    quit = Button(window,text="退出",width=10,height=1,command= windowquit)
    quit.place(x=315,y=20)
    Button(window,text="清除输入",width=10,height=1,command=clear).place(x=230,y=53)
    Button(window,text="清除输出",width=10,height=1,command=clear_scr).place(x=315,y=53)
    Button(window,text="清除输入",width=10,height=1,command=clear_scan_ip).place(x=230,y=86)
    Button(window,text="清除record",width=10,height=1,command=clear_scan_record).place(x=315,y=86)
    global scr
    scr = scrolledtext.ScrolledText(window, width=50, height=28)
    scr.insert(END,'''**************************************\n*    欢迎使用快乐软工端口扫描工具!   *\n*------------------------------------*\n*注意:开始扫描前，请在scan_ip.txt 填 *\n*写标准IP:端口格式,如127.0.0.1:135   *\n**************************************\n''')
    scr.place(x=22,y=120)
    window.mainloop()
