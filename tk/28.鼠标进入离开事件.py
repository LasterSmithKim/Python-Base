import tkinter

win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")

#<Enter> 光标进入时触发
#<Leave>" 光标离开时触发
def func(event):
    print(event.x,event.y)
label = tkinter.Label(win,text="sunck is a good man",bg="red")
label.pack()
label.bind("<Leave>",func)



win.mainloop()