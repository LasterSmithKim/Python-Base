import urllib.request
import re
import os

def imageCrawler(url,toPath):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    htmlStr = response.read().decode("utf-8")
    #with open(r"/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/网络爬虫/file/1haodian.html","wb") as f:
        #f.write(htmlStr)

    pat = r'<div style="position: relative">\n<img src="//(.*?)"/>'
    re_image = re.compile(pat,re.S)
    imageList = re_image.findall(htmlStr)
    #print(imageList)
    num = 1
    for imageUrl in imageList:
        path = os.path.join(toPath,str(num)+".jpg")
        num += 1
        #把图片下载到本地
        urllib.request.urlretrieve("http://"+imageUrl,filename=path)


url = "http://search.yhd.com/c9719-0-0/mbname-b/a-s1-v0-p1-price-d0-f0-m1-rt0-pid-mid0-color-size-k/"
toPath = "/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/网络爬虫/file/image"

imageCrawler(url,toPath)