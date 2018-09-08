import os

def getAllDir(path,sp = ""):
    #得到当前目录下所有的文件
    filesList = os.listdir(path)

    sp += "   "
    for fileName in filesList:
        #判断是否是路径(绝对路径）
        fileAbsPath = os.path.join(path,fileName)
        if os.path.isdir(fileAbsPath):
            print(sp + "目录：",fileName)
            getAllDir(fileAbsPath,sp)
        else:
            print(sp + "普通文件：",fileName)




getAllDir(r"/Users/jinpeihua/dir")