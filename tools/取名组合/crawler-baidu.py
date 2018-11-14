# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import ssl
import re

def getHtmlStr(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 "\
                      "(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    #套件1
    req = urllib.request.Request(url,headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)
    return response.read().decode("utf-8")
    #套件2
    #responese = urllib.request.urlopen(url)
    #data = responese.read().decode("gbk")
    #return data

def mingCrawler(url):
    htmlStr=getHtmlStr(url)
    print(htmlStr)
    #筛选需要的信息


if __name__ == "__main__":

    ming = urllib.parse.quote("银",encoding='utf8')
    url = str("https://hanyu.baidu.com/zici/s?wd=" + ming
              + "&query="+"%E6%B1%89%E5%AD%97%E4%BA%94%E8%A1%8C"+"&srcid=28204&from=kg0&from=kg0")
    mingCrawler(url)
