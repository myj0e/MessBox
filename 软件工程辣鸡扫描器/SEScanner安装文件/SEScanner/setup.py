import os
import sys
import shutil
import winreg
from win32com.shell import shell
from win32com.shell import shellcon
import pythoncom


def getDesktop():
    key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
    return winreg.QueryValueEx(key,"Desktop")[0]

def createShortcut(filename,lnkname):
    shortcut=pythoncom.CoCreateInstance(shell.CLSID_ShellLink,None,pythoncom.CLSCTX_INPROC_SERVER,shell.IID_IShellLink)
    shortcut.SetPath(filename)
    if os.path.splitext(lnkname)[-1]!='.lnk':
        lnkname+=".lnk"
        lnkname=os.path.join(getDesktop(),lnkname)
        shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(lnkname,0)
    

src="SEScanner/"
dst="C:/SEScanner/"
root="C:\SEScanner\\"

print("初始化环境.....")

try:
    if os.path.exists(dst):
        shutil.rmtree(dst)
    else:
        pass
except BaseException:
    print("错误！检查已初始化，或正在打开初始化根目录及文件")
    print("输入Enter结束")
    input()
else:
    shutil.copytree(src,dst)
    print("环境初始化结束！")

    createShortcut(root+"SEScanner\SEScanner.exe","SEScanner")
    print("桌面快捷方式已创建！")
    print("输入Enter结束")
    input()
