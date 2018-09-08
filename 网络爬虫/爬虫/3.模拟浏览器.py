import urllib.request
import random

'''
url = "http://fanyi.baidu.com"
#模拟请求头
headers = {
    "Accept":"                 ",  #连接
    "X-Requested-With":"       ",  #请求对象的类型
    "Content-Type":"           ",  #请求类型



    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}
#设置一个请求体
req = urllib.request.Request(url,headers=headers)
#发起请求
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)
'''
#url = "http://www.baidu.com"
url = "http://fanyi.baidu.com"
agnetsList = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
]

agentStr = random.choice(agnetsList)
req = urllib.request.Request(url)
#向请求体里 添加了 User-Agent
req.add_header("User-Agent",agentStr)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))



