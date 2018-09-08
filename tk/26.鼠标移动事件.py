import tkinter

win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")


#"<B1-Motion>"鼠标左键移动
#"<B2-Motion>",右键
#"<B3-Motion>",中键
def func(event):
    print(event.x,event.y)
label = tkinter.Label(win,text="sunck is a good man")
label.pack()
label.bind("<B1-Motion>",func)


win.mainloop()