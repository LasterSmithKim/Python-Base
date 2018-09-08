from dealFile import DealFile

d = DealFile()

path = r"/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/自动化办公与鼠标键盘模拟/2.读取PDF文件/LegalNotices.pdf"
def func(str):
    print(str + "！")

#  回调函数 func
d.readPDF(path)