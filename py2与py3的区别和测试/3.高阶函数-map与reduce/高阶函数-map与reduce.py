from functools import reduce

#Google的文章

#Pythone内置了 map 和 reduce 函数（）


#map（）
#原型 map（fn，lsd）
#参数1 是函数
#参数2 是序列

#功能：将传入的函数依次作用在序列中的每一个元素，并把结果作为新的Iterator返回

#将单个字符转成对应字面的整数
def chr2int(chr):
    return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[chr]

list1 = ["2","1","4","2","4","5","6",]

res = map(chr2int,list1)
print(res)
print(list(res))

#将list1里面的元素 都进入 cha2int 计算一次
#res序列对象 是一个惰性列表 需要使用list（）显示



#将整数元素的序列，转为字符串类型
#【1，2，3，4，5】->【"1"，"2"，"3"，"4"，"5"】
l = map(str,[1,2,3,4,5])
print(list(l))

#reduce(fn,lsd)
#参数1 ：函数
#参数2：列表
#功能：一个函数作用在序列上，这个函数必须接受两个参数，reduce把结果继续和序列下一个元素累计计算


#reduce(f,[a.b.c.d])
#f(f(f(a,b),c),d)

#求一个序列的 和
list2 = [1,2,3,4,5,6,7,8,9]
def mysun(x,y):
    return x+y
r = reduce(mysun,list2)
print(r)

#需求：将字符串转成对应字面量的数字
def str22int(str):
    def fc(x,y):
        return x * 10 + y
    def fs(chr):
        return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[chr]
    return reduce(fc,map(fs,str))

print(str22int("1232321321"))


print(int("123"))








