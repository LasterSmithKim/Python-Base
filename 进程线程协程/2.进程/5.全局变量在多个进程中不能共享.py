from multiprocessing import Process
from time import sleep

num = 100

def func():
    print("子进程开始")
    global num # num = 100 定义了新的 num变量
    num += 1

    print("子进程结束--%d"%num)


if __name__ == "__main__":
    print("父进程开始")

    p = Process(target=func)
    p.start()
    p.join()

    p1 = Process(target=func)
    p1.start()
    p1.join()


    #在子进程中修改全局变量，在父进程中的全局变量没有影响
    #在创建子进程时，对全局变量做了一个备份，父进程与子进程中的num是完全不一样的
    print("父进程结束--%d"%num)