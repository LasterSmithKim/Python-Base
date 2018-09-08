'''

两个线程同时工作，一个存钱一个取钱

可能导致数据异常

思路：加锁，


'''

import threading


#创建锁对象
lock = threading.Lock()
num = 0

def run(n):
    global num
    for i in range(1000000):
        #加锁
        #确保了这段代码只能由一个线程从头到尾完整执行
        #阻止了多线程的并发执行，包含锁的某段代码 实际上只能以单线程模式执行 所以效率大大地降低了
        #由于它可以存在多个锁，不同线程持有不同的锁，并且试图获取其他的锁，可能造成死锁，导致多个线程挂起，只能靠操作系统强制终止
        lock.acquire()
        try:#防止死锁 如果错误一定要释放
            num = num + n
            num = num - n
        finally:
        #修改完一定要解锁
            lock.release()

         '''
         with look：
            num = num + n
            num = num - n
            
         以上代码与上面相同
         可以自动上锁 解锁
         
         '''


if __name__ == "__main__":
    t1 = threading.Thread(target=run,args=(6,))
    t2 = threading.Thread(target=run,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("num = ",num)