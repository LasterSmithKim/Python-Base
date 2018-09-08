from pymongo import MongoClient

#连接数据库
conn = MongoClient("mongodb://smith:smith123@192.168.56.101:27017/sunck")
#获取数据库
db = conn.sunck
#获取集合
collection = db.student
#添加文档
#collection.insert({"name":"abc","age":22,"gender":0,"address":"上海","isDelete":0})
collection.insert([{"name":"abc1","age":22,"gender":0,"address":"上海","isDelete":0},
                   {"name":"edf","age":22,"gender":1,"address":"上海","isDelete":0},
                   {"name":"gha","age":22,"gender":0,"address":"上海","isDelete":0},
                   ])

#断开连接
conn.close()
