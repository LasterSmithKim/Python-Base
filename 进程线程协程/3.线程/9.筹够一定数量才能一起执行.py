import threading,time


bar = threading.Barrier(3)
def run():
    print("%s--start" %(threading.current_thread().name))
    time.sleep(1)
    bar.wait()
    print("%s--end" % (threading.current_thread().name))
    time.sleep(1)




if __name__ == "__main__":
    for i in range(5):
        threading.Thread(target=run).start()

'''
结果：筹够3个进程一起执行，否则等待

Thread-1--start
Thread-2--start
Thread-3--start
Thread-4--start
Thread-5--start
Thread-3--end
Thread-1--end
Thread-2--end


'''