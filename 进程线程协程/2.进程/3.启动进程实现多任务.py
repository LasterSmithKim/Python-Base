'''

multiprocession 库
跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象

'''

from multiprocessing import Process
from time import sleep
import os

#子进程需要的执行的代码
def fun(str):
    while True:
        #获取当前进程号
        print("sunck is %s man-%s-%s"%(str,os.getpid(),os.getppid()))
        sleep(1.2)

if __name__ == "__main__":
    print("主（父）进程启动-%s"%(os.getpid()))
    #创建子进程
    #target 说明进程执行的任务
    p = Process(target=fun,args=("nice",))
    #启动进程
    p.start()


    while True:
        print("sunck is a good man-%s"%(os.getpid()))
        sleep(1)

