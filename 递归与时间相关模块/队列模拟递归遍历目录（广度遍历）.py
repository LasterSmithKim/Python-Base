import os
import collections



def getAllDirQU(path):
    queue = collections.deque()
    #进队
    queue.append(path)

    while len(queue) != 0:
        #出队数据
        dirPath = queue.popleft()

        #找出所有的文件
        firlsList = os.listdir(dirPath)

        for firleName in firlsList:
            #合成绝对路径
            fileAbsPath = os.path.join(dirPath,firleName)
            #判断是否是目录，是目录进队，不是就打印
            if os.path.isdir(fileAbsPath):
                print("目录：" + firleName)
                queue.append(fileAbsPath)
            else:
                print("普通文件：" + firleName)


getAllDirQU(r"/Users/jinpeihua/dir")