import tkinter

win = tkinter.Tk()
win.title("标题")


def func(event):
    print("event.chr = ", event.char)
    print("event.keycode = ", event.keycode)
win.bind("a",func)

win.mainloop()



