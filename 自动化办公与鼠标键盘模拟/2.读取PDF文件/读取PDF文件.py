import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import  PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed



def readPDF(path,toPath):
    #以二进制形式打开PDF文件
    f = open(path,"rb")

    #创建管理器-pdf文档分析器
    parser = PDFParser(f)

    #创建一个pdf文档
    pdfFile = PDFDocument()

    #链接分析器与文档对象(分析器和文件双向链接）
    parser.set_document(pdfFile)
    pdfFile.set_parser(parser)

    #提供初始化密码
    pdfFile.initialize()

    #检测文档是否提供txt转换
    if not pdfFile.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        #解析数据
        #数据管理器
        manager = PDFResourceManager()
        #创建一个PDF设备的对象
        laparams = LAParams()
        device = PDFPageAggregator(manager,laparams=laparams)
        #创建解释器对象
        interpreter = PDFPageInterpreter(manager,device)


        #开始循环处理，每次处理一页
        for page in pdfFile.get_pages():
            interpreter.process_page(page)
            #创建涂层，循环处理涂层
            layout = device.get_result()
            for x in layout:
                #判断 x 是否是 LTTextBoxHorizontal类型的数据
                if(isinstance(x,LTTextBoxHorizontal)):
                    with open(toPath,"a") as f:
                        str = x.get_text()
                        #print(str)
                        f.write(str+"\n")







path = r"/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/自动化办公与鼠标键盘模拟/2.读取PDF文件/LegalNotices.pdf"
toPath = r"/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/自动化办公与鼠标键盘模拟/2.读取PDF文件/a.txt"
readPDF(path,toPath)

