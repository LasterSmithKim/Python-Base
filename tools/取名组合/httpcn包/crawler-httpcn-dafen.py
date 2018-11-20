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

    xing = ("金").encode("gb2312")
    ming = str.encode("gb2312")
    postdata = urllib.parse.urlencode({
        "data_type":"0",
        "RenYue":"0",
        "year":"2018",
        "month":"11",
        "day":"18",
        "hour":"17",
        "minute":"10",
        "pid":(b'\xc9\xcf\xba\xa3'),
        "cid":(b'\xc9\xcf\xba\xa3'),
        "zty":"1",
        "wxxy":"0",
        "xishen":(b'\xbd\xf0'),
        "yongshen":(b'\xbd\xf0'),
        "xing":xing,
        "ming":ming,
        "sex":"0",
        "act":"submit",
        "isbz":"1",
        }).encode("utf-8") #将数据使用urlencode编码后，使用encode（）设置utf-8编码

    req = urllib.request.Request(url,postdata)
    context = ssl._create_unverified_context()
    req.add_header(
            "User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 "\
                          "(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
    data = urllib.request.urlopen(req).read().decode("gb2312","ignore")
    return data



def mingCrawler(url,str):
    htmlStr=getHtmlStr(url,str)
    #print(htmlStr)
    #筛选需要的信息

    pat1 = "姓名五格评分：<font style=\"color:#3333FF;font-size:24px;font-family:arial;\"><b>(.*)</b> 分</font>"
    re_1 = re.compile(pat1)
    List1 = re_1.findall(htmlStr)
    pat2 = "姓名八字评分：<font style=\"color:#E24223;font-size:24px;font-family:arial;\"><b>(.*)</b> 分</font>"
    re_2 = re.compile(pat2)
    List2 = re_2.findall(htmlStr)

    return ("金"+str + " " + List1[0] + " " + List2[0])

if __name__ == "__main__":
    #循环文件行数
    num_col = 0;
    for line in open('from-data2.txt'):
        line = line.strip('\n')
        num_col = num_col + 1

    url = "http://life.httpcn.com/xingming.asp"
    num_work = 0
    for line in open('from-data2.txt'):
        line = line.strip('\n')
        file = os.path.join('to-data2-end.txt')
        mingCrawler(url, str(line))
        with open(file, 'a+') as f:
            f.write(mingCrawler(url, str(line)) + '\n')
            num_work = num_work + 1
            print(str(num_col) + "-" + str(num_work))







