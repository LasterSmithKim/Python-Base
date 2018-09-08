import time

class Admin(object):

    admin = "1"
    passwd = "1"


    def printadminView(self):
        print("********************************************************************")
        print("*                                                                  *")
        print("*                      欢迎登录银行管理员界面                         *")
        print("*                                                                  *")
        print("*                                                                  *")
        print("*                                                                  *")
        print("*                                                                  *")
        print("********************************************************************")



    def printSysFunctionView(self):
        print("********************************************************************")
        print("*                                                                  *")
        print("*                      欢迎登录银行用户界面                           *")
        print("*     开户(1)                               查询(2)                 *")
        print("*     取款(3)                               存款(4)                 *")
        print("*     转账(5)                               改密码(6)               *")
        print("*     锁定(7)                               解锁(8)                 *")
        print("*     补卡(9)                               销户(0)                 *")
        print("*     退出(q)                                                      *")
        print("*                                                                  *")
        print("*                                                                  *")
        print("*                                                                  *")
        print("********************************************************************")

    def adminOption(self):
        inputadmin = input("请输入管理员账号：")
        if self.admin != inputadmin:
            print("账号输入有误！！")
            return -1
        inputPasswd = input("请输入密码：")
        if self.passwd != inputPasswd:
            print("输入密码有误！！")
            return -1
        # 能执行到这里，说明账号、密码正确
        print("操作成功，请稍后...")
        time.sleep(2)
        return 0



