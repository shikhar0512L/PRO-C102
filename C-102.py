import os
print("This program is to automate the process of cleaning your temporary files in computer.")
file_size = os.path.getsize('C:\Windows\Temp')
print(str(file_size) + "kb of data will be removed")
import os, subprocess
del_dir = r'c:\windows\temp'
pObj = subprocess.Popen('rmdir /S /Q %s' % del_dir, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
rTup = pObj.communicate()
rCod = pObj.returncode
if rCod == 0:
    print('Success: Cleaned Windows Temp Folder')
else:
    print('Fail: Unable to Clean Windows Temp Folder')
import winshell
winshell.recycle_bin().empty(confirm=False, show_progress=False, 
sound=False)
from random import randint
from time import sleep
sleep(randint(4,6))
input("Press any key to continue")