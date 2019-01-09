import socket

# 创建socket对象
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址及端口号
local_addr = ("", 9528)
tcp_server.bind(local_addr)

# 监听客户端链接，将套接字由主动改为被动
tcp_server.listen(10)

# 等待客户端链接
new_client, client_addr = tcp_server.accept()
print(new_client, client_addr)

# 获取客户端数据 等待数据时进入阻塞状态
# 解阻塞的两种情况：
#   1、获取到数据
#   2、客户端调用socket.close()方法，不会返回任何数据
content = new_client.recv(1024)
print("%s:%s" % (str(client_addr), content.decode("utf8")))

# 关闭客户端的链接
new_client.close()

# 关闭链接
tcp_server.close()