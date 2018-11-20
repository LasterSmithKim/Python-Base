# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import ssl
import re,os
import urllib.request



def read_file_as_str():
    file_path = os.path.join('bak.txt')
    all_the_text = open(file_path).read()
    return all_the_text



def getHtmlStr(url,str):

    xing = "金"
    postdata = urllib.parse.urlencode({
        "xing":xing.encode("gbk"),
        "ming":xing.encode("gbk"),



        }).encode("gbk") #将数据使用urlencode编码后，使用encode（）设置utf-8编码

    '''
          "sex": 1,
          "wxxy":1,
          "data_type":"nongli",
          "year":1991,
          "month":2,
          "day":1,
          "hour":12,
          "minute":12,
        '''


    req = urllib.request.Request(url,postdata)
    context = ssl._create_unverified_context()
    req.add_header(
            "User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 "\
                          "(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
    data = urllib.request.urlopen(req).read().decode("gbk","ignore")
    return data


    '''
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 "\
                      "(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }

    postdata = urllib.parse.urlencode({
        "xingx": str.encode("gbk"),
        "mingx": str.encode("gbk")}).encode("gbk")  # 将数据使用urlencode编码后，使用encode（）设置utf-8编码
    req = urllib.request.Request(url, postdata)
    context = ssl._create_unverified_context()
    req.add_header(
        "User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 " \
                      "(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
    data = urllib.request.urlopen(req).read().decode("gbk", "ignore")
    print(data)
    '''

def mingCrawler(url,str):
    htmlStr=getHtmlStr(url,str)
    print(htmlStr)
    #筛选需要的信息



    '''
    正则表达式
    pat1 = "<span>(\d+)</span>"
    re_1 = re.compile(pat1)
    List1 = re_1.findall(htmlStr)
    print("金"+str+"  "+List1[0])
    '''


if __name__ == "__main__":
    url = "http://life.httpcn.com/xingming.asp"
    str = "佩华"
    mingCrawler(url,str)










