import tkinter
from tkinter import ttk
win = tkinter.Tk()
win.title("标题")
win.geometry("600x400+200+20")

#表格
tree = ttk.Treeview(win)
tree.pack( )
#定义列
tree["columns"] = ("姓名","年龄","身高","体重")
#设置列，列还没有显示
tree.column("姓名",width=100)
tree.column("年龄",width=100)
tree.column("身高",width=100)
tree.column("体重",width=100)


#设置显示表头
tree.heading("姓名",text="姓名-name")
tree.heading("年龄",text="年龄-age")
tree.heading("身高",text="身高-height")
tree.heading("体重",text="体重-weight")

#添加数据
tree.insert("",0,text="line1",values=("陆彦旭","28","165","80"))
tree.insert("",1,text="line2",values=("范育冰","28","165","80"))

win.mainloop()