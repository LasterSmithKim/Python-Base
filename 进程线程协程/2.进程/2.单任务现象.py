from  time import sleep



def fun():
    while True:
        print("sunck is a nice man")
        sleep(1.2)

if __name__ == "__main__":
    while True:
        print("sunck is a good man")
        sleep(1)
    #不会执行到fun方法，只有上面的while循环结束才可以执行
    fun()