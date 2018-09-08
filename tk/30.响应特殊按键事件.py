import tkinter

win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")

#<Shift_R>
#<Shift_L>
#<F5>
#<Return>
#<BackSpace>


def func(event):
    print("event.chr = ",event.char)
    print("event.keycode = ",event.keycode)
label = tkinter.Label(win,text="sunck is a good man",bg="red")
#设置焦点 才能响应键盘事件 作用在焦点身上
label.focus_set()
label.pack()
label.bind("<BackSpace>",func)


win.mainloop()