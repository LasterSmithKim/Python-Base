import socket

#创建一个socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定IP和端口
server.bind(("127.0.0.1",8080))
#监听
server.listen(5)
print("服务器启动成功")
#等待连接
clientSocket, clientAddress = server.accept()

print("%s -- %s 连接成功" % (str(clientSocket),clientAddress))

while True:
    data = clientSocket.recv(1024)
    print("收到"+str(clientSocket)+"的数据："+data.decode("utf-8"))
    clientSocket.send("你也好帅".encode("utf-8"))



