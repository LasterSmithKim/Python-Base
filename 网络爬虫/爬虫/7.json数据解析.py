import json
'''
概念：一种保存数据的格式
作用：可以保存本地的json文件，也可以将json字符串进行传输，通常将json称为轻量级的传输方式

xml早期的格式

json的组成
{}  代表对象（字典）
[]  代表列表  
:   代表键值对
,   分隔两个部分

'''



jsonStr = '{"name":"sunck","age":18,"hobby":["money","power","english"],"parames":{"a":1,"b":2}}'

#将json格式的字符串转为python的数据类型的对象
jsonData = json.loads(jsonStr)
print(jsonData)
print(type(jsonData))
print(jsonData["hobby"])

#将python数据类型的对象转为json格式的字符串
jsonStr2 = {'name': 'sunck', 'age': 18, 'hobby': ['money', 'power', 'english'], 'parames': {'a': 1, 'b': 2}}
jsonData2 = json.dumps(jsonStr2)
print(jsonData2)
print(type(jsonData2))

#读取本地的json文件
path1 = r"/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/网络爬虫/file/json文件.json"
with open(path1,"rb") as f:
    data = json.load(f)
    print(data)
    #字典类型
    print(type(data))

#写本地json
path2 = r"/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/网络爬虫/file/test.json"
jsonData3 = {'name': 'sunck', 'age': 18, 'hobby': ['money', 'power', 'english'], 'parames': {'a': 1, 'b': 2}}
with open(path2,"w") as f1 :
    json.dump(jsonData3,f1)


