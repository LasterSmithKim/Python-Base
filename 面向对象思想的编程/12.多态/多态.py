from cat import Cat
from mouse import Mouse
from person import Person
'''
多态：一种事物的多种形态
最终的目标：人可以喂任何一种动物
'''

tom = Cat("Tom")
jerry = Mouse("Jerry")

tom.eat()
jerry.eat()

#思考：再添加100种动物，都有 吃方法 name属性
#采用继承，定义了一个有name属性和eat方法的Animal类，让所有的动物类都继承自Animal


#定义一个人类，可以喂猫和老鼠吃东西
per = Person("P")
#per.feedCat(tom)
#per.feedMouse(jerry)

#思考：人要喂100种动物，难道要写100个feed方法么
per.feedAnimal(tom)
per.eat()
#自己喂自己吃
per.feedAnimal(per)