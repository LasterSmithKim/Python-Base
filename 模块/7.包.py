import sys
import a.sunck
import a.kaige
import b.sunck
'''
思考：如果不同的人编写的模块名相同怎么办？

解决：为了解决模块名的冲突，引入了按目录来组织模块的方法，称为 包

特点：引入了包以后，只要顶层的包不予其他人发生冲突，那么模块都不会与别人的发生冲突

注意：目录只有包含一个叫做 __init__.py 的文件才被认作是一个包，主要是为了避免一些滥竽充数的单词，基本上
目前这个文件中什么都不用写def sayGood():
    print("sunck is a good man!-a")

'''

for i in sys.path:
    print(i)

a.sunck.sayGood()
a.kaige.sayKaige()