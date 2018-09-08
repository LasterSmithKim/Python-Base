import tkinter


def showInfo():
    print(entry.get())

win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")

entry = tkinter.Entry(win)
entry.pack()

button = tkinter.Button(win,text="按钮",command=showInfo)
button.pack()




win.mainloop()