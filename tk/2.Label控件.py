import tkinter

win = tkinter.Tk()
win.title("标题")
win.geometry("400x400+200+20")

'''
Label:标签控件
可以显示文本
'''
#win：父窗体
#text:显示文本的内容
#bg:背景色
#fg：字体颜色
#font:字体
#width:宽度
#wraplength指定text文本中多宽进行换行
#justify 设置换行后的对齐方式
#anchor 位置 n北 e东 s南 w西 center居中 ne es sw nw
label = tkinter.Label(win,
                      text = "sunck",
                      bg = "blue",
                      fg = "red",
                      font = ("黑体",20),
                      width = 10,
                      height = 4,
                      wraplength = 100,
                      justify = "left",
                      anchor = "center")

#挂载到试图
label.pack()

win.mainloop()