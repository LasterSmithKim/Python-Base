from multiprocessing import Process
from time import sleep
import os

def fun(str):
    print("启动子进程")
    sleep(3)
    print("子进程结束")

if __name__ == "__main__":
    print("父进程启动")
    p = Process(target=fun,args=("nice",))
    p.start()
    #父进程的结束 不能音响子进程，需求： 让父进程等待子进程结束 父进程再执行父进程
    p.join()
    print("父进程结束")

