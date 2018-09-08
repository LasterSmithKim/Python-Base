import tkinter


def func():
    print("sunck is a good man .")
win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")

'''

'''
#创建按钮
#text 按钮的文字
#command 按钮的动作
button1 = tkinter.Button(win,
                        text = "按钮",
                        command = func,
                        width = 3,
                        height =5)
button1.pack()

button2 = tkinter.Button(win,
                        text = "按钮",
                        command = lambda :print("sunck "))
button2.pack()

button3 = tkinter.Button(win,
                        text = "关闭",
                        command = win.quit)
button3.pack()

win.mainloop()