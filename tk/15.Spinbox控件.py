
import tkinter

win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")

'''
数值控制控件
increment步长 默认为1

'''
def updata():
    print(v.get())
#绑定变量
v = tkinter.StringVar()


#使用values 时不要使用 from to increment 三个属性同时使用
sp = tkinter.Spinbox(win,from_=0,to=100,increment=1)
sp.pack()
sp2 = tkinter.Spinbox(win,values=(0,2,4,6,8))
sp2.pack()
#设置值   command只要值改变就会执行对应的方法
sp3 = tkinter.Spinbox(win,from_=0,to=100,increment=1,textvariable=v,command=updata)
sp3.pack()
#赋值
v.set(20)
#取值
print(v.get())



win.mainloop()

