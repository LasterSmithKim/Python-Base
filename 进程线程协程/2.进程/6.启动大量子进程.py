from multiprocessing import Process
import os,time,random
from multiprocessing import Pool

def run(name):
    print("子进程%d启动-%s"%(name,os.getpid()))
    start = time.time()
    time.sleep(random.choice([1,2,3,4,5]))
    end = time.time()
    print("子进程%d结束-%s--耗时%.2f"%(name,os.getpid(),end-start))


if __name__ == "__main__":
    print("父进程启动")

    #创建多个进程
    #创建进程池
    #表示同时执行的进程数量，默认是CPU核心数
    pp = Pool(12)
    for i in range(4):
        #创建进程，放入进程池统一管理
        pp.apply_async(run,args=(i,))

    #在调用join之前必须调用close，调用close之后就不能再继续添加新的进程
    pp.close()
    #进程池对象调用join，会等待进程池中所有的子进程结束完毕后 在去执行父进程
    pp.join()

    print("父进程结束")