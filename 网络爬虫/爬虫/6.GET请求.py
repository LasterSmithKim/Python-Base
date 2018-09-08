'''
特点：把数据拼接到请求路劲后面传递给服务器
优点：速度快
缺点：承载的数据量小，而且不安全



'''
import urllib.request
url = "http://www.sunck.wang:8085/sunck"
responese = urllib.request.urlopen(url)
data = responese.read().decode("utf-8")
print(data)

