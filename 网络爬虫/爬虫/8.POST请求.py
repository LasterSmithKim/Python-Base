'''
特点：把参数进行打包，单独传输
优点：数据量大，安全（当对服务器数据修改时，建议使用post）
缺点：速度慢


'''
import urllib.request
import urllib.parse

url = "http://www.sunck.wang:8085/form"
#将要发送的数据合成一个字典
#字典的键去网址分析里面找，一般为input标签的name属性的值
data = {
    "username":"sunck",
    "passwd":"666"
}

#对要发送的数据进行打包 注意：编码 encode
postData = urllib.parse.urlencode(data).encode("utf-8")
#创建请求体
req = urllib.request.Request(url,data=postData)
#请求
req.add_header("User-Agent","Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))

#需要服务器配合使用

