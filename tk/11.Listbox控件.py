import tkinter

win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")

#绑定变量
lbv = tkinter.StringVar()

#与BORWSE相似，当它不支持鼠标移动选中
lb = tkinter.Listbox(win,selectmode=tkinter.SINGLE,listvariable = lbv)
lb.pack()
for item in ["good","nice","handsone","vg","vs"]:
    #按顺序添加
    lb.insert(tkinter.END,item)

#打印当前列表中的选项
print(lbv.get())
#设置选项
#lbv.set(("1","2","3"))

def myPrint(event):
    print(lb.get(lb.curselection()))

#绑定事件
lb.bind("<Double-Button-1>",myPrint)


win.mainloop()



