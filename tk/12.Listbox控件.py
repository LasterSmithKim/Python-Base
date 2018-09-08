import tkinter

win = tkinter.Tk()
win.title("标题")
#win.geometry("400x400+200+20")


#EXTENDED 可以使listbox支持shift和control
lb = tkinter.Listbox(win,selectmode=tkinter.EXTENDED)
lb.pack()
for item in ["good","nice","handsone","vg","vs","good2","nice2","handsone2","vg2","vs2","good3","nice3","handsone3","vg3","vs3"]:
    lb.insert(tkinter.END,item)


#按住shift + 点击鼠标 可以实现连续选择
#按住control + 点击鼠标 可以实现多选

#滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side = tkinter.RIGHT,fill = tkinter.Y)
lb.configure(yscrollcommand = sc.set)
lb.pack(side = tkinter.LEFT,fill=tkinter.BOTH)
#额外给属性赋值
sc['command'] = lb.yview









win.mainloop()