import os
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    try:
        os.system('cmd /c "taskkill /F /IM "iCUE.exe" /T"')
        os.system('cmd /c "taskkill /F /IM "LightingService.exe" /T"')
        os.system ('cmd /c "cd /d d: & cd D:\SteamLibrary\steamapps\common\Apex Legends & start r5apex.exe"')
    except:
        print('could not execute command')
else:
    print('program failed')
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

