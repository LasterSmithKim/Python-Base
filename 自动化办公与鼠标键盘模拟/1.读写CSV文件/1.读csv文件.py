import csv

def readCsv(path):
    InfoList = []
    with open(path,"r") as f:
        allFileInfo = csv.reader(f)
        print(allFileInfo)
        for row in allFileInfo:
            InfoList.append(row)
    return InfoList

path = r"/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/自动化办公与鼠标键盘模拟/1.读写CSV文件/000001.csv"
info = readCsv(path)
print(info)



