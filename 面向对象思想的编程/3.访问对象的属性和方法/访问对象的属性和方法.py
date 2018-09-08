
class Person(object):
    #定义属性
    name   = "stu"
    age    = 10
    height = 80
    weight = 90
    #定义方法
    #注意：方法的参数必须以self当第一个参数
    #self代表类的实例（某个对象）
    def run(self):
        print(("run"))
    def eat(self,food):
        print("eat "+ food)
    def openDoor(self):
        print("我已经打开了冰箱门")
    def fillEle(self):
        print("我已经把大象装入了冰箱")
    def closeDoor(self):
        print("我已经关闭了冰箱门")

per = Person()

'''
访问属性
格式：对象名.属性名
赋值：对象名.属性名 = 新值

'''


per.name = "tom"
per.age  = "18"
per.height = 160
per.weight = 60



print(per.name,per.age,per.weight,per.height)


'''
访问方法
格式：对象名.方法名（参数列表）

'''
per.openDoor()
per.fillEle()
per.closeDoor()


per.eat("apple")

#问题：目前来看Person创建的所有对象属性都是一样的
















