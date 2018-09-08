from person import Person
from gun import Gun
from bulletbox import BulletBox

'''
人
类别：Person
属性：gun
行为：fire

枪
类别：Gun
属性：bulletBox
行为：shoot


弹夹
类别：BulletBox
属性：bulletCount
行为：

'''
#弹夹
bulletBox = BulletBox(5)
#枪
gun = Gun(bulletBox)
#人
per = Person(gun)

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()

per.fillBullet(1)
per.fire()
per.fire()