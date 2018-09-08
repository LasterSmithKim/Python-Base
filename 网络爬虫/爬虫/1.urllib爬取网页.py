import urllib.request




#向指定的url地址发起请求，并返回服务器响应的数据（文件的对象）
response = urllib.request.urlopen("http://www.baidu.com")


#读取全部数据，读取到的数据赋值给一个字符串变量
data = response.read()
print(data)
print(type(data))





#读取一行
#data = response.readline()
#print(data)


#读取文件的全部内容 会把读取到的数据赋值给一个列表变量 list变量
#data = response.readlines()
'''
print(data)
print(type(data))
print(len(data))
print(type(data[100]))
print(type(data[100].decode("utf-8")))
#将每一行的数据 转换成 .decode("utf-8") str类型的 ，然后才能使用正则表达式等功能处理数据
'''


#将爬取到的网页写入文件
#with open(r"/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/网络爬虫/file/file1.html","wb") as f:
#    f.write(data)


#response 属性

#返回当前环境的有关信息
#print(response.info())

#返回状态码
#print(response.getcode())
#if response.getcode() == 200 or response.getcode()== 304:
    #处理网页
#    pass

#返回当前正在爬取的URL地址
#print(response.geturl())


url = "http://www.baidu.com"
#编码
newUr2 = urllib.request.quote(url)
print(newUr2)
#解码
newUr1 = urllib.request.unquote(newUr2)
print(newUr1)







