import tkinter
import os

from treeWindows import TreeWindows
from infoWindows import InfoWindows

win = tkinter.Tk()
win.title("sunck")
win.geometry("800x400+200+50")

path = "/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一"

infoWin = InfoWindows(win)
treeWin = TreeWindows(win,path,infoWin)





win.mainloop()