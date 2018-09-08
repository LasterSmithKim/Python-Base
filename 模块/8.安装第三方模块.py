


'''

Mac：无需安装
Liunx:无需安装
Windows：在安装python时 勾选安装

要安装三方模块，需要知道模块的名字
Pillow 非常强大的处理图像的工具库
$ pip install Pillow

$ pip install --upgrade pip

'''
#引入了第三方库
from PIL import Image
#from PIL import *

#打开图片
im = Image.open("111.gif")
#查看图片的信息
print(im.format,im.size,im.mode)
#设置图片的大小
im.thumbnail((50,23))
#保存成新图片
im.save("temp.gif","GIF")




