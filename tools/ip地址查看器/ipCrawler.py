import urllib.request
import ssl
import re
import collections



#读取ip字符串集
def read_file_as_str():
    file_path = "ip.txt"
    all_the_text = open(file_path).read()
    return all_the_text


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
    pat = r"" + ipadd + "查询结果,地理位置：.*?,"
    re_url = re.compile(pat)
    urlsList = re_url.findall(htmlStr)
    #print(urlsList)
    #判断重复次数，以显示不同的警告色
    #设置ip重复倍数值
    multiple = 1
    if dic.get(ipadd)>100:
        print('\033[1;31m%s\033[0m' % (urlsList[0][:-1]) + "  " + '\033[1;31m%s\033[0m' % str(int((dic.get(ipadd) / multiple))) + '\033[1;31m%s\033[0m' % " 次")
    elif dic.get(ipadd)>50:
        print((urlsList[0][:-1]) + "  " + '\033[1;31m%s\033[0m' % str(int((dic.get(ipadd) / multiple))) + '\033[1;31m%s\033[0m' % " 次")
    elif dic.get(ipadd)>10:
        print((urlsList[0][:-1]) + "  " + str(int((dic.get(ipadd) / multiple))) + '\033[1;31m%s\033[0m' % " 次")
    else:
        print((urlsList[0][:-1]) + "  " + str(int((dic.get(ipadd) / multiple))) + " 次")


if __name__ == "__main__":
    #获取文档字符串  请在ip.txt中添加 文本集合
    ip = str(read_file_as_str())
    # 查找所有的IP号码
    pat = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    re_ip = re.compile(pat)
    ipList = re_ip.findall(ip)
    ipLists = re_ip.findall(ip)
    ipList = list(set(ipList))
    #print(ipList)
    dic = collections.Counter(ipLists)
    for ipadd in ipList:
        ipa = ipadd
        url = "http://ip.yqie.com/ip.aspx?ip=" + ipadd
        ipCrawler(url)
