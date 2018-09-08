import redis

#连接
r = redis.StrictRedis(host="192.168.56.101",port=6379,password="smith123")

#方式1：根据数据类型的不同，调用响应的方法
#写
#r.set("p2","nice")
#读
#print((r.get("p2")).decode("utf-8"))
#lpush key value [value ...]
#r.lpush('ss1',1,2,3,4)


#方式2:pipline
#缓冲多条命令，然后依次执行，减少服务器-客户端之间的TCP数据包
pipe = r.pipeline()
pipe.set("p2","nice")
pipe.set("p3","good")
pipe.set("p4","handsome")
pipe.set("p5","nice1")
pipe.execute()



