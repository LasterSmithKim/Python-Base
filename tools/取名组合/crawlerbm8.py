# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import ssl
import re,os

def read_file_as_str():
    file_path = os.path.join('basedata.txt')
    all_the_text = open(file_path).read()
    return all_the_text

def getHtmlStr(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 "\
                      "(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }

    try:
        responese = urllib.request.urlopen(url)
        return responese.read().decode('gbk')
    except:
        return "未知错误"


def mingCrawler(url):
    htmlStr=getHtmlStr(url)
    #筛选需要的信息

    pat1 = "<td><strong>五行属性</strong>：.*?</td>"
    pat2 = "<td>吉凶：.*?</td>"
    pat3 = "<td colspan=5 bgcolor=\"#FFFFFF\">.*?,"
    pat4 = "<td>笔画：.*?</td>"
    pat5 = "<td colspan=5 bgcolor=\"#FFFFFF\"><strong>.*? </div></div></td>"

    re_1 = re.compile(pat1)
    re_2 = re.compile(pat2)
    re_3 = re.compile(pat3)
    re_4 = re.compile(pat4)
    re_5 = re.compile(pat5)

    List1 = re_1.findall(htmlStr)
    List2 = re_2.findall(htmlStr)
    List3 = re_3.findall(htmlStr)
    List4 = re_4.findall(htmlStr)
    List5 = re_5.findall(htmlStr)
    if len(List1):
        pass
    else:
        List1 = ["空数据"]
    if len(List2):
        pass
    else:
        List2 = ["空数据"]
    if len(List3):
        pass
    else:
        List3 = ["空数据"]
    if len(List4):
        pass
    else:
        List4 = ["空数据"]
    if len(List5):
        pass
    else:
        List5 = ["空数据"]
    strs = List1[0]+ " " +List2[0]+ " " +List3[0]+ " " +List4[0]+" " +List5[0].replace(' ', '')
    return strs

    #pat1 = "<td><strong>五行属性</strong>：.*?</td>"
    #pat2 = "<td>吉凶：.*?</td>"
    #pat3 = "<td colspan=5 bgcolor=\"#FFFFFF\">.*?,"
    #pat4 = "<td>笔画：.*?</td>"
    #pat5 = "<td colspan=5 bgcolor=\"#FFFFFF\"><strong>.*? </div></div></td>"

#if __name__ == "__main__":

def cooking(ming):
    ming_gbk = str(ming.encode('gbk'))
    ming_gbkstr = "%" + ming_gbk[4:6] + "%" + ming_gbk[8:-1]
    url = str("http://wuxing.bm8.com.cn/zi/"+ming_gbkstr+".html")
    print(url)
    x = mingCrawler(url)
    return x



    '''
    strs = str(read_file_as_str())
    num = len(strs)
    for i in range(0, len(strs)):
        ming = strs[i][0]
        ming_gbk = str(ming.encode('gbk'))
        print(ming_gbk)
        ming_gbkstr = "%" + ming_gbk[4:6] + "%" + ming_gbk[8:-1]
        url = str("http://wuxing.bm8.com.cn/zi/" + ming_gbkstr + ".html")
        print(url)
    '''


















