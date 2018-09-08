import tkinter

win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")

'''
框架控件：在屏幕上显示一个矩形区域，多作为容器控件

'''
#创建Frame
frm =tkinter.Frame(win)
frm.pack()

#在frm中创建 frm_l 和 frm_r
#再在 frm_l 和 frm_r 中分别创建了2个标签

#left
frm_l = tkinter.Frame(frm)
tkinter.Label(frm_l,text="左上",bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frm_l,text="左下",bg="blue").pack(side=tkinter.TOP)
frm_l.pack(side=tkinter.LEFT)
#right
frm_r = tkinter.Frame(frm)
tkinter.Label(frm_r,text="右上",bg="red").pack(side=tkinter.TOP)
tkinter.Label(frm_r,text="右下",bg="yellow").pack(side=tkinter.TOP)
frm_r.pack(side=tkinter.RIGHT)


win.mainloop()