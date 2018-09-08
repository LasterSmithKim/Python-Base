

class Person(object):
    #定义属性
    # name   = ""
    # age    = 0
    # height = 0
    # weight = 0
    #定义方法
    #注意：方法的参数必须以self当第一个参数
    #self代表类的实例（某个对象）
    def run(self):
        print(("run"))
    def eat(self,food):
        print("eat"+ food)
    def __init__(self,name,age,height,weight):
        print("这里是init")
        print(name,age,height,weight)
        #定义属性
        self.name = name
        self.age  = age
        self.height = height
        self.weight = weight



'''
构造函数：__init__()  在使用类创建对象的时候自动调用，
注意：如果不显示的写出构造函数，默认会自动添加一个空的构造函数


'''

per1 = Person("hanmeimei",20,170,55)

print(per1.name,per1.age,per1.height,per1.weight)

per2 = Person("lilei",21,180,65)

print(per2.name,per2.age,per2.height,per2.weight)
















