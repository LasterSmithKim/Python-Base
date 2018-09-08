'''
fetchone()
功能：获取下一个查询结果集，结果集是一个对象

fetchall()
功能：接收全部的返回的行

rowcount:是一个只读属性，返回execute()方法影响的行数（你查了多少条数据）

'''

import pymysql
db = pymysql.connect("192.168.56.101","root","Smith123!","sunck")
cursor = db.cursor()


sql = 'select * from bandcard where money > 400'

try:
        cursor.execute(sql)

        relist = cursor.fetchall()
        for row in relist:
            print("%d--%d" % (row[0],row[1]))

except:
        #如果提交失败，回滚到上一次的数据
        db.rollback()
        print("数据回滚")


cursor.close()
db.close()