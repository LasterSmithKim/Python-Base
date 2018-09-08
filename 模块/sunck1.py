#一个.py文件就是一个模块
#每一个模块都有一个 __name__属性，当其值等于 __main__ 的时候，表明该模块自身在执行
#当前文件如果是程序入口文件，则__name__属性的值为__main__

if __name__ == "__main__":
    print("**********")

else:

    def sayGood():
        print("sunck is a good man!")

    def sayNice():
        print("sunck ia a nice man!")

    def sayHandsome():
        print("sunck is a handsome man!")

