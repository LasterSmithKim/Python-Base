'''
原型：filter(fn,lsd)
参数1：函数
参数2：序列

功能：用于过滤序列
白话文：把传入的函数依次作用于序列每个元素，根据返回的是True还是False决定是否保留该元素




'''


list1 = [1,2,3,4,5,6,7,8,9]
#筛选条件，偶数保留
def func(num):
    if num%2 ==0:
        return True
    return False
l = filter(func,list1)
#
print(list(l))


