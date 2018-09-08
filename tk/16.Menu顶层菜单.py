

import tkinter

win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")


#菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)

def func():
    print()
    print("****")

#创建一个菜单选项
menu1 = tkinter.Menu(menubar,tearoff=False)
#给菜单选项添加内容
for item in ["Python","C","C++","OC","Swift","C#","shell","Java","JS","PHP","汇编","NodeJS","退出"]:
        if item == "退出":
            #添加分割线
            menu1.add_separator()
            menu1.add_command(label=item,command=win.quit)
        else:
            menu1.add_command(label=item,command=func)
#向菜单条上添加菜单

menubar.add_cascade(label="语言",menu=menu1)


menu2 = tkinter.Menu(menubar,tearoff = False)
menu2.add_command(label="red")
menu2.add_command(label="blue")
menubar.add_cascade(label="颜色",menu=menu2)

win.mainloop()
