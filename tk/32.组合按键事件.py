import tkinter

win = tkinter.Tk()
win.title("标题")

#<Shift-Up>
#<Control-p>
def func(event):
    print("event.chr = ", event.char)
    print("event.keycode = ", event.keycode)
win.bind("<Control-p>",func)

win.mainloop()

