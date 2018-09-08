
import urllib.request

urllib.request.urlretrieve("http://www.baidu.com",filename=r"/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/网络爬虫/file/file2.html")


#urlretrieve这个方法在执行的过程中，会产生一些缓存
#清除缓存
urllib.request.urlcleanup()