


'''
windows OS 代码


import win32api
import win32con
import wingui


def setWallPaper(path)
    #打开注册表
    reg_key = win32api.RegOpenKeyEx(
win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)

    win32api.RegSetValueEx(reg_key,"WallpaperStyle",0,win32con.REG_SZ,"6")
    #
    win32api.RegSetValueEx(reg_key,"WallPaper")
    win32api.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path,win32con.SPIF_SENDWININICHANGE)


setWallPaper(path)

'''




