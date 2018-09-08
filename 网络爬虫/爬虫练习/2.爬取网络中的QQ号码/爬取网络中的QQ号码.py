import urllib.request
import ssl
import re
import os
from collections import deque


def writeFileBytes(htmlBytes,toPath):
    with open(toPath,"wb") as f:
        f.write(htmlBytes)
def writeFileStr(htmlBytes,toPath):
    with open(toPath,"w") as f:
        f.write(str(htmlBytes))

def getHtmlBytes(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 "\
                      "(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)
    return response.read()


def qqCrawler(url,toPath):
    htmlBytes = getHtmlBytes(url)
    #writeFileBytes(htmlBytes,toPath1)
    #writeFileStr(htmlBytes,toPath2)
    htmlStr = str(htmlBytes)



    pat = r"(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)"
    re_url = re.compile(pat)
    urlsList = re_url.findall(htmlStr)
    #去重复
    urlsList = list(set(urlsList))




    #查找所有的QQ号码
    pat = r"[1-9]\d{4,9}"
    re_qq = re.compile(pat)
    qqsList = re_qq.findall(htmlStr)
    #去重复
    qqsList = list(set(qqsList))
    #qq号码追加写入文件
    f = open(toPath,"a")
    for qqStr in qqsList:
        f.write(qqStr+"\n")
    f.close()

    return urlsList

def center(rul,toPath):
    queue = deque()

    queue.append(url)
    while len(queue) != 0:
        targetUrl = queue.popleft()
        urlList = qqCrawler(targetUrl, toPath)
        for item in urlList:
            tempUrl = item[0]
            queue.append(tempUrl)

url = r"https://www.douban.com/group/topic/17359302/?start=0"
toPath = "/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/网络爬虫/file/qqFile.txt"
toPath1 = "/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/网络爬虫/file/qqFile1.html"
toPath2 = "/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/网络爬虫/file/qqFile2.txt"
#qqCrawler(url,toPath)
center(url,toPath)

