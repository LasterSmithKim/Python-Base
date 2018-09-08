import urllib.request
import ssl
import re

def jokeCrawler(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
              }
    req = urllib.request.Request(url,headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)

    HTML = str(response.read().decode("utf-8"))
    #with open(r"/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/网络爬虫/file/file3.html","w") as f:
    #    f.write(HTML)

    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    re_joke = re.compile(pat,re.S) #re.S 将 （.*?）中的点 能够匹配换行
    divList = re_joke.findall(HTML)
    #print(divlist)
    #print(len(divlist))
    dic = {}
    for div in divList:
        #用户名
        re_u = re.compile(r"<h2>(.*?)</h2>",re.S)
        username = re_u.findall(div)
        username = username[0]
        #print(username)
        #print(type(username))


        #段子
        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
        duanzi = re_d.findall(div)
        duanzi = duanzi[0]

        dic[username] = duanzi

    return dic


url = "https://www.qiushibaike.com/text/page/2/"
info = jokeCrawler(url)
for k,v in info.items():
    print(k + "说：\n" + v)