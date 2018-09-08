class Person(object):
    def run(self):
        print("run")
        print(self.__money)
    def eat(self, food):
        print("eat" + food)

    def __init__(self, name, age, height, weight, money):
        self.name = name
        self.__age__ = age
        self._height = height
        self.weight = weight
        self.__money = money


    #通过内部的方法，去修改私有的属性
    #通过自定义的方法实现对私有属性的赋值与取值
    def setMoney(self,money):
        if money < 0 :
            money = 0
        self.__money = money
    def getMoney(self):
        return self.__money

per = Person("hangmeimei", 21, 160, 80, 10000)

# 如果要让内部的属性不被外部直接访问，在属性前加两个下划线（__）在Python中如果在属性前加两个下划线就变成了私有属性

#per.__money = 0

#print(per.__money)
per.run()#内部使用 __money

per.a = 100  #动态自定义了一个属性
print(per.a)

per.setMoney(10)
print(per.getMoney())


#不能直接访问per.__money是因为Ptython解释器把__money变成了_Person__money
#仍然可以用_Person__money去访问，但是强烈建议不要这么干，
#不同的解释器可能存在解释的变量名不一致


per._Person__money = 1
print(per.getMoney())

#注意：在Python中  __XXX__属于特殊变量，可以直接访问
print(per.__age__)

'''
在Python中 _XXX 变量，这样的实例变量外部是可以访问的，
但是按照约定的规则，当我们看到这样的变量时，
意思是"虽然我可以被访问"，但是请把我看成私有变量，在外部不要直接访问我

'''

print(per._height)


