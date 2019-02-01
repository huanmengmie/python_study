import socket
import os

# 创建socket对象
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址及端口号
local_addr = ("", 9528)
tcp_server.bind(local_addr)

# 监听客户端链接，允许链接的数量
tcp_server.listen(10)
print("服务器准备好了，来链接我吧")

# 等待客户端链接
new_client, client_addr = tcp_server.accept()

# 获取客户端数据
content = new_client.recv(1024).decode("utf8")
if os.path.isfile(content):
    with open(content, "rb") as file:
        file_content = file.read()
        new_client.send(file_content)
else:
    print(content+"文件找不到")

# 关闭客户端的链接
new_client.close()

# 关闭链接
tcp_server.close()
