# -*- coding: utf-8 -*-
import os
import collections

def cooking(path):


    #打开文件
    resPath = r"/Users/jinpeihua/PycharmProjects/maillist/res"

    with open(path,"r") as f:
        while True:
            #fsafdsaf@163.com----fdsafdsa
            lineInfo = f.readline()
            if len(lineInfo) < 5:  #控制到达最后一行以后退出循环
                break
            # 处理每一行数据

            mailStr = lineInfo.split("----")[0]
            fileType = mailStr.split("@")[1].split(".")[0]
            dirStr  = os.path.join(resPath,fileType)
            #是否创建目录，存在不创建，不存在创建
            if not os.path.exists(dirStr):
                os.mkdir(dirStr)

            #追加数据
            filePath = os.path.join(dirStr,fileType + ".txt")
            with open(filePath,"a") as fw:
                fw.write(mailStr + "\n")







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
            if firleName == ".DS_Store":
                pass
            else:
                #合成绝对路径
                fileAbsPath = os.path.join(dirPath,firleName)
                    #判断是否是目录，是目录进队，不是就处理cooking
                if os.path.isdir(fileAbsPath):
                   queue.append(fileAbsPath)
                else:
                    #处理普通文件
                    cooking(fileAbsPath)

getAllDirQU(r"/Users/jinpeihua/PycharmProjects/maillist/list")