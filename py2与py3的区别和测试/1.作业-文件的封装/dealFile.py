import csv
import sys
import importlib
importlib.reload(sys)
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import  PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed




class DealFile(object):
    #读csv
    def readCsv(self,path):
        InfoList = []
        with open(path, "r") as f:
            allFileInfo = csv.reader(f)
            print(allFileInfo)
            for row in allFileInfo:
                InfoList.append(row)
        return InfoList


    #写csv
    #数据格式：[[1,2,3],[4,5,6],[7,8,9]]
    def writeCsv(self,path, data):
        with open(path, "w") as f:
            writer = csv.writer(f)
            for rowData in data:
                writer.writerow(rowData)


    #读取PDF
    def readPDF(self,path, callback=None,toPath=""):
        f = open(path, "rb")
        parser = PDFParser(f)
        pdfFile = PDFDocument()
        parser.set_document(pdfFile)
        pdfFile.set_parser(parser)
        pdfFile.initialize()
        if not pdfFile.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            manager = PDFResourceManager()
            laparams = LAParams()
            device = PDFPageAggregator(manager, laparams=laparams)
            interpreter = PDFPageInterpreter(manager, device)
            for page in pdfFile.get_pages():
                interpreter.process_page(page)
                layout = device.get_result()
                for x in layout:
                    if (isinstance(x, LTTextBoxHorizontal)):
                        #处理每行数据
                        if toPath == "":
                            #处理每一行数据
                            str = x.get_text()
                            if callback != None:
                                callback(str)
                            else:
                                print(str)
                        else:
                            #写文件
                            print("将PDF文件写入文件：")


