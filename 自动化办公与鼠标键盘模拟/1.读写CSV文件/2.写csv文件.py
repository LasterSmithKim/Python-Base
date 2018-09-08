import csv



def writeCsv(path,data):
    with open(path,"w") as f:
        writer = csv.writer(f)
        for rowData in data:
            writer.writerow(rowData)


path = r"/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/自动化办公与鼠标键盘模拟/1.读写CSV文件/000002.csv"
writeCsv(path,[[1,2,3],[4,5,6],[7,8,9]])