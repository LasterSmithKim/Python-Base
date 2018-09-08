'''
重写：将函数重新定义写一遍

__str__()在调用print打印对象时自动调用，是个用户用的，它是一个描述对象的方法。


__repr__()是个机器用的，在Python解释器里面直接敲对象名在回车后调用的方法
注意：在没有 __str__时，且有repr，  str等于repr




'''


class Person(object):
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age  = age
        self.height = height
        self.weight = weight
    def __str__(self):
        return "%s-%d-%d-%d" %(self.name,self.age,self.weight,self.height)

per = Person("hangmeimei",21,160,80)

#print(per.name,per.age,per.weight,per.height)
print(per)

#优点：当一个对象的属性值很多，并且都需要打印，重写了__str__方法后，简化了代码

#作业：人开枪射击子弹

