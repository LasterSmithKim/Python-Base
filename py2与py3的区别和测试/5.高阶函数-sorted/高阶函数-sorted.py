#排序：冒泡、选择、快速、插入、计数器

#普通排序

list1 = [1,3,2,9,4,5,7,10,8,6]
list2 = sorted(list1)#默认升序
print(list2)

#绝对值大小排序
list3 = [1,3,2,-9,4,5,-7,10,8,6]
#key 接收函数来实现自定义排序规则
list4 = sorted(list3,key=abs)
#list5 = sorted(map(abs,list3))
print(list4)
#print(list5)

#降序
list5 = ["b","d","c","a",]
list6 = sorted(list5,reverse=True)
print(list6)

#字符串长短排,函数可以自编写
def myLen(str):
    return len(str)
list7 = ["b22222","d444","c3","a111",]
list8 = sorted(list7,key=myLen,reverse=False)
print(list8)