
#使用 from ....... import 语句
#作用： 从模块中导入一个指定的部分到当前命名空间
#格式： from module import name1[,name2[,name3[,namen......]]]
from sunck import sayGood,sayNice

'''
程序内部的函数可以将导入的模块中的同名函数覆盖

'''


sayGood()
sayNice()