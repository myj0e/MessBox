from threading import Thread, BoundedSemaphore
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
    v1.set("")
    v2.set("")
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

def ip():
    with open("scan_ip.txt", "r") as f:
        ftextlist = f.readlines()
        if ftextlist == []:
            messagebox.showerror('错误',  'scan_ip.txt未写入IP地址,请检查！')
    startport = int(e1.get())
    endport = int(e2.get()) + 1
    thread = int(e3.get())
    maxconnections = thread
    global semlock
    semlock = BoundedSemaphore(maxconnections)
    list=[]
    for dst in ftextlist:
        goBtn.config(state=DISABLED)
        quit.config(state=DISABLED)
        dst = dst.strip()
        if ipcheak(dst):
            while startport < endport:  # 指定扫描端口结束位置
                semlock.acquire()
                t=Thread(target=inset, args=(dst,startport))
                list.append(t)
                t.start()
                scr.update()
                startport = startport + 1
        else:
            messagebox.showerror('错误', 'scan_ip.txt格式错误,请检查！' + dst)
    goBtn.config(state=NORMAL)
    quit.config(state=NORMAL)

#检测soket是否连接成功或失败
def test_port(dst,port):
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_sock.settimeout(2)
    try:
        # 使用socket模块进行尝试连接
        indicator = cli_sock.connect_ex((dst, port))
        if indicator == 0:#如果连接成功，输入连接信息，并将结果写入文件中
            #print("[+]" + str(dst) + "  " + str(port) + " Open")
            b = (str(dst) + "  " + str(port) + " Open" + str("\n"))
            f1 = open('scan_record.txt', 'a+')
            f1.write(b)
            f1.close()
            semlock.release()
            return ("open")
        else:#如果连接失败，输入连接信息
            #print("[-]" + str(dst) + "  " +str(port) + " Close")
            b = (str(dst) + "  " + str(port) + " Close" )
            #print(b)
            semlock.release()
            return ("close")
        cli_sock.close()
    except:
        pass

#将连接记录写入UI文本
def inset(dst,port):
    dst = dst
    port = port
    vi = test_port(dst,port)
    b = (str(dst) + "  " + str(port)+  "  " + vi + str("\n"))
    scr.insert(END, b)
    scr.update()


def windowquit():
    window.destroy()




def main():
    global window
    window=Tk()
    window.title(string='快乐软工scanner')
    window.geometry('400x500')
    window.iconbitmap(root+"src/scanner.ico")
    global v1,v2,v3
    v1 = StringVar()
    v1.set(1)
    v2 = StringVar()
    v2.set(255)
    v3 = StringVar()
    v3.set(120)
    Label(window,text="请将IP地址输入到文件:scan_ip.txt",font = ('Arial',10),).place(x=20,y=20)
    Label(window,text="端口范围:",font = ('Arial',10),).place(x=20,y=55)
    Label(window,text="——",font = ('Arial',10),).place(x=130,y=53)
    global e1,e2,e3
    e1 = Entry(window,textvariable=v1,width=5)
    e1.place(x=90,y=55)
    e2 = Entry(window,textvariable=v2,width=5)
    e2.place(x=165,y=55)
    e3 = Entry(window,textvariable=v3,width=5)
    e3.place(x=90,y=90)
    Label(window,text="线程数:",font = ('Arial',10),).place(x=34,y=90)
    global goBtn
    goBtn=Button(window,text="开始扫描",width=10,height=1,command=ip)
    goBtn.place(x=230,y=20)
    global quit
    quit = Button(window,text="退出",width=10,height=1,command= windowquit)
    quit.place(x=315,y=20)
    Button(window,text="清除输入",width=10,height=1,command=clear).place(x=230,y=53)
    Button(window,text="清除输出",width=10,height=1,command=clear_scr).place(x=315,y=53)
    Button(window,text="清除input",width=10,height=1,command=clear_scan_ip).place(x=230,y=86)
    Button(window,text="清除record",width=10,height=1,command=clear_scan_record).place(x=315,y=86)
    global scr
    scr = scrolledtext.ScrolledText(window, width=50, height=28)
    scr.insert(END,'''***********************************\n*  欢迎使用快乐软工端口扫描工具!  *\n*---------------------------------*\n*注意:开始扫描前，请在scan_ip.txt *\n*填写标准ip地址,如127.0.0.1       *\n***********************************\n''')
    scr.place(x=22,y=120)
    window.mainloop()
