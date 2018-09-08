import tkinter


def func():
    print("sunck is a good man .")
win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")

'''
输入控件
用于显示简单的文本内容

'''
e = tkinter.Variable()
# 指定变量 testvariable = e
# show = "*" 密文显示
entry = tkinter.Entry(win,textvariable=e)
entry.pack()

#e 就代表输入框这个对象
#设置值
e.set("sunck is a good man.")
#取值
print(e.get())
print(entry.get())




win.mainloop()