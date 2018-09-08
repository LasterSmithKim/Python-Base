import pymysql

#参数：ip user password database
db = pymysql.connect("192.168.1.111","root","Smith123!","sunck")
#db = pymysql.connect(host = '192.168.1.111', port = 3306, user = 'root', passwd = 'Smith123!', db = 'sunck', charset="utf8")
#创建一个cursor对象
cursor = db.cursor()


sql = "select version()"

#执行sql语句
cursor.execute(sql)

#获取返回的信息
data = cursor.fetchone()


print(data)
#断开
cursor.close()
db.close()