import urllib.request
import ssl
import re

def getHtmlStr(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 "\
                      "(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)
    return response.read().decode("utf-8")

def ipCrawler(url):
    htmlStr=getHtmlStr(url)
    #print(htmlStr)
    pat = r"" + ip + "查询结果,地理位置：.*?,"
    re_url = re.compile(pat)
    urlsList = re_url.findall(htmlStr)
    print(urlsList[0][:-1])

if __name__ == "__main__":
    ip = input("请输入ip地址：")
    url = "http://ip.yqie.com/ip.aspx?ip=" + ip
    ipCrawler(url)