'''
self 代表类的实例，而非类


哪个对象调用发放，那么该方法中的self就代表那个对象


self.__class__ 代表类名

 print("Hello!My name is %s,I am %d years old ."(self.name,self.age))

'''

class Person(object):
    def run(self):
        print(("run"))
        print(self.__class__)
        #使用类名 再次创建了 一个实例对象 p
        p = self.__class__("tt",30,10,30)
        print(p)
    def eat(self,food):
        print("eat"+ food)
    def say(self):
        print("Hello!My name is %s,I am %d years old ."%(self.name, self.age))

    #self不是关键字，换成其他的标识符也是可以的，但是通常使用self
    def play(a):
        print("play " + a.name)
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age  = age
        self.height = height
        self.weight = weight




per1 = Person("Tom",20,160,80)
per1.say()

per2 = Person("hangmeimei",21,160,80)
per2.say()

per2.play()
per2.run()


