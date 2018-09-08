import tkinter

win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")
def func(event):
    print(event.x,event.y)
button1 = tkinter.Button(win,text="leftmouse button")

#"<Button-1>"鼠标左键 <Button-2>鼠标右键<Button-3>鼠标中键
#<Double-Button-1>"鼠标左键双击
#<Triple-Button-1> 鼠标左键三击

#bind 给控件绑定事件
button1.bind("<Triple-Button-1>",func)
button1.pack()



win.mainloop()