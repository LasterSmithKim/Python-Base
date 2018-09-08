import time

"""
UTC 世界协调时间，格林尼治天文时间，世界标准时间
    在中国是 UTC-8
DST 夏令时：是一种节约能源而人为规定时间制度，夏季调快1个小时


时间表示形式：
1.时间戳
以整型或浮点型表示时间的一个以秒为单位的时间间隔
从1970年1月1日开始算起

2.元组
一种python的数据结构表示，这个元组有9个整型内容
year
month
day
hours
miuntec
seconds
weekday
Julia day
DST  flag(1 or -1 or 0)

3.格式化字符串



"""
#返回当前时间的时间戳，浮点型形式，不需要参数
c = time.time()
print(c)

#将时间戳转为UTC时间元组
t = time.gmtime(c)
print(t)

#得到北京时间
b = time.localtime(c)
print(b)


#将本地时间转为时间戳
m = time.mktime(b)
print(m)

#将时间元组转为字符串
s = time.asctime(b)
print(s)

#将时间戳转为字符串
p = time.ctime(c)
print(p)


#将时间元组转为给定格式的字符串
q = time.strftime("%Y-%m-%d %X",b)
print(q)
print(type(q))

#将时间字符串转为时间元组
w = time.strptime(q,"%Y-%m-%d %X")
print(w)


#延迟一个时间，整型或浮点型
time.sleep(3)

#返回当前程序的cpu时间
#Unix形同始终返回全部的运行时间
#windows从第二次开始，都是以第一个调用此函数的开始时间戳作为基数

y1 = time.clock()
print(y1)

time.sleep(1)

y2 = time.clock()
print(y2)







