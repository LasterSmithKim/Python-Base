
class Person(object):
    def __init__(self,name,age):
        #直接对外暴露
        #self.age = age

        #限制访问
        self.__age = age
        self.__name = name

    '''
    def getAge(self):
        return self.__age

    def setAge(self,age):
        if age < 0:
            age = 0
        self.__age = age

    '''
    #方法名为受限制的变量去掉双下划线
    @property
    def age(self):
        return self.__age
    @age.setter #去掉下划线 setter
    def age(self,age):
        if age < 0 :
            age = 0
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter  # 去掉下划线 setter
    def name(self, name):
        self.__name = name


per = Person("sunck",18)

#属性直接对外暴露
#不安全，没有数据过滤
#per.age = -18
#print(per.age)

#使用限制访问，需要自己写set和get方法才能访问


'''
per.setAge(15)
print(per.getAge())

'''
per.name = "Tom"
per.age = -100 #相当于 调用setage
print(per.name,per.age) #相当于 调用getage



#property：可以让你对受限制的属性使用 点 语法













