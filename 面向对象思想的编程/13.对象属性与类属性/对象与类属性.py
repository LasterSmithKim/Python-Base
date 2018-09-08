

class Person(object):
    #这里的属性实际上属于类属性（用类名来调用）
    name = "person"

    def __init__(self,name):
        #对象属性
        self.name = name
        pass


print(Person.name)

#对象属性的优先级高于类属性
per = Person("Tom")
#动态的给对象添加对象属性
per.age = 10 #只正对当前对象生效，对于类创建其他对象没有作用
print(per.name)

per2 = Person("lILEI")
#print(per2.age) 没有AGE属性

#删除对象中的某个属性，再调用会使用同名的类属性
del per.name
print(per.name)

#注意：以后千万不要将对象属性与类属性重名，因为对象属性会屏蔽掉类属性，
#但是，当删除对象属性后，在使用又能使用类属性了。

