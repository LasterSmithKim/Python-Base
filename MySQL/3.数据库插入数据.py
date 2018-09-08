import pymysql
db = pymysql.connect("192.168.56.101","root","Smith123!","sunck")
cursor = db.cursor()


sql = 'insert into bandcard values(0,700)'

try:
        cursor.execute(sql)
        db.commit() #提交事务
        print("数据已提交")
except:
        #如果提交失败，回滚到上一次的数据
        db.rollback()
        print("数据回滚")


cursor.close()
db.close()