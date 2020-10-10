import shutil
import package.MipOport as miop
import package.OipMport as oimp
import package.OipOport as oiop
import tkinter as tk
from PIL import Image


root="C:/SEScanner/"
def mo():
    window.destroy()
    miop.main()
    main()
    
def om():
    window.destroy()
    oimp.main()
    main()
    
def oo():
    
    window.destroy()
    oiop.main()
    main()

def init_size(x):
    img=Image.open(x)
    new_x=250
    new_y=170
    out = img.resize((new_x, new_y), Image.ANTIALIAS)
    out.save(x)

def main():
    global window,bt1,bt2,bt3,im,cn
    window=tk.Tk()
    window.title('快乐软工scanner')
    window.geometry('550x200')
    window.configure(bg='#1F3970')
    bt1=tk.Button(window,text='多地址单端口扫描',width=23,height=2,font=('Arial',10),fg='#AFEEEE',bg='#484D8B',command=mo)
    bt1.place(x=15,y=20)
    bt2=tk.Button(window,text='单地址多端口扫描',width=23,height=2,font=('Arial',10),fg='#AFEEEE',bg='#484D8B',command=om)
    bt2.place(x=15,y=80)
    bt3=tk.Button(window,text='单地址单端口扫描',width=23,height=2,font=('Arial',10),fg='#AFEEEE',bg='#484D8B',command=oo)
    bt3.place(x=15,y=140)
    init_size(root+'src/background.png')
    im=tk.PhotoImage(file=root+'src/background.png')
    cn=tk.Canvas(window,height=170,width=250)
    #cn.grid()
    cn.create_image(2,2,image=im,anchor=tk.NW)
    cn.place(x=250,y=10)

    window.mainloop()
