from pymongo import MongoClient
from bson.objectid import ObjectId#用于ID查询数据
import pymongo

conn = MongoClient("mongodb://smith:smith123@192.168.56.101:27017/sunck")
db = conn.sunck
collection = db.student
#条件删除
collection.remove({"name":"abc"})
#全部删除
#collection.remove()
conn.close()

