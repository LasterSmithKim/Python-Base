import os,time
from multiprocessing import Pool


#实现文件的拷贝
def copyFile(rPath,wPath):
    fr = open(rPath,"rb")
    fw = open(wPath,"wb")
    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()


path = r"/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/进程线程协程/2.进程/file"
toPath = r"/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/进程线程协程/2.进程/tofile"




if __name__ == "__main__":
    # 读取path下的所有文件
    filesList = os.listdir(path)
    start = time.time()

    pp = Pool(2)
    for fileName in filesList:
        pp.apply_async(copyFile,args=(os.path.join(path,fileName),os.path.join(toPath,fileName)))


    pp.close()
    pp.join()
    end = time.time()

    print("总耗时：%0.2f"%(end-start))
