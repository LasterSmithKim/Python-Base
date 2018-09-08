import tkinter

win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")



#<Key> 响应所有的按键

def func(event):
    print("event.chr = ",event.char)
    print("event.keycode = ",event.keycode)
label = tkinter.Label(win,text="sunck is a good man",bg="red")
#设置焦点 才能响应键盘事件 作用在焦点身上
label.focus_set()
label.pack()
label.bind("<Key>",func)
'''
def func(event):
    print("event.chr = ",event.char)
    print("event.keycode = ", event.keycode)
win.bind("<Key>",func)
'''



win.mainloop()