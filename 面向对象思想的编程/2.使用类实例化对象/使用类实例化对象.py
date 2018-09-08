

class Person(object):
    #定义属性
    name   = ""
    age    = 0
    height = 0
    weight = 0
    #定义方法
    #注意：方法的参数必须以self当第一个参数
    #self代表类的实例（某个对象）
    def run(self):
        print(("run"))
    def eat(self,food):
        print("eat"+ food)
    def openDoor(self):
        print("我已经打开了冰箱门")
    def fillEle(self):
        print("我已经把大象装入了冰箱")
    def closeDoor(self):
        print("我已经关闭了冰箱门")


'''
实例化对象
格式： 对象名 = 类名（参数列表）
注意：没有参数，小括号也不能省略


'''

#实例化一个对象

per1 = Person()
print(per1)
print(type(per1))
print(id(per1))


per2 = Person()
print(per2)
print(type(per2))
print(id(per2))













