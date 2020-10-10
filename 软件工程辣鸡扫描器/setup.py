import os


os.system('xcopy /y qrcode C:\\qrcode\ /s/e')
os.system('setx "Path" "%path_%;C:\qrcode\ " /m')
