import tkinter

win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")

def updata():
    print(r.get())

#注意：一组单选框绑定同一个变量
#绑定变量
r = tkinter.IntVar() #绑定不同的变量类型 StrtingVar-value为 字符串类型
radio1 = tkinter.Radiobutton(win,text="one",value = 1,variable = r,command = updata)
radio1.pack()
radio2 = tkinter.Radiobutton(win,text="two",value = 2,variable = r,command = updata)
radio2.pack()






win.mainloop()