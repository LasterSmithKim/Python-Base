import tkinter

win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")


'''
供用户通过拖拽指示器改变变量的值，可以水平也可以竖直

tkinter.HORIZONTAL 水平方向
tkinter.VERTICAL   竖直方向
length  水平时表示宽度，竖直时表示宽度
tickinterval  选择值将会为该值得倍数
'''

scale1 = tkinter.Scale(win,from_=0,to=100,orient=tkinter.VERTICAL,tickinterval=10,length=200)
scale1.pack()

#设置值
scale1.set(20)


#取值
def showNum():
    print(scale1.get())

tkinter.Button(win,text="按钮",command=showNum).pack()






win.mainloop()



