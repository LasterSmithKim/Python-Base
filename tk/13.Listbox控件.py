import tkinter

win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")
#支持多选
lb = tkinter.Listbox(win,selectmode = tkinter.MULTIPLE)
lb.pack()
for item in ["good","nice","handsone","vg","vs"]:
    lb.insert(tkinter.END,item)







win.mainloop()

