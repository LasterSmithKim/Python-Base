#发邮件的库
import smtplib
#邮件文本
from email.mime.text import  MIMEText

#SMTP邮件服务器
SMTPServer = "smtp.yeah.net"
#发送邮件的邮箱地址
sender = "*******@yeah.net"
#发送邮箱的POP3授权密码
passwd = "*******"

receiver = "*******@yeah.net"


#设置发送的内容
message = "测试邮件发送功能是否成功。测试邮件发送功能是否成功。测试邮件发送功能是否成功。"
#转换成邮件文本
msg = MIMEText(message)

#邮件主题
msg["Subject"] = "测试邮件，发送是否成功。"
#邮件发送者
msg["From"] = sender
#邮件接收者
msg["To"] = receiver

#创建SMTP服务器连接
mailServer = smtplib.SMTP(SMTPServer,25)
#登录邮箱
mailServer.login(sender,passwd)
#发送邮件
mailServer.sendmail(sender,receiver,msg.as_string())
#退出邮箱登录
mailServer.quit()

