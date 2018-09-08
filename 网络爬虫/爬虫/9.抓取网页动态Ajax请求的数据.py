
import urllib.request
import ssl
import json

def ajaxCrawler(url):

    req = urllib.request.Request(url)
    #使用SSL创建未验证的上下文
    context = ssl._create_unverified_context()

    response = urllib.request.urlopen(req,context=context)


    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)


    return jsonData

'''
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20"
info = ajaxCrawler(url)
print(info)
'''

for i in (1,11):
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+str(i*10)+"&limit=20"
    info = ajaxCrawler(url)
    print(len(info))
