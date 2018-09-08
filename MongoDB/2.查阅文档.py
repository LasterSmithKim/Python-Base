from pymongo import MongoClient
from bson.objectid import ObjectId#用于ID查询数据
import pymongo

#连接数据库
conn = MongoClient("mongodb://smith:smith123@192.168.56.101:27017/sunck")
#获取数据库
db = conn.sunck
#获取集合
collection = db.student
#查询文档

#查询部分文档
'''
res = collection.find({"age":{"$gt":18}})
for row in res:
    print(row)
    print(type(row))
'''
#查询所有文档
'''
res = collection.find()
for row in res:
    print(row)
'''
#统计查询
'''
res = collection.find({"age":{"$gt":18}}).count()
print(res)
'''
#根据ID查询
'''
res1 = collection.find({"_id":ObjectId("5b7b6f918c47540ecdc78a4e")})
print(res1[0])
'''
#结果排序
'''
#res = collection.find().sort("age")#默认升序
res = collection.find().sort("age",pymongo.DESCENDING)#降序
for row in res:
    print(row)
'''

#分页取数据
res = collection.find().skip(3).limit(5)
for row in res:
    print(row)


#断开连接
conn.close()






