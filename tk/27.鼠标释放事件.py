import tkinter

win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")

#<ButtonRelease-1>" 释放鼠标左键
#<ButtonRelease-2>"
#<ButtonRelease-3>"

def func(event):
    print(event.x,event.y)
label = tkinter.Label(win,text="sunck is a good man",bg="red")
label.pack()
label.bind("<ButtonRelease-1>",func)



win.mainloop()