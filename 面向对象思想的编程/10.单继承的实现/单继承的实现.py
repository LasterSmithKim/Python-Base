from person import Person
from student import Student
from worker import Worker



stu = Student("Tom",18,1234,110)
print(stu.name,stu.age)
stu.run()

print(stu.stuId)
stu.stuId = 11
print(stu.stuId)
#print(stu.__money)私有属性
print(stu.getMoney()) #通过继承过来的共有方法 访问私有属性
#stu.stuFunc()


worker = Worker("hanmeimei",18,200)
print(worker.name,worker.age)
worker.eat("food")

